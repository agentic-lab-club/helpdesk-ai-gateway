package com.form.FormFullStack.api;

import com.form.FormFullStack.model.dto.FormData;
import com.form.FormFullStack.model.dto.Output;
import com.form.FormFullStack.service.FormService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import java.util.concurrent.CompletableFuture;

@RestController
@RequestMapping("/api/v1")
@RequiredArgsConstructor
public class FormController {

    private final FormService formService;

    @PostMapping("/start")
    @ResponseStatus(HttpStatus.CREATED)
    public CompletableFuture<Output> startChat(@RequestBody FormData data) {
        return formService.startChat(data);
    }
}
