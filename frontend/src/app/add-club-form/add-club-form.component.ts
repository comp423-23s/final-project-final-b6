import { Component } from '@angular/core';
import { Route } from '@angular/router';

@Component({
  selector: 'app-add-club-form',
  templateUrl: './add-club-form.component.html',
  styleUrls: ['./add-club-form.component.css']
})
export class AddClubFormComponent {
  static Route: Route = {
    path: 'add-club-form',
    component: AddClubFormComponent, 
    title: 'Add Club Form', 
  };
}


