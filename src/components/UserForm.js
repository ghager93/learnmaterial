import { useNavigate } from "react-router-dom";
import { useFormik } from "formik";
import { object, string, ref } from "yup";
import { TextField, Button, Grid } from "@mui/material";

const UserValidation = object().shape({
  username: string().required("Required."),
  email: string().email("Valid email required."),
  password: string().required("Required."),
  confirmPassword: string().oneOf([ref('password')], "Passwords do not match.")
});

const UserForm = () => {
  const formik = useFormik({
    initialValues: {
      username: '',
      email: '',
      password: '',
      confirmPassword: ''
    },
    validationSchema: UserValidation,
    onSubmit: (values) => {
      handleSubmit(values);
    },
  });

  const navigate = useNavigate();

  const handleSubmit = (values) => {
    const requestOptions = {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        'username': values.username,
        'email': values.email,
        'password': values.password
      })
    }
    fetch('api/users', requestOptions)
      .then(response => response.json())
      .then(out => console.log(out));
    navigate('/');
  }

  return (
    <div>
      <form onSubmit={formik.handleSubmit}>
        <Grid container direction={'column'} spacing={1} margin={0} >
          <Grid item padding={1}>
            <TextField
              fullWidth
              id="username"
              name="username"
              label="Username"
              value={formik.values.username}
              onChange={formik.handleChange}
              error={formik.touched.username && Boolean(formik.errors.username)}
              helperText={formik.touched.email && formik.errors.username}
            />
          </Grid>
          <Grid item padding={1}>
            <TextField
              fullWidth
              id="email"
              name="email"
              label="Email"
              value={formik.values.email}
              onChange={formik.handleChange}
              error={formik.touched.email && Boolean(formik.errors.email)}
              helperText={formik.touched.email && formik.errors.email}
            />    
          </Grid> 
          <Grid item padding={1}>
            <TextField
              fullWidth
              id="password"
              name="password"
              label="Password"
              type="password"
              value={formik.values.password}
              onChange={formik.handleChange}
              error={formik.touched.password && Boolean(formik.errors.password)}
              helperText={formik.touched.password && formik.errors.password}
            />
          </Grid>
          <Grid item padding={1}>
            <TextField
              fullWidth
              id="confirmPassword"
              name="confirmPassword"
              label="Confirm Password"
              type="password"
              value={formik.values.confirmPassword}
              onChange={formik.handleChange}
              error={formik.touched.confirmPassword && Boolean(formik.errors.confirmPassword)}
              helperText={formik.touched.confirmPassword && formik.errors.confirmPassword}
            />
          </Grid>
          <Grid item padding={1}>
            <Button color="primary" variant="contained" fullWidth type="submit">
              Submit
            </Button>
          </Grid>
        </Grid>
      </form>
    </div>
  );
};

export default UserForm;
