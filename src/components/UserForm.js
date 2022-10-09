import { Formik, Form, Field, ErrorMessage } from "formik";
import { object, string, ref } from "yup";

const UserValidation = object().shape({
  username: string().required("Required."),
  email: string().email("Valid email required."),
  password: string().required("Required."),
  confirmPassword: string().oneOf([ref('password')], "Passwords do not match.")
});

const UserForm = () => (
  <div>
    <Formik
      initialValues={{
        username: "",
        email: "",
        password: "",
        confirmPassword: "",
      }}
      validationSchema={UserValidation}
      onSubmit={(values, { setSubmitting }) => {
        setTimeout(() => {
          alert(JSON.stringify(values, null, 2));
          setSubmitting(false);
        }, 400);
      }}
    > 
      {({ isSubmitting }) => (
        <Form>
          <h1>Sign Up</h1>
          <Field name="username" />
          <div>
            <ErrorMessage name="username" component="div" />
          </div>
          <Field type="email" name="email" />
          <ErrorMessage name="email" component="div" />
          <Field type="password" name="password" />
          <ErrorMessage name="password" component="div" />
          <Field type="password" name="confirmPassword" />
          <ErrorMessage name="confirmPassword" component="div" />
          <button type="submit" disabled={ isSubmitting }>
            Submit
          </button> 
        </Form>
      )}
    </Formik>
  </div>
);

export default UserForm;
