import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import {ExamsApiService} from './exam/exam-api.service';
import { CustomerService } from './customers/customers.service';



@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [ExamsApiService,
  CustomerService],
  bootstrap: [AppComponent]
})
export class AppModule { }
