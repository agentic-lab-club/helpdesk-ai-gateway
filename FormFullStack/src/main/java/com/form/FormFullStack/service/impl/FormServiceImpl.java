package com.form.FormFullStack.service.impl;

import com.form.FormFullStack.model.dto.FormData;
import com.form.FormFullStack.model.dto.Output;
import com.form.FormFullStack.model.entity.Form;
import com.form.FormFullStack.model.repo.FormUserRepository;
import com.form.FormFullStack.service.FormService;
import lombok.RequiredArgsConstructor;
import org.springframework.ai.chat.memory.ChatMemory;
import org.springframework.ai.chat.messages.SystemMessage;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.UUID;
import java.util.concurrent.CompletableFuture;

@Service
@RequiredArgsConstructor
public class FormServiceImpl implements FormService {


    private final FormUserRepository repository;
    private final ChatModel model;


    @Async("chatExecutor")
    @Override
    public CompletableFuture<Output> startChat(FormData data) {
        UUID id = UUID.randomUUID();

        Form saveForm = Form.builder()
                .id(id)
                .email(data.email())
                .message(data.message())
                .type("FORM_QUESTION")
                .build();

        repository.save(saveForm);

        Prompt prompt = buildHelpDeskPrompt(data);

        return CompletableFuture.supplyAsync(() -> {
            ChatResponse response = model.call(prompt);

            return Output.builder()
                    .id(id)
                    .answer(response.getResult().getOutput().getText())
                    .build();
        });
    }


    private Prompt buildHelpDeskPrompt(FormData data) {
        SystemMessage system = new SystemMessage(
                """
                                        Ты ИИ Help Desk сервис для IT-поддержки.
                                        Отвечай как опытный IT-специалист первой линии:
                                        - говори кратко, по делу;
                                        - обязательно уточняй важные детали, если информации мало;
                                        - работай на русском (и при необходимости можешь использовать казахский);
                                        - если вопрос не про IT/технику, всё равно ответь вежливо и по сути.
                                        Формат ответа: просто текст, без технической разметки и служебных метаданных.
                        
                        """
        );


        UserMessage message =new UserMessage(
                """
                                       Email пользователя: %s
                        
                                       Вопрос пользователя:
                        %s
                        """.formatted(data.email() , data.message())
        );


        return new Prompt(List.of(system, message));
    }
}
