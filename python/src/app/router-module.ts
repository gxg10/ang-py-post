import { NgModule } from "@angular/core";
import { Routes, RouterModule } from '@angular/router';
import { AboutComponent } from "./about/about.component";
import { ContactComponent } from "./contact/contact.component";
import { AppComponent } from "./app.component";
import { AuthGuard } from "./auth-guard";

const appRoutes: Routes = [
    {path: 'about', component: AboutComponent},
    {path: 'contact', canActivate:[AuthGuard], component: ContactComponent}

]

@NgModule({
    imports: [RouterModule.forRoot(appRoutes)],
    exports: [RouterModule]
})
export class AppRoutingModule {

}
