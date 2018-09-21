import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';

import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import {ExamsApiService} from './exam/exam-api.service';
import { CustomerService } from './customers/customers.service';
import { OrderService } from './orders/orders.service';
import {MatDatepickerModule} from '@angular/material/datepicker';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatNativeDateModule, MatInputModule} from '@angular/material';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AboutComponent } from './about/about.component';



@NgModule({
  declarations: [
    AppComponent,
    AboutComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatDatepickerModule,
    MatFormFieldModule,
    MatNativeDateModule,
    MatInputModule,
    FormsModule,
    ReactiveFormsModule

  ],
  providers: [ExamsApiService,
  CustomerService,
OrderService],
  bootstrap: [AppComponent]
})
export class AppModule { }
