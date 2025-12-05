package com.form.FormFullStack.model.repo;

import com.form.FormFullStack.model.entity.Form;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.UUID;

@Repository
public interface FormUserRepository extends JpaRepository<Form , UUID> {

}
