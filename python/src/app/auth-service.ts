export class AuthService {
    loggedIn = false;

    isAutheticated() {
        const promise = new Promise(
            (resolve, reject) => {
                setTimeout(() => {
                    resolve(this.loggedIn);
                }, 800);
            }
        );
        return promise;
    }

    login() {
        this.loggedIn = true;
    }

    loggout() {
        this.loggedIn = false;
    }
}