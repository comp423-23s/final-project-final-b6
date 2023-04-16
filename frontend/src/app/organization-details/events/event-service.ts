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

  getEvent(organizationName: string, eventID: number): Observable<Event>{
    return this.http.get<Event>(`api/${organizationName}/events/${eventID}`)
  }

  editEvent(organizationName: string, event: Event): Observable<Event>{
    const body = {
        id: event.id,
        name: event.name,
        description: event.description,
        date_time: event.date_time,
        location: event.location,
        image: event.image,
        organization_id: event.organization_id
      }
    return this.http.patch<Event>(`api/${organizationName}/events/${event.id}`, body);
  }
  createEvent(organizationName: string, event: Event): Observable<Event>{
    const body = {
        id: event.id,
        name: event.name,
        description: event.description,
        date_time: event.date_time,
        location: event.location,
        image: event.image,
        organization_id: event.organization_id
      }
    return this.http.post<Event>(`api/${organizationName}/events`, body);
  }
}