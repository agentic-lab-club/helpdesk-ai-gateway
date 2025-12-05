package com.form.FormFullStack.model.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.*;
import java.util.UUID;


@Entity
@Builder
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class Form {

    @Id
    private UUID id;

    private String email;

    private String message;

    private String type;

}
