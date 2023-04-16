import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppTitleStrategy } from './app-title.strategy';
import { GateComponent } from './gate/gate.component';
import { HomeComponent } from './home/home.component';
import { ProfileEditorComponent } from './profile/profile-editor/profile-editor.component';
import { OrganizationsComponent } from './organizations/organizations.component';
import { OrganizationDetailsComponent } from './organization-details/organization-details.component';
import {EventEditComponent} from './organization-details/events/event-edit/event-edit.component'
import { OrganizationEditComponent } from './organization-edit/organization-edit.component';
import { OrganizationCreateComponent } from './organization-create/organization-create.component';


const routes: Routes = [
  HomeComponent.Route,
  ProfileEditorComponent.Route,
  OrganizationsComponent.Route,
  GateComponent.Route,
  OrganizationDetailsComponent.Route,
  EventEditComponent.Route,
  OrganizationEditComponent.Route,
  OrganizationCreateComponent.Route,
  { path: 'admin', title: 'Admin', loadChildren: () => import('./admin/admin.module').then(m => m.AdminModule) },
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {
    scrollPositionRestoration: 'enabled',
    anchorScrolling: 'enabled'
  })],
  exports: [RouterModule],
  providers: [AppTitleStrategy.Provider]
})
export class AppRoutingModule {}