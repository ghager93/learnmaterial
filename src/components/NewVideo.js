import { useNavigate } from "react-router-dom";
import { TextField, Button, Grid } from "@mui/material";
import { useFormik } from "formik";
import { object, string } from "yup";

const stripYoutubeURL = (url) => url.match(/.*=(.*)/)[1];

const VideoValidation = object().shape({
  url: string().required("Required."),
});

const NewVideo = () => {
  const formik = useFormik({
    initialValues: {
      username: "",
      name: "",
      youtube_id: "",
      url: "",
    },
    validationSchema: VideoValidation,
    onSubmit: (values) => {
      handleSubmit(values);
    },
  });

  const navigate = useNavigate();

  const handleSubmit = (values) => {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: "username",
        name: values.name,
        youtube_id: stripYoutubeURL(values.url),
        url: values.url,
      }),
    };

    fetch("api/videos", requestOptions)
      .then((response) => response.json())
      .then((out) => console.log(out));
    navigate("/Videos");
  };

  return (
    <div>
      <form onSubmit={formik.handleSubmit}>
        <Grid container direction={"column"} spacing={1} margin={0}>
          <Grid item padding={1}>
            <TextField
              fullWidth
              id="name"
              name="name"
              label="Name"
              value={formik.values.name}
              onChange={formik.handleChange}
            />
          </Grid>
          <Grid item padding={1}>
            <TextField
              fullWidth
              id="url"
              name="url"
              label="URL"
              value={formik.values.url}
              onChange={formik.handleChange}
              error={formik.touched.url && Boolean(formik.errors.url)}
              helperText={formik.touched.url && formik.errors.url}
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

export default NewVideo;
