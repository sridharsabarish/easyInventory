#[macro_use] extern crate rocket;
use rocket::fs::{FileServer, relative};
use rocket::response::Redirect;
mod manual {
    use std::path::{PathBuf, Path};
    use rocket::fs::NamedFile;

    #[rocket::get("/second/<path..>")]
    pub async fn second(path: PathBuf) -> Option<NamedFile> {
        let mut path = Path::new(super::relative!("templates")).join(path);
        if path.is_dir() {
            path.push("index.html");
        }

        NamedFile::open(path).await.ok()
     
    }
}



#[rocket::launch]
fn rocket() -> _ {
    rocket::build()
        .mount("/", rocket::routes![manual::second])
        .mount("/", FileServer::from(relative!("templates")))
}


