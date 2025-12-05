package com.form.FormFullStack.service;

import com.form.FormFullStack.model.dto.FormData;
import com.form.FormFullStack.model.dto.Output;
import java.util.concurrent.CompletableFuture;

public interface FormService {
    CompletableFuture<Output> startChat(FormData data);
}
