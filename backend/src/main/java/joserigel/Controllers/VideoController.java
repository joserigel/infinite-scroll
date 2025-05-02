package joserigel.Controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class VideoController {

  @GetMapping(path = "/")
  public @ResponseBody String health() {
    return "healthy";
  }
}
