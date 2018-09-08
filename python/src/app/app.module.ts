import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import {ExamsApiService} from './exam/exam-api.service';
import { CustomerService } from './customers/customers.service';
import { OrderService } from './orders/orders.service';



@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [ExamsApiService,
  CustomerService,
OrderService],
  bootstrap: [AppComponent]
})
export class AppModule { }
