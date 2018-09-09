import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {API_URL} from '../env';
import {Orders} from './orders.model';

@Injectable()
export class OrderService{
    constructor(private http: HttpClient) {

    }
    getOrders(): Observable<Orders[]> {
        return this.http.get<Orders[]>(`${API_URL}/orders`);
    }

    getOrdersById(id: number): Observable<Orders[]> {
        return this.http.get<Orders[]>(`${API_URL}/orders/${id}`);
    }
}