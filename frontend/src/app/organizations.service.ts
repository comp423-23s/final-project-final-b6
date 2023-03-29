import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { ReturnStatement } from '@angular/compiler';

export interface Organizations {
  id: number;
  name: string;
  overview: string;
  description: string;
  image: string;
}

@Injectable({
  providedIn: 'root'
})
export class OrganizationsService {

  constructor(private http: HttpClient) { }


  getOrganizations() : Observable<Organizations[]> {
    return this.http.get<Organizations[]>("/api/organizations");
  }

}
