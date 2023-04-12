import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable} from 'rxjs';

export interface Event {
  id: number;
  name: string;
  description: string;
  date_time: Date;
  location: string;
  image: string;
  organization_id: number;
}
@Injectable({
  providedIn: 'root'
})

export class EventService {
  constructor(private http: HttpClient) { }

  getOrganizationEvents(organizationName: string): Observable<Event[]>{
    return this.http.get<Event[]>(`api/${organizationName}/events`)
  }

  deleteEvent(eventID: number){
    // TODO Implement once the backend API exists
  }
}