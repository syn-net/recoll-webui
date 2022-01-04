`use strict`

export 
function log_message(message) {
  return console.log(message);
}

export
function log_debug(message) {
  if(DEBUG == 1) {
    return console.debug(message);
  }
}

const api = {
  log_message,
  log_debug,
};

export default api;

