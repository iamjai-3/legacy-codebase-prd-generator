# Schema Relationships - Complete Analysis

Comprehensive analysis of table relationships in both Legacy (Oases) and Target (Lumina) schemas.

## Table of Contents

1. [Comparison Summary](#comparison-summary)
2. [Legacy Schema Relationships](#legacy-schema-relationships)
3. [Target Schema Relationships](#target-schema-relationships)
4. [Relationship Changes](#relationship-changes)

---

## Comparison Summary

| Metric | Legacy (Oases) | Target (Lumina) | Change |
|--------|----------------|-----------------|--------|
| Total Tables | 881 | 966 | +85 |
| Total Relationships | 1764 | 1966 | +202 |

---

## Legacy Schema Relationships


## Table of Contents

1. [Summary Statistics](#summary-statistics)
2. [Table Dependency Hierarchy](#table-dependency-hierarchy)
3. [Highly Connected Tables](#highly-connected-tables)
4. [Detailed Relationships](#detailed-relationships)
5. [Relationship Matrix](#relationship-matrix)

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total Tables | 881 |
| Total Relationships | 1764 |
| Tables with Relationships | 756 |
| Isolated Tables | 125 |

---

## Table Dependency Hierarchy

Tables organized by dependency levels (Level 0 = no dependencies):

### Level 0

- **oaseslive.aaafcb** (0 relationships)
- **oaseslive.accfcb** (0 relationships)
- **oaseslive.account_properties** (0 relationships)
- **oaseslive.accounting_periods** (0 relationships)
- **oaseslive.accounts_references** (1 relationships)
- **oaseslive.aircraft_header_mavis** (0 relationships)
- **oaseslive.aircraft_list_temp** (0 relationships)
- **oaseslive.aircraft_notes** (0 relationships)
- **oaseslive.aircraft_types** (3 relationships)
- **oaseslive.airport_codes** (0 relationships)
- **oaseslive.airvault_lookup** (0 relationships)
- **oaseslive.alert_colors** (10 relationships)
- **oaseslive.amp_datmig_100int** (0 relationships)
- **oaseslive.amp_datmig_a320_100int** (0 relationships)
- **oaseslive.amp_datmig_a320_samint** (0 relationships)
- **oaseslive.amp_datmig_fleet_visit_pack** (30 relationships)
- **oaseslive.amp_datmig_panel_eff** (0 relationships)
- **oaseslive.amp_datmig_panel_notes** (0 relationships)
- **oaseslive.amp_datmig_panels** (0 relationships)
- **oaseslive.amp_datmig_panels_by_card** (0 relationships)
- **oaseslive.amp_datmig_samint** (0 relationships)
- **oaseslive.amp_datmig_task_eff** (0 relationships)
- **oaseslive.amp_datmig_task_eff_a320** (0 relationships)
- **oaseslive.amp_datmig_task_eff_b737** (0 relationships)
- **oaseslive.amp_datmig_withdrawn_tasks** (0 relationships)
- **oaseslive.awsdms_validation_failures_v1** (1 relationships)
- **oaseslive.b737ng_activity_import_table** (1 relationships)
- **oaseslive.batch_file_header** (46 relationships)
- **oaseslive.batfcb** (0 relationships)
- **oaseslive.bbbfcb** (0 relationships)
- **oaseslive.camo_part_issue_alert_emails** (0 relationships)
- **oaseslive.cbcfcb** (0 relationships)
- **oaseslive.cfd_categories** (1 relationships)
- **oaseslive.cfd_categorires_bkpoases405** (1 relationships)
- **oaseslive.cg_ref_codes** (0 relationships)
- **oaseslive.chapter_alert_rates** (0 relationships)
- **oaseslive.chapters** (0 relationships)
- **oaseslive.chcfcb** (0 relationships)
- **oaseslive.credit_notes_header** (0 relationships)
- **oaseslive.currency_conversion** (0 relationships)
- **oaseslive.dckfcb** (0 relationships)
- **oaseslive.document_control_xref** (0 relationships)
- **oaseslive.document_dir_list** (0 relationships)
- **oaseslive.drn_maint_mod_applicability** (0 relationships)
- **oaseslive.drn_notes** (0 relationships)
- **oaseslive.email_licence** (4 relationships)
- **oaseslive.engineering_support_status** (0 relationships)
- **oaseslive.esignoff_roles** (0 relationships)
- **oaseslive.fleet_ata_references** (0 relationships)
- **oaseslive.fleet_build** (0 relationships)
- **oaseslive.fleet_build_chapters** (0 relationships)
- **oaseslive.fleet_chapter** (0 relationships)
- **oaseslive.fleet_header_1** (0 relationships)
- **oaseslive.fleet_header_mavis_1** (0 relationships)
- **oaseslive.fleet_header_mavis_2** (0 relationships)
- **oaseslive.fleet_notes** (0 relationships)
- **oaseslive.flight_types** (0 relationships)
- **oaseslive.forward_schedule_summary_hdr** (0 relationships)
- **oaseslive.forward_schedule_summary_refs** (0 relationships)
- **oaseslive.freight_default_costs** (0 relationships)
- **oaseslive.genlog** (0 relationships)
- **oaseslive.import_messages** (0 relationships)
- **oaseslive.invoice_categories** (37 relationships)
- **oaseslive.ivdfcb** (0 relationships)
- **oaseslive.ivhfcb** (0 relationships)
- **oaseslive.java_object_registry** (0 relationships)
- **oaseslive.job_references** (0 relationships)
- **oaseslive.lasfcb** (0 relationships)
- **oaseslive.lmc_base_data_defs** (1 relationships)
- **oaseslive.lngfcb** (0 relationships)
- **oaseslive.load_attachment_files** (0 relationships)
- **oaseslive.load_manufacturers_files** (0 relationships)
- **oaseslive.logfcb** (0 relationships)
- **oaseslive.maint_cost_mro_works_orders** (0 relationships)
- **oaseslive.manufacturer_codes** (0 relationships)
- **oaseslive.mavemp** (0 relationships)
- **oaseslive.mavlog** (0 relationships)
- **oaseslive.msrfcb** (0 relationships)
- **oaseslive.narrative_build** (0 relationships)
- **oaseslive.oeim_booking_base_data** (3 relationships)
- **oaseslive.oldfcb** (0 relationships)
- **oaseslive.operation_status** (0 relationships)
- **oaseslive.osys_to_aircraft_reg** (0 relationships)
- **oaseslive.part_properties** (0 relationships)
- **oaseslive.pirep_history_1** (0 relationships)
- **oaseslive.pirep_history_2** (0 relationships)
- **oaseslive.pirep_history_3** (0 relationships)
- **oaseslive.pirep_history_4** (0 relationships)
- **oaseslive.pirfcb** (0 relationships)
- **oaseslive.public_holidays** (2 relationships)
- **oaseslive.puwfcb** (0 relationships)
- **oaseslive.release_to_service_statement** (1 relationships)
- **oaseslive.release_types** (0 relationships)
- **oaseslive.relfcb** (0 relationships)
- **oaseslive.remfcb** (0 relationships)
- **oaseslive.removal_history_1** (0 relationships)
- **oaseslive.reqfil** (0 relationships)
- **oaseslive.rfc_status_contacts** (0 relationships)
- **oaseslive.rfid_antenna_txrx_settings** (0 relationships)
- **oaseslive.rfid_black_listed_tags** (0 relationships)
- **oaseslive.rfid_readers** (0 relationships)
- **oaseslive.rfid_users_default_reader** (0 relationships)
- **oaseslive.rfqfil** (0 relationships)
- **oaseslive.sabre_fleet_mel_equipment_map** (0 relationships)
- **oaseslive.sabre_mel_revision_processing** (0 relationships)
- **oaseslive.sabre_message_queue** (0 relationships)
- **oaseslive.sabre_messages** (0 relationships)
- **oaseslive.sap_payment_terms** (0 relationships)
- **oaseslive.scheduled_job_params** (0 relationships)
- **oaseslive.schema_version** (0 relationships)
- **oaseslive.secfcb** (0 relationships)
- **oaseslive.security_group_links** (0 relationships)
- **oaseslive.sfdc_comp_change_review_emails** (0 relationships)
- **oaseslive.shipment_demand_reasons** (0 relationships)
- **oaseslive.shipment_demand_types** (0 relationships)
- **oaseslive.shipment_uom_configuration** (0 relationships)
- **oaseslive.shtnam** (0 relationships)
- **oaseslive.sopfil** (0 relationships)
- **oaseslive.srqfil** (0 relationships)
- **oaseslive.stafcb** (0 relationships)
- **oaseslive.stcomm** (0 relationships)
- **oaseslive.stmisc** (0 relationships)
- **oaseslive.stock_group_depreciation** (0 relationships)
- **oaseslive.stpfil** (0 relationships)
- **oaseslive.streci** (0 relationships)
- **oaseslive.streco** (0 relationships)
- **oaseslive.strfcb** (0 relationships)
- **oaseslive.structural_damage_causes** (0 relationships)
- **oaseslive.structural_damage_parts** (0 relationships)
- **oaseslive.structural_damage_types** (0 relationships)
- **oaseslive.stwfcb** (0 relationships)
- **oaseslive.subchapters** (0 relationships)
- **oaseslive.suppress_recharge_list** (0 relationships)
- **oaseslive.sys_paras** (0 relationships)
- **oaseslive.table_name** (0 relationships)
- **oaseslive.table_name1** (0 relationships)
- **oaseslive.tablename** (0 relationships)
- **oaseslive.tech_log_types** (0 relationships)
- **oaseslive.tester** (0 relationships)
- **oaseslive.tmi_undefined** (0 relationships)

### Level 1

- **oaseslive.batch_record_camo** (1 relationships)
- **oaseslive.customs_status_codes** (2 relationships)
- **oaseslive.fleet_assembles** (1 relationships)
- **oaseslive.invoice_line_notes** (2 relationships)
- **oaseslive.licence_categories** (1 relationships)
- **oaseslive.maint_cost_mro_wo_invoices** (1 relationships)
- **oaseslive.oeim_invoice** (1 relationships)
- **oaseslive.oeim_invoice_snap_public_hol** (1 relationships)
- **oaseslive.oeim_invoice_snap_time_crits** (1 relationships)
- **oaseslive.oeim_invoice_snap_users** (2 relationships)
- **oaseslive.repetitive_defect_header_2** (1 relationships)
- **oaseslive.rp_calendar_addition_type** (1 relationships)

### Level 2

- **oaseslive.PART_NUMBER_CHAPTERS_DJ-82** (154 relationships)
- **oaseslive.access_dim_accounts_info** (65 relationships)
- **oaseslive.access_dim_sales_info** (5 relationships)
- **oaseslive.accomp_bkup** (10 relationships)
- **oaseslive.accomp_hist_delta_1763** (12 relationships)
- **oaseslive.accomp_hist_lost_sched** (10 relationships)
- **oaseslive.accomp_hist_lost_sched_val** (2 relationships)
- **oaseslive.accomp_values_bkup** (2 relationships)
- **oaseslive.accomplishment_history** (31 relationships)
- **oaseslive.accomplishment_history_values** (2 relationships)
- **oaseslive.account_amendment_history** (1 relationships)
- **oaseslive.account_ata_spec_2000_xref** (1 relationships)
- **oaseslive.account_available_warehouses** (12 relationships)
- **oaseslive.account_buying_contacts** (2 relationships)
- **oaseslive.account_header_1** (1 relationships)
- **oaseslive.account_header_2** (1 relationships)
- **oaseslive.account_location_email_address** (1 relationships)
- **oaseslive.account_location_header_1** (1 relationships)
- **oaseslive.account_location_header_2** (1 relationships)
- **oaseslive.account_location_header_3** (1 relationships)
- **oaseslive.account_location_header_4** (1 relationships)
- **oaseslive.account_location_header_5** (2 relationships)
- **oaseslive.account_location_header_6** (3 relationships)
- **oaseslive.account_location_header_7** (1 relationships)
- **oaseslive.account_location_header_8** (1 relationships)
- **oaseslive.account_location_header_9** (3 relationships)
- **oaseslive.account_location_notes** (1 relationships)
- **oaseslive.account_location_properties** (1 relationships)
- **oaseslive.account_supplier_approvals** (5 relationships)
- **oaseslive.account_system_header** (1 relationships)
- **oaseslive.accs_var_corrections_bkp** (1 relationships)
- **oaseslive.accum_cycles_static_data** (2 relationships)
- **oaseslive.add_extension_permissions** (14 relationships)
- **oaseslive.aircraft_assembles** (112 relationships)
- **oaseslive.aircraft_build** (3 relationships)
- **oaseslive.aircraft_build_chapters** (1 relationships)
- **oaseslive.aircraft_documents** (14 relationships)
- **oaseslive.aircraft_exclusions** (3 relationships)
- **oaseslive.aircraft_flight_hours_1** (5 relationships)
- **oaseslive.aircraft_flight_hours_2** (1 relationships)
- **oaseslive.aircraft_header_1** (2 relationships)
- **oaseslive.aircraft_header_2** (2 relationships)
- **oaseslive.aircraft_lease_details** (2 relationships)
- **oaseslive.aircraft_leased_apu** (3 relationships)
- **oaseslive.aircraft_leased_engines** (3 relationships)
- **oaseslive.aircraft_leased_landing_gear** (3 relationships)
- **oaseslive.aircraft_leased_propellers** (3 relationships)
- **oaseslive.aircraft_life** (7 relationships)
- **oaseslive.aircraft_life_dbf1065** (2 relationships)
- **oaseslive.aircraft_major_checks** (5 relationships)
- **oaseslive.aircraft_reg_xref** (1 relationships)
- **oaseslive.aircraft_short_reg_xref** (1 relationships)
- **oaseslive.aircraft_statistics** (1 relationships)
- **oaseslive.aircraft_subchapter_statistics** (1 relationships)
- **oaseslive.aircraft_weight** (1 relationships)
- **oaseslive.aircraft_weight_7487bkp** (1 relationships)
- **oaseslive.aircraft_weight_conf** (4 relationships)
- **oaseslive.aircraft_weight_conf_entries** (1 relationships)
- **oaseslive.aircraft_weight_conf_xref** (2 relationships)
- **oaseslive.airway_bill_references** (6 relationships)
- **oaseslive.alternate_parts** (10 relationships)
- **oaseslive.amp_acc_panel_desc_osd_33348** (2 relationships)
- **oaseslive.amp_access_panel_desc_hdr** (7 relationships)
- **oaseslive.amp_access_panel_descriptions** (2 relationships)
- **oaseslive.amp_access_panel_effectivity** (6 relationships)
- **oaseslive.amp_access_panel_notes** (1 relationships)
- **oaseslive.amp_access_panels_by_workcard** (85 relationships)
- **oaseslive.amp_accesspanel_effectivity_jn** (5 relationships)
- **oaseslive.amp_audit_notes** (9 relationships)
- **oaseslive.amp_comments** (5 relationships)
- **oaseslive.amp_component_intervals** (9 relationships)
- **oaseslive.amp_component_intervals_limits** (3 relationships)
- **oaseslive.amp_component_intervals_stages** (5 relationships)
- **oaseslive.amp_component_reset_on_compl** (2 relationships)
- **oaseslive.amp_data_migration_log** (7 relationships)
- **oaseslive.amp_datmig_accomplishments** (5 relationships)
- **oaseslive.amp_datmig_comp_task_lookup** (7 relationships)
- **oaseslive.amp_datmig_llp** (2 relationships)
- **oaseslive.amp_document_effectivity** (3 relationships)
- **oaseslive.amp_document_effectivity_bk** (3 relationships)
- **oaseslive.amp_documents_by_workcard** (5 relationships)
- **oaseslive.amp_documents_by_workcard_bk** (5 relationships)
- **oaseslive.amp_manufacturers_documents** (2 relationships)
- **oaseslive.amp_material_effectivity** (4 relationships)
- **oaseslive.amp_material_effectivity_jn** (3 relationships)
- **oaseslive.amp_materials_required_by_wc** (3 relationships)
- **oaseslive.amp_package_notes** (31 relationships)
- **oaseslive.amp_packages** (3 relationships)
- **oaseslive.amp_packages_by_visit** (3 relationships)
- **oaseslive.amp_packages_by_workcard** (3 relationships)
- **oaseslive.amp_planning_notes** (9 relationships)
- **oaseslive.amp_report_documents** (27 relationships)
- **oaseslive.amp_revision_history** (3 relationships)
- **oaseslive.amp_revision_status** (10 relationships)
- **oaseslive.amp_revisions** (69 relationships)
- **oaseslive.amp_visit_notes** (2 relationships)
- **oaseslive.amp_visits** (4 relationships)
- **oaseslive.amp_wc_aircraft_exclusions** (3 relationships)
- **oaseslive.amp_wc_in_limits_bak** (2 relationships)
- **oaseslive.amp_wc_in_stages_bak** (1 relationships)
- **oaseslive.amp_wcard_extended_desc_41** (2 relationships)
- **oaseslive.amp_workcard_ac_effectivity** (3 relationships)
- **oaseslive.amp_workcard_ac_effectivity_jn** (3 relationships)
- **oaseslive.amp_workcard_accomplishments** (2 relationships)
- **oaseslive.amp_workcard_activations** (15 relationships)
- **oaseslive.amp_workcard_call_workcard** (6 relationships)
- **oaseslive.amp_workcard_cancellations** (4 relationships)
- **oaseslive.amp_workcard_extended_desc** (2 relationships)
- **oaseslive.amp_workcard_h3_7487bkp** (2 relationships)
- **oaseslive.amp_workcard_header_1** (3 relationships)
- **oaseslive.amp_workcard_header_1_43216** (3 relationships)
- **oaseslive.amp_workcard_header_2** (2 relationships)
- **oaseslive.amp_workcard_header_3** (2 relationships)
- **oaseslive.amp_workcard_header_4** (2 relationships)
- **oaseslive.amp_workcard_header_5** (3 relationships)
- **oaseslive.amp_workcard_header_properties** (2 relationships)
- **oaseslive.amp_workcard_intervals_limits** (9 relationships)
- **oaseslive.amp_workcard_intervals_stages** (1 relationships)
- **oaseslive.amp_workcard_lcl_applicability** (4 relationships)
- **oaseslive.amp_workcard_narrative** (2 relationships)
- **oaseslive.amp_workcard_not_with_workcard** (6 relationships)
- **oaseslive.amp_workcard_previously_acc_by** (4 relationships)
- **oaseslive.amp_workcard_publications** (7 relationships)
- **oaseslive.amp_workcard_saved_reports** (3 relationships)
- **oaseslive.amp_workcard_saved_reports_hdr** (1 relationships)
- **oaseslive.amp_workcard_sections** (13 relationships)
- **oaseslive.amp_workcards_by_package** (4 relationships)
- **oaseslive.amp_workcards_by_section** (4 relationships)
- **oaseslive.assemble_thrust_life_code** (5 relationships)
- **oaseslive.assembly_model_header** (3 relationships)
- **oaseslive.assembly_model_nodes** (3 relationships)
- **oaseslive.audit_trail** (2 relationships)
- **oaseslive.audit_trail_ids** (1 relationships)
- **oaseslive.audit_trail_meta_data** (3 relationships)
- **oaseslive.bar_codes** (4 relationships)
- **oaseslive.batch_history** (2 relationships)
- **oaseslive.batch_notes** (3 relationships)
- **oaseslive.batch_notes_gu4240** (3 relationships)
- **oaseslive.batch_orders** (63 relationships)
- **oaseslive.batch_record_1** (6 relationships)
- **oaseslive.batch_record_1_gu4240** (6 relationships)
- **oaseslive.batch_record_2** (3 relationships)
- **oaseslive.batches_by_airway_bill** (2 relationships)
- **oaseslive.batches_by_customs_entry** (6 relationships)
- **oaseslive.bins** (11 relationships)
- **oaseslive.bkp_mobile_permissions** (2 relationships)
- **oaseslive.block_countries** (6 relationships)
- **oaseslive.bulk_batch_header** (2 relationships)
- **oaseslive.cfd_xref_to_tech_log** (1 relationships)
- **oaseslive.company_codes** (9 relationships)
- **oaseslive.company_form_attachments** (7 relationships)
- **oaseslive.company_form_details** (3 relationships)
- **oaseslive.completion_fleet_ata_pos** (1 relationships)
- **oaseslive.completion_life_values** (4 relationships)
- **oaseslive.completion_maint_mod** (2 relationships)
- **oaseslive.completion_part_serial** (78 relationships)
- **oaseslive.component_life** (3 relationships)
- **oaseslive.component_life_limits** (12 relationships)
- **oaseslive.component_mods_history_by_part** (1 relationships)
- **oaseslive.component_movement_hist_life** (13 relationships)
- **oaseslive.component_movement_history** (2 relationships)
- **oaseslive.component_movement_history_ext** (7 relationships)
- **oaseslive.component_movt_hist_ext_8661** (7 relationships)
- **oaseslive.components** (3 relationships)
- **oaseslive.components_bkp_dj95** (3 relationships)
- **oaseslive.components_bkp_dj97** (3 relationships)
- **oaseslive.components_oases971** (3 relationships)
- **oaseslive.condition_codes** (9 relationships)
- **oaseslive.condition_pick_table** (10 relationships)
- **oaseslive.consumable_batch_locations** (2 relationships)
- **oaseslive.consumable_history** (8 relationships)
- **oaseslive.consumable_repair_xref_to_part** (4 relationships)
- **oaseslive.consumables_below_re_order** (1 relationships)
- **oaseslive.contacts_xref** (1 relationships)
- **oaseslive.continents** (3 relationships)
- **oaseslive.corrosion_categories** (4 relationships)
- **oaseslive.cost_codes** (20 relationships)
- **oaseslive.countries** (1 relationships)
- **oaseslive.cq_documents** (2 relationships)
- **oaseslive.cq_fixed_charge_xref** (4 relationships)
- **oaseslive.cq_quote_cards** (14 relationships)
- **oaseslive.cq_quote_materials** (3 relationships)
- **oaseslive.cq_quote_nrc_access_panels** (18 relationships)
- **oaseslive.cq_quote_nrcs** (3 relationships)
- **oaseslive.cq_quote_packages** (3 relationships)
- **oaseslive.cq_quote_status** (2 relationships)
- **oaseslive.cq_quote_status_contacts** (1 relationships)
- **oaseslive.cq_quotes** (3 relationships)
- **oaseslive.credit_works_order_cards** (10 relationships)
- **oaseslive.credit_works_orders** (1 relationships)
- **oaseslive.crs_signature_text** (2 relationships)
- **oaseslive.crs_text** (3 relationships)
- **oaseslive.currency_codes** (32 relationships)
- **oaseslive.customer_contract_rates** (10 relationships)
- **oaseslive.customer_contract_stop_incl** (3 relationships)
- **oaseslive.customer_contracts** (4 relationships)
- **oaseslive.customer_sales_order_xref** (14 relationships)
- **oaseslive.customs_tariff_codes** (5 relationships)
- **oaseslive.customs_tariff_codes_territory** (1 relationships)
- **oaseslive.daily_loans_out** (3 relationships)
- **oaseslive.dataset_locks_by_lock_type** (1 relationships)
- **oaseslive.dataset_locks_by_user** (17 relationships)
- **oaseslive.default_labour_rates** (3 relationships)
- **oaseslive.default_labour_windows** (3 relationships)
- **oaseslive.defect_extensions** (26 relationships)
- **oaseslive.defect_maint_stages** (1 relationships)
- **oaseslive.defect_stage_employees** (25 relationships)
- **oaseslive.deferred_defect_xref_to_cfd_no** (1 relationships)
- **oaseslive.delay_codes** (6 relationships)
- **oaseslive.delays** (3 relationships)
- **oaseslive.delivery_note_extended_remarks** (14 relationships)
- **oaseslive.delivery_note_header_1** (4 relationships)
- **oaseslive.delivery_note_header_2** (1 relationships)
- **oaseslive.delivery_note_header_3** (1 relationships)
- **oaseslive.delivery_note_header_4** (2 relationships)
- **oaseslive.delivery_note_item_header_1** (15 relationships)
- **oaseslive.delivery_note_item_header_2** (2 relationships)
- **oaseslive.delivery_note_master_list** (1 relationships)
- **oaseslive.demand_reason_to_movement_code** (9 relationships)
- **oaseslive.departments** (4 relationships)
- **oaseslive.dmg_rpr_action_taken_details** (2 relationships)
- **oaseslive.dmg_rpr_attachments** (2 relationships)
- **oaseslive.dmg_rpr_ca_approval_details** (2 relationships)
- **oaseslive.dmg_rpr_corrosion_levels** (2 relationships)
- **oaseslive.dmg_rpr_damage** (22 relationships)
- **oaseslive.dmg_rpr_damage_numbering** (3 relationships)
- **oaseslive.dmg_rpr_damage_types** (3 relationships)
- **oaseslive.dmg_rpr_dmg_2d_position_labels** (5 relationships)
- **oaseslive.dmg_rpr_dmg_2d_positions** (2 relationships)
- **oaseslive.dmg_rpr_doc_effectivity** (5 relationships)
- **oaseslive.dmg_rpr_doc_subject** (5 relationships)
- **oaseslive.dmg_rpr_document_order** (4 relationships)
- **oaseslive.dmg_rpr_documents** (2 relationships)
- **oaseslive.dmg_rpr_fitted_locations** (4 relationships)
- **oaseslive.dmg_rpr_idnt_inspect** (1 relationships)
- **oaseslive.dmg_rpr_idnt_inspect_info** (1 relationships)
- **oaseslive.dmg_rpr_inspection_type_dtls** (7 relationships)
- **oaseslive.dmg_rpr_inspections** (9 relationships)
- **oaseslive.dmg_rpr_interim_repairs** (9 relationships)
- **oaseslive.dmg_rpr_location** (5 relationships)
- **oaseslive.dmg_rpr_location_measurement** (6 relationships)
- **oaseslive.dmg_rpr_mat_types_fld_dtls** (1 relationships)
- **oaseslive.dmg_rpr_material_types_dtls** (4 relationships)
- **oaseslive.dmg_rpr_measurement_sections** (4 relationships)
- **oaseslive.dmg_rpr_measurement_zones** (4 relationships)
- **oaseslive.dmg_rpr_measurements** (1 relationships)
- **oaseslive.dmg_rpr_permanent_repairs** (7 relationships)
- **oaseslive.dmg_rpr_repair_req_details** (2 relationships)
- **oaseslive.dmg_rpr_section_details** (1 relationships)
- **oaseslive.dmg_rpr_section_fleet_details** (1 relationships)
- **oaseslive.dmg_rpr_stage_limits** (3 relationships)
- **oaseslive.dmg_rpr_stages** (5 relationships)
- **oaseslive.dmg_rpr_subject_sections** (4 relationships)
- **oaseslive.dmg_rpr_subject_zones** (3 relationships)
- **oaseslive.dmg_rpr_surface_finish_details** (3 relationships)
- **oaseslive.dmg_rpr_time_limited_repairs** (9 relationships)
- **oaseslive.document_classes** (10 relationships)
- **oaseslive.document_image_source** (23 relationships)
- **oaseslive.document_image_types** (1 relationships)
- **oaseslive.document_images** (1 relationships)
- **oaseslive.document_images_jn** (1 relationships)
- **oaseslive.drn_class_codes** (1 relationships)
- **oaseslive.drn_component_mods_history** (3 relationships)
- **oaseslive.drn_components_nsbl_history** (3 relationships)
- **oaseslive.drn_cycles** (3 relationships)
- **oaseslive.drn_fleet_ata** (2 relationships)
- **oaseslive.drn_life_limits** (4 relationships)
- **oaseslive.drn_maint_mod** (3 relationships)
- **oaseslive.drn_maint_mod_notes** (1 relationships)
- **oaseslive.drn_maintenance_history** (3 relationships)
- **oaseslive.drn_maintenance_history_notes** (1 relationships)
- **oaseslive.drn_mod_desc_order_hist** (2 relationships)
- **oaseslive.drn_modification_history** (3 relationships)
- **oaseslive.drn_modification_history_notes** (1 relationships)
- **oaseslive.drn_part_serial** (3 relationships)
- **oaseslive.dues_register** (4 relationships)
- **oaseslive.dummy_part_numbers** (1 relationships)
- **oaseslive.easa_trace** (3 relationships)
- **oaseslive.economic_blocks** (1 relationships)
- **oaseslive.email_notification** (2 relationships)
- **oaseslive.email_notification_categories** (3 relationships)
- **oaseslive.email_template** (3 relationships)
- **oaseslive.employee_experience_details** (3 relationships)
- **oaseslive.employee_presence** (1 relationships)
- **oaseslive.employee_presence_log** (2 relationships)
- **oaseslive.employee_training_details** (3 relationships)
- **oaseslive.employees** (1 relationships)
- **oaseslive.employees_licences** (4 relationships)
- **oaseslive.end_use_codes** (5 relationships)
- **oaseslive.engineering_support_history** (4 relationships)
- **oaseslive.esign_off_nrc** (2 relationships)
- **oaseslive.export_codes** (7 relationships)
- **oaseslive.extended_part_descriptions** (1 relationships)
- **oaseslive.extensions** (1 relationships)
- **oaseslive.fixed_charges** (1 relationships)
- **oaseslive.fleet_chap_part_header_1** (2 relationships)
- **oaseslive.fleet_chap_part_header_2** (1 relationships)
- **oaseslive.fleet_chap_part_header_3** (1 relationships)
- **oaseslive.fleet_chapter_part_aircraft** (2 relationships)
- **oaseslive.fleet_forecast_plans** (4 relationships)
- **oaseslive.fleet_forecast_plans_amp** (4 relationships)
- **oaseslive.fleet_forecast_plans_drn** (3 relationships)
- **oaseslive.fleet_forecast_plans_rfc** (34 relationships)
- **oaseslive.fleet_header_2** (1 relationships)
- **oaseslive.fleet_statistics** (1 relationships)
- **oaseslive.float_history** (2 relationships)
- **oaseslive.flown_sectors** (9 relationships)
- **oaseslive.flown_sectors_bkp** (4 relationships)
- **oaseslive.flown_sectors_con_680** (4 relationships)
- **oaseslive.flown_sectors_delta1817** (4 relationships)
- **oaseslive.forecast_cache** (11 relationships)
- **oaseslive.forecast_cache_ac_details** (1 relationships)
- **oaseslive.forecast_cache_revisions** (3 relationships)
- **oaseslive.forecast_filter_groups** (9 relationships)
- **oaseslive.forecast_filters** (2 relationships)
- **oaseslive.forecast_parameters** (2 relationships)
- **oaseslive.forecast_variation_details** (1 relationships)
- **oaseslive.form_number** (3 relationships)
- **oaseslive.forward_schedule_summary_vals** (1 relationships)
- **oaseslive.freight_cost_markups** (7 relationships)
- **oaseslive.freight_costs** (3 relationships)
- **oaseslive.future_flights** (1 relationships)
- **oaseslive.gl_global_codes** (2 relationships)
- **oaseslive.goods_received_sheet_document** (7 relationships)
- **oaseslive.hazardous_materials** (1 relationships)
- **oaseslive.ie96_historic** (8 relationships)
- **oaseslive.inherited_acquisition_costs** (3 relationships)
- **oaseslive.invoice_lines** (7 relationships)
- **oaseslive.invoice_system_header** (1 relationships)
- **oaseslive.invoice_trail_entries** (8 relationships)
- **oaseslive.invoices** (3 relationships)
- **oaseslive.jasper_workcard_templates** (1 relationships)
- **oaseslive.lasers_system_header** (1 relationships)
- **oaseslive.latest_repair_values** (3 relationships)
- **oaseslive.ldt** (1 relationships)
- **oaseslive.le80_defect_temp** (1 relationships)
- **oaseslive.life_code_entry** (3 relationships)
- **oaseslive.life_code_entry_backup** (3 relationships)
- **oaseslive.life_code_entry_dbf1065** (3 relationships)
- **oaseslive.life_code_levels** (27 relationships)
- **oaseslive.life_codes** (1 relationships)
- **oaseslive.lmc_base_data_options** (3 relationships)
- **oaseslive.lmc_base_data_reported_wc** (2 relationships)
- **oaseslive.loaned_units** (4 relationships)
- **oaseslive.long_serial_number_xref** (7 relationships)
- **oaseslive.maint_accomplishment_costs** (2 relationships)
- **oaseslive.maint_associated_cost_aircraft** (5 relationships)
- **oaseslive.maint_associated_costs** (2 relationships)
- **oaseslive.maint_card_pref_cost_cats** (1 relationships)
- **oaseslive.maint_cost_budget_adsb** (26 relationships)
- **oaseslive.maint_cost_budget_aircraft** (2 relationships)
- **oaseslive.maint_cost_budget_cfds** (3 relationships)
- **oaseslive.maint_cost_budget_costs** (6 relationships)
- **oaseslive.maint_cost_budget_defects** (3 relationships)
- **oaseslive.maint_cost_budget_labour_ests** (4 relationships)
- **oaseslive.maint_cost_budget_materials** (4 relationships)
- **oaseslive.maint_cost_budget_packages** (5 relationships)
- **oaseslive.maint_cost_budget_visits** (5 relationships)
- **oaseslive.maint_cost_budget_workcards** (8 relationships)
- **oaseslive.maint_cost_hourly_rate_set** (4 relationships)
- **oaseslive.maint_cost_hourly_rates** (3 relationships)
- **oaseslive.maint_cost_mro_wo_quotes** (1 relationships)
- **oaseslive.maint_cost_time_categories** (3 relationships)
- **oaseslive.maint_cost_time_category_set** (23 relationships)
- **oaseslive.maint_hist_associated_costs** (2 relationships)
- **oaseslive.maint_historic_defects** (1 relationships)
- **oaseslive.maint_labour_costs** (1 relationships)
- **oaseslive.maint_material_costs** (6 relationships)
- **oaseslive.maint_nrc_costs** (2 relationships)
- **oaseslive.maint_pack_pref_cost_cats** (1 relationships)
- **oaseslive.maint_works_order_costs** (1 relationships)
- **oaseslive.maintenance_cat_excl_subchap** (1 relationships)
- **oaseslive.maintenance_cat_incl_chapter** (1 relationships)
- **oaseslive.maintenance_cat_incl_parts** (2 relationships)
- **oaseslive.maintenance_cost_budgets** (1 relationships)
- **oaseslive.maintenance_cost_cat_fleet** (1 relationships)
- **oaseslive.maintenance_cost_categories** (1 relationships)
- **oaseslive.maintenance_cost_entry** (2 relationships)
- **oaseslive.maintenance_cost_invoices** (2 relationships)
- **oaseslive.maintenance_cost_quotes** (3 relationships)
- **oaseslive.maintenance_cost_types** (3 relationships)
- **oaseslive.mandatory_parts** (1 relationships)
- **oaseslive.manufacturers_work_documents** (2 relationships)
- **oaseslive.marketing_codes** (3 relationships)
- **oaseslive.markups** (1 relationships)
- **oaseslive.material_pool_agreement** (5 relationships)
- **oaseslive.material_pool_agreement_ac** (2 relationships)
- **oaseslive.material_pool_agreement_pn** (2 relationships)
- **oaseslive.mavis_system_header** (1 relationships)
- **oaseslive.maximum_preload_pick_quantity** (1 relationships)
- **oaseslive.measurement_alerts_aircraft** (4 relationships)
- **oaseslive.measurement_alerts_fleet** (3 relationships)
- **oaseslive.mel_items** (1 relationships)
- **oaseslive.mel_references** (1 relationships)
- **oaseslive.mel_revision_history** (6 relationships)
- **oaseslive.mel_revisions** (2 relationships)
- **oaseslive.monthly_loans_in** (3 relationships)
- **oaseslive.monthly_loans_out** (3 relationships)
- **oaseslive.movement_codes** (1 relationships)
- **oaseslive.n_s_extended_part_descriptions** (1 relationships)
- **oaseslive.netline_import_index** (1 relationships)
- **oaseslive.no_narrative_default** (1 relationships)
- **oaseslive.non_stock_parts** (4 relationships)
- **oaseslive.non_stock_parts_bkp_oases382** (2 relationships)
- **oaseslive.nrc_access_panels** (2 relationships)
- **oaseslive.nrc_defect_details** (3 relationships)
- **oaseslive.nrc_defect_notes** (2 relationships)
- **oaseslive.nrc_documents** (4 relationships)
- **oaseslive.nrc_high_sequence_control** (14 relationships)
- **oaseslive.nrc_materials** (2 relationships)
- **oaseslive.nrc_print_history** (4 relationships)
- **oaseslive.nrc_properties** (1 relationships)
- **oaseslive.nrc_rectification_notes** (2 relationships)
- **oaseslive.nrc_requirements_actions** (28 relationships)
- **oaseslive.nrc_status_history** (5 relationships)
- **oaseslive.nrc_tools** (2 relationships)
- **oaseslive.nrc_workcard_narrative** (1 relationships)
- **oaseslive.nrc_xref_to_scheduled_workcard** (3 relationships)
- **oaseslive.oases_message_log** (1 relationships)
- **oaseslive.oases_reports** (1 relationships)
- **oaseslive.oeim_credit_warranty** (6 relationships)
- **oaseslive.oeim_invoice_cards** (3 relationships)
- **oaseslive.oeim_invoice_fixed_charges** (2 relationships)
- **oaseslive.oeim_invoice_inclusive_hrs** (3 relationships)
- **oaseslive.oeim_invoice_materials** (8 relationships)
- **oaseslive.oeim_invoice_packages** (3 relationships)
- **oaseslive.oeim_invoice_snap_con_rates** (3 relationships)
- **oaseslive.oeim_invoice_snap_cost_codes** (2 relationships)
- **oaseslive.oeim_invoice_snap_currencies** (2 relationships)
- **oaseslive.oeim_invoice_snap_departments** (3 relationships)
- **oaseslive.oeim_invoice_snap_employees** (2 relationships)
- **oaseslive.oeim_invoice_snap_part_master** (2 relationships)
- **oaseslive.oeim_invoice_snap_pay_types** (2 relationships)
- **oaseslive.oeim_invoice_snap_pm_bkup** (2 relationships)
- **oaseslive.oeim_invoice_snap_serl_master** (4 relationships)
- **oaseslive.oeim_invoice_snap_sfdc_book** (5 relationships)
- **oaseslive.oeim_invoice_snap_time_cats** (2 relationships)
- **oaseslive.oeim_invoice_snap_vat_codes** (3 relationships)
- **oaseslive.oeim_invoice_warranty** (8 relationships)
- **oaseslive.oeim_invoice_warranty_refunds** (7 relationships)
- **oaseslive.oeim_invoice_works_orders** (2 relationships)
- **oaseslive.oeim_quote_dismissed** (4 relationships)
- **oaseslive.oeim_transaction_log_details** (2 relationships)
- **oaseslive.oeim_transaction_log_header** (1 relationships)
- **oaseslive.ord_po_unit_conv_delta1827** (1 relationships)
- **oaseslive.order_change_history** (3 relationships)
- **oaseslive.order_customs_info** (1 relationships)
- **oaseslive.order_delivery_note_remarks** (1 relationships)
- **oaseslive.order_email_chasing** (1 relationships)
- **oaseslive.order_goods_received** (3 relationships)
- **oaseslive.order_goods_received_invoices** (4 relationships)
- **oaseslive.order_header_1** (5 relationships)
- **oaseslive.order_header_2** (2 relationships)
- **oaseslive.order_header_3** (2 relationships)
- **oaseslive.order_header_4** (2 relationships)
- **oaseslive.order_history** (7 relationships)
- **oaseslive.order_line_additional_info** (5 relationships)
- **oaseslive.order_line_additional_info_2** (1 relationships)
- **oaseslive.order_line_notes** (1 relationships)
- **oaseslive.order_line_quotes_data** (3 relationships)
- **oaseslive.order_line_requirement_xref** (2 relationships)
- **oaseslive.order_line_weight_dimension** (3 relationships)
- **oaseslive.order_lines** (5 relationships)
- **oaseslive.order_numbers_by_supplier** (2 relationships)
- **oaseslive.order_print_date** (1 relationships)
- **oaseslive.order_purchase_unit_conversion** (1 relationships)
- **oaseslive.order_requirement_allocation** (3 relationships)
- **oaseslive.order_standard_text_blocks** (1 relationships)
- **oaseslive.order_supplier_approval** (2 relationships)
- **oaseslive.order_text** (1 relationships)
- **oaseslive.order_workshop_works_orders** (1 relationships)
- **oaseslive.orders_by_due_date** (1 relationships)
- **oaseslive.orders_to_part_number_xref** (2 relationships)
- **oaseslive.ordr_goods_bkp** (3 relationships)
- **oaseslive.original_purchase_values** (3 relationships)
- **oaseslive.osys_defect_act_to_defect_id** (1 relationships)
- **oaseslive.osys_defect_to_defect_id** (2 relationships)
- **oaseslive.osys_defect_to_tech_log_line** (1 relationships)
- **oaseslive.osys_key_to_reportid** (10 relationships)
- **oaseslive.outstation_codes** (2 relationships)
- **oaseslive.package** (2 relationships)
- **oaseslive.package_items** (5 relationships)
- **oaseslive.paragraph_cancels** (18 relationships)
- **oaseslive.part_applicability_codes** (1 relationships)
- **oaseslive.part_change_warning_chapters** (1 relationships)
- **oaseslive.part_change_warnings** (1 relationships)
- **oaseslive.part_customs_tariff_territory** (2 relationships)
- **oaseslive.part_master** (2 relationships)
- **oaseslive.part_master_bkp_oases382** (2 relationships)
- **oaseslive.part_number_amendment_history** (2 relationships)
- **oaseslive.part_number_chapters** (1 relationships)
- **oaseslive.part_number_chapters_dj-82** (1 relationships)
- **oaseslive.part_number_essentiality_codes** (3 relationships)
- **oaseslive.part_number_marketing_codes** (2 relationships)
- **oaseslive.part_number_order_retention** (1 relationships)
- **oaseslive.part_number_owner_float_levels** (1 relationships)
- **oaseslive.part_number_properties** (1 relationships)
- **oaseslive.part_number_properties_serials** (2 relationships)
- **oaseslive.part_number_shelf_life_details** (2 relationships)
- **oaseslive.part_number_technical_notes** (1 relationships)
- **oaseslive.part_number_vat_codes** (2 relationships)
- **oaseslive.part_serial_documents** (5 relationships)
- **oaseslive.part_serial_master_list** (1 relationships)
- **oaseslive.part_xref_to_pick_history** (3 relationships)
- **oaseslive.parts_customs_tariff_codes** (2 relationships)
- **oaseslive.parts_freight_tiered_markups** (1 relationships)
- **oaseslive.parts_received_without_cost** (2 relationships)
- **oaseslive.parts_requiring_export_licence** (1 relationships)
- **oaseslive.payment_types** (3 relationships)
- **oaseslive.pdc_import_index** (1 relationships)
- **oaseslive.pick_hist_7890_bkp** (6 relationships)
- **oaseslive.pick_history** (6 relationships)
- **oaseslive.pirep_index_data** (1 relationships)
- **oaseslive.planners_notes** (4 relationships)
- **oaseslive.planners_notes_categories** (1 relationships)
- **oaseslive.planners_notes_statuses** (1 relationships)
- **oaseslive.planners_notes_xref** (10 relationships)
- **oaseslive.prefered_bins** (1 relationships)
- **oaseslive.preferred_suppliers_by_part** (2 relationships)
- **oaseslive.preorder_line_requirement_xref** (9 relationships)
- **oaseslive.preorder_line_stock_info** (5 relationships)
- **oaseslive.preorder_lines** (6 relationships)
- **oaseslive.preorders** (5 relationships)
- **oaseslive.price_codes** (2 relationships)
- **oaseslive.price_types** (4 relationships)
- **oaseslive.purchase_demand_by_part** (1 relationships)
- **oaseslive.quote_email_chasing** (1 relationships)
- **oaseslive.quotes_by_part** (3 relationships)
- **oaseslive.quotes_for_part_by_account** (2 relationships)
- **oaseslive.random_stock_check_bins** (6 relationships)
- **oaseslive.random_stock_check_date** (1 relationships)
- **oaseslive.random_stock_check_log** (1 relationships)
- **oaseslive.random_stock_check_parts** (2 relationships)
- **oaseslive.rd_xref_to_tech_logs** (4 relationships)
- **oaseslive.rdi_history** (3 relationships)
- **oaseslive.rdi_to_nrc** (2 relationships)
- **oaseslive.release_codes** (6 relationships)
- **oaseslive.reliability_report_logo_desc** (3 relationships)
- **oaseslive.removals** (2 relationships)
- **oaseslive.repair_approval_data** (3 relationships)
- **oaseslive.repetitive_defect_header_1** (2 relationships)
- **oaseslive.repetitive_defect_narrative** (2 relationships)
- **oaseslive.repetitive_defect_tech_logs** (2 relationships)
- **oaseslive.req_priority_desc_oases_1228** (6 relationships)
- **oaseslive.requests_for_quotes** (1 relationships)
- **oaseslive.requests_for_quotes_lines** (4 relationships)
- **oaseslive.requests_for_quotes_notes** (1 relationships)
- **oaseslive.requirement_planners_notes** (1 relationships)
- **oaseslive.requirement_priority_codes** (1 relationships)
- **oaseslive.requirement_priority_desc** (1 relationships)
- **oaseslive.requirement_priority_leadtimes** (1 relationships)
- **oaseslive.requirement_priority_sla** (2 relationships)
- **oaseslive.requirement_recharge_details** (5 relationships)
- **oaseslive.requirement_source_codes** (1 relationships)
- **oaseslive.requirement_to_rfq_xref** (15 relationships)
- **oaseslive.requirements** (8 relationships)
- **oaseslive.rfc_accomplishment** (1 relationships)
- **oaseslive.rfc_aircraft** (5 relationships)
- **oaseslive.rfc_change_origin** (5 relationships)
- **oaseslive.rfc_components** (6 relationships)
- **oaseslive.rfc_documents** (4 relationships)
- **oaseslive.rfc_download_effectivity** (2 relationships)
- **oaseslive.rfc_download_origin_codes** (3 relationships)
- **oaseslive.rfc_download_taxonomy** (4 relationships)
- **oaseslive.rfc_effectivity_ata** (1 relationships)
- **oaseslive.rfc_effectivity_fleet** (1 relationships)
- **oaseslive.rfc_effectivity_part** (2 relationships)
- **oaseslive.rfc_evaluation_history** (3 relationships)
- **oaseslive.rfc_evaluation_stages** (1 relationships)
- **oaseslive.rfc_frequency_phase_header** (16 relationships)
- **oaseslive.rfc_frequency_phase_limits** (4 relationships)
- **oaseslive.rfc_frequency_phases** (4 relationships)
- **oaseslive.rfc_header** (5 relationships)
- **oaseslive.rfc_header_publications** (2 relationships)
- **oaseslive.rfc_na_notes** (2 relationships)
- **oaseslive.rfc_paragraphs** (2 relationships)
- **oaseslive.rfc_policies** (1 relationships)
- **oaseslive.rfc_print_history_log** (2 relationships)
- **oaseslive.rfc_publications** (1 relationships)
- **oaseslive.rfc_regulating_authority** (6 relationships)
- **oaseslive.rfc_relationships** (1 relationships)
- **oaseslive.rfc_statement_sections** (2 relationships)
- **oaseslive.rfc_status** (3 relationships)
- **oaseslive.rfc_transaction_log** (2 relationships)
- **oaseslive.rfq_by_part_number** (2 relationships)
- **oaseslive.rfq_history** (5 relationships)
- **oaseslive.rfq_quote_received** (3 relationships)
- **oaseslive.rfq_quote_received_notes** (2 relationships)
- **oaseslive.rfq_requirement_xref** (2 relationships)
- **oaseslive.rfq_supplier_details** (2 relationships)
- **oaseslive.rfq_supplier_notes** (2 relationships)
- **oaseslive.rfq_to_order_xref** (3 relationships)
- **oaseslive.rotable_batch_locations** (7 relationships)
- **oaseslive.rotable_float_values** (1 relationships)
- **oaseslive.rotable_history** (9 relationships)
- **oaseslive.rotables_below_re_order** (1 relationships)
- **oaseslive.rp_base_plan_header** (6 relationships)
- **oaseslive.rp_basic_shift** (11 relationships)
- **oaseslive.rp_block_resource** (4 relationships)
- **oaseslive.rp_block_resource_days** (3 relationships)
- **oaseslive.rp_dependencies** (4 relationships)
- **oaseslive.rp_employee_allocation** (4 relationships)
- **oaseslive.rp_employee_allocation_header** (5 relationships)
- **oaseslive.rp_employee_calendar_addition** (5 relationships)
- **oaseslive.rp_employee_calendar_pattern** (3 relationships)
- **oaseslive.rp_milestone_history** (8 relationships)
- **oaseslive.rp_milestones** (2 relationships)
- **oaseslive.rp_shift_pattern** (4 relationships)
- **oaseslive.rp_shift_pattern_header** (1 relationships)
- **oaseslive.rp_weekends** (2 relationships)
- **oaseslive.rp_wo_base_estimated_defects** (2 relationships)
- **oaseslive.rp_wo_base_milestones** (2 relationships)
- **oaseslive.rp_wo_base_nrc_plan** (3 relationships)
- **oaseslive.rp_wo_base_workcard_plan** (3 relationships)
- **oaseslive.rp_wo_estimated_defects** (1 relationships)
- **oaseslive.rp_wo_milestones** (1 relationships)
- **oaseslive.rp_wo_nrc_plan** (2 relationships)
- **oaseslive.rp_wo_workcard_plan** (2 relationships)
- **oaseslive.sabre_flight_map** (1 relationships)
- **oaseslive.sabre_trace** (1 relationships)
- **oaseslive.sage_order_line_details** (1 relationships)
- **oaseslive.sales_history** (7 relationships)
- **oaseslive.sales_invoice_genled_xref** (1 relationships)
- **oaseslive.sales_invoices_xref** (2 relationships)
- **oaseslive.sales_notes_for_part** (1 relationships)
- **oaseslive.sales_order_dispatches** (7 relationships)
- **oaseslive.sales_order_history** (1 relationships)
- **oaseslive.sales_order_lines** (3 relationships)
- **oaseslive.sales_order_notes** (1 relationships)
- **oaseslive.sales_order_parameters** (1 relationships)
- **oaseslive.sales_order_payments** (3 relationships)
- **oaseslive.sales_orders** (4 relationships)
- **oaseslive.sales_orders_by_part** (2 relationships)
- **oaseslive.sales_prices** (5 relationships)
- **oaseslive.sales_quotes_out_history** (5 relationships)
- **oaseslive.sales_request_quote_detail** (13 relationships)
- **oaseslive.sales_request_quote_header** (5 relationships)
- **oaseslive.sales_request_quote_notes** (1 relationships)
- **oaseslive.sales_requested_unknown_parts** (2 relationships)
- **oaseslive.sales_requests_by_part** (2 relationships)
- **oaseslive.sales_requests_by_unknown_part** (2 relationships)
- **oaseslive.sample_fleets** (2 relationships)
- **oaseslive.sample_fleets_jn** (2 relationships)
- **oaseslive.sap_order_header** (2 relationships)
- **oaseslive.sap_order_line** (2 relationships)
- **oaseslive.schedule_forecast_xref** (9 relationships)
- **oaseslive.schedule_source** (4 relationships)
- **oaseslive.scope_type_rating** (4 relationships)
- **oaseslive.sectors** (1 relationships)
- **oaseslive.security_audit_log_header** (4 relationships)
- **oaseslive.security_audit_log_meta_data** (2 relationships)
- **oaseslive.security_group_perm_attribute** (7 relationships)
- **oaseslive.security_group_permissions** (2 relationships)
- **oaseslive.security_group_policies** (2 relationships)
- **oaseslive.security_groups** (1 relationships)
- **oaseslive.security_permission_def_attrib** (2 relationships)
- **oaseslive.security_policy** (8 relationships)
- **oaseslive.security_policy_perm_attribute** (3 relationships)
- **oaseslive.security_policy_permissions** (2 relationships)
- **oaseslive.security_user_effectivity** (2 relationships)
- **oaseslive.security_user_groups** (1 relationships)
- **oaseslive.security_user_notifications** (3 relationships)
- **oaseslive.security_user_perm_attribute** (2 relationships)
- **oaseslive.security_user_permissions** (1 relationships)
- **oaseslive.security_user_permissions_bkp** (1 relationships)
- **oaseslive.security_user_policies** (1 relationships)
- **oaseslive.serial_numbers_by_part** (2 relationships)
- **oaseslive.sfdc_activity** (4 relationships)
- **oaseslive.sfdc_bookings** (4 relationships)
- **oaseslive.sfdc_component_changes** (3 relationships)
- **oaseslive.sfdc_deleted_bookings** (4 relationships)
- **oaseslive.sfdc_open_bookings** (3 relationships)
- **oaseslive.shelf_li_dt_bkp_2020** (5 relationships)
- **oaseslive.shelf_life_dates** (8 relationships)
- **oaseslive.shelf_life_dates_oases6834** (5 relationships)
- **oaseslive.shelf_life_expiry_req_codes** (1 relationships)
- **oaseslive.shipment** (9 relationships)
- **oaseslive.shipment_demands** (7 relationships)
- **oaseslive.shipment_documents** (3 relationships)
- **oaseslive.shipment_item** (8 relationships)
- **oaseslive.shipment_item_customs** (3 relationships)
- **oaseslive.shipment_item_demands** (2 relationships)
- **oaseslive.shipment_order_demands** (3 relationships)
- **oaseslive.shipment_requirement_demands** (3 relationships)
- **oaseslive.shipment_status** (4 relationships)
- **oaseslive.shipment_status_type** (2 relationships)
- **oaseslive.shipment_stocktransfer_demands** (1 relationships)
- **oaseslive.shipment_works_orders_demands** (1 relationships)
- **oaseslive.short_long_serials** (2 relationships)
- **oaseslive.skill_codes** (2 relationships)
- **oaseslive.sold_hours_history** (1 relationships)
- **oaseslive.stock_audit_batches** (6 relationships)
- **oaseslive.stock_audit_bins** (2 relationships)
- **oaseslive.stock_audits** (2 relationships)
- **oaseslive.stock_by_bin** (2 relationships)
- **oaseslive.stock_documents** (4 relationships)
- **oaseslive.stock_group_additional_data** (1 relationships)
- **oaseslive.stock_groups** (1 relationships)
- **oaseslive.stock_groups_bkp_oases382** (1 relationships)
- **oaseslive.stock_works_order_markups** (1 relationships)
- **oaseslive.strip_documents** (4 relationships)
- **oaseslive.strip_report_findings_text** (8 relationships)
- **oaseslive.strip_report_header_1** (6 relationships)
- **oaseslive.strip_report_header_2** (1 relationships)
- **oaseslive.strip_report_modification_text** (1 relationships)
- **oaseslive.structural_damage** (2 relationships)
- **oaseslive.sub_fleet_header** (2 relationships)
- **oaseslive.sub_fleets** (15 relationships)
- **oaseslive.sub_fleets_jn** (2 relationships)
- **oaseslive.supplier_loan_contract_rates** (1 relationships)
- **oaseslive.system_header_icarus** (1 relationships)
- **oaseslive.talend_jobs** (2 relationships)
- **oaseslive.task_activity_link** (6 relationships)
- **oaseslive.taskcard_wo_order_line** (1 relationships)
- **oaseslive.tech_log_1** (1 relationships)
- **oaseslive.tech_log_2** (3 relationships)
- **oaseslive.tech_log_3** (6 relationships)
- **oaseslive.tech_log_defect_text** (1 relationships)
- **oaseslive.tech_log_documents** (2 relationships)
- **oaseslive.tech_log_nrc_xref** (1 relationships)
- **oaseslive.tech_log_rectification_text** (2 relationships)
- **oaseslive.tech_log_workcard_link** (2 relationships)
- **oaseslive.temp_rfc_paragraphs** (2 relationships)
- **oaseslive.test_table** (1 relationships)
- **oaseslive.third_party_account_id** (2 relationships)
- **oaseslive.tiered_markup_range** (1 relationships)
- **oaseslive.time_categories** (2 relationships)
- **oaseslive.tool_check_out_in** (3 relationships)
- **oaseslive.units_of_measure** (6 relationships)

---

## Highly Connected Tables

Tables with the most relationships (central entities):

| Rank | Table | Total Relationships | Incoming | Outgoing |
|------|-------|---------------------|----------|----------|
| 1 | `oaseslive.PART_NUMBER_CHAPTERS_DJ-82` | 154 | 153 | 1 |
| 2 | `oaseslive.aircraft_assembles` | 112 | 111 | 1 |
| 3 | `oaseslive.amp_access_panels_by_workcard` | 85 | 82 | 3 |
| 4 | `oaseslive.completion_part_serial` | 78 | 76 | 2 |
| 5 | `oaseslive.amp_revisions` | 69 | 66 | 3 |
| 6 | `oaseslive.access_dim_accounts_info` | 65 | 61 | 4 |
| 7 | `oaseslive.batch_orders` | 63 | 61 | 2 |
| 8 | `oaseslive.batch_file_header` | 46 | 46 | 0 |
| 9 | `oaseslive.invoice_categories` | 37 | 37 | 0 |
| 10 | `oaseslive.fleet_forecast_plans_rfc` | 34 | 32 | 2 |
| 11 | `oaseslive.currency_codes` | 32 | 31 | 1 |
| 12 | `oaseslive.accomplishment_history` | 31 | 19 | 12 |
| 13 | `oaseslive.amp_package_notes` | 31 | 29 | 2 |
| 14 | `oaseslive.amp_datmig_fleet_visit_pack` | 30 | 30 | 0 |
| 15 | `oaseslive.nrc_requirements_actions` | 28 | 25 | 3 |
| 16 | `oaseslive.amp_report_documents` | 27 | 25 | 2 |
| 17 | `oaseslive.life_code_levels` | 27 | 24 | 3 |
| 18 | `oaseslive.defect_extensions` | 26 | 24 | 2 |
| 19 | `oaseslive.maint_cost_budget_adsb` | 26 | 17 | 9 |
| 20 | `oaseslive.defect_stage_employees` | 25 | 21 | 4 |

---

## Detailed Relationships

Complete list of all table relationships:

### oaseslive.PART_NUMBER_CHAPTERS_DJ-82

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

**Referenced By (Incoming):**

- `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number` → `part_number`
- `oaseslive.accomp_bkup.PART_NUMBER` → `part_number`
- `oaseslive.accomp_hist_delta_1763.PART_NUMBER` → `part_number`
- `oaseslive.accomp_hist_lost_sched.PART_NUMBER` → `part_number`
- `oaseslive.accomplishment_history.PART_NUMBER` → `part_number`
- `oaseslive.accum_cycles_static_data.PART_NUMBER` → `part_number`
- `oaseslive.aircraft_build.part_number` → `part_number`
- `oaseslive.aircraft_leased_apu.part_number` → `part_number`
- `oaseslive.aircraft_leased_engines.part_number` → `part_number`
- `oaseslive.aircraft_leased_landing_gear.part_number` → `part_number`
- `oaseslive.aircraft_leased_propellers.part_number` → `part_number`
- `oaseslive.aircraft_major_checks.PART_NUMBER` → `part_number`
- `oaseslive.alternate_parts.PART_NUMBER` → `part_number`
- `oaseslive.amp_component_intervals.part_number` → `part_number`
- `oaseslive.amp_datmig_accomplishments.PART_NUMBER` → `part_number`
- `oaseslive.amp_datmig_llp.PART_NUMBER` → `part_number`
- `oaseslive.amp_material_effectivity.PART_NUMBER` → `part_number`
- `oaseslive.amp_material_effectivity_jn.PART_NUMBER` → `part_number`
- `oaseslive.batch_notes.PART_NUMBER` → `part_number`
- `oaseslive.batch_notes_gu4240.PART_NUMBER` → `part_number`
- `oaseslive.batch_record_1.part_number` → `part_number`
- `oaseslive.batch_record_1_gu4240.PART_NUMBER` → `part_number`
- `oaseslive.completion_life_values.PART_NUMBER` → `part_number`
- `oaseslive.completion_part_serial.PART_NUMBER` → `part_number`
- `oaseslive.component_life.part_number` → `part_number`
- `oaseslive.component_mods_history_by_part.PART_NUMBER` → `part_number`
- `oaseslive.component_movement_hist_life.part_number` → `part_number`
- `oaseslive.component_movement_history.PART_NUMBER` → `part_number`
- `oaseslive.component_movement_history_ext.part_number` → `part_number`
- `oaseslive.component_movt_hist_ext_8661.PART_NUMBER` → `part_number`
- `oaseslive.components.part_number` → `part_number`
- `oaseslive.components_bkp_dj95.PART_NUMBER` → `part_number`
- `oaseslive.components_bkp_dj97.PART_NUMBER` → `part_number`
- `oaseslive.components_oases971.PART_NUMBER` → `part_number`
- `oaseslive.condition_pick_table.PART_NUMBER` → `part_number`
- `oaseslive.consumable_batch_locations.part_number` → `part_number`
- `oaseslive.consumable_history.part_number` → `part_number`
- `oaseslive.consumable_repair_xref_to_part.PART_NUMBER` → `part_number`
- `oaseslive.consumables_below_re_order.part_number` → `part_number`
- `oaseslive.cq_quote_materials.part_number` → `part_number`
- `oaseslive.credit_works_order_cards.part_number` → `part_number`
- `oaseslive.daily_loans_out.PART_NUMBER` → `part_number`
- `oaseslive.delivery_note_item_header_1.part_number` → `part_number`
- `oaseslive.dmg_rpr_damage.PART_NUMBER` → `part_number`
- `oaseslive.dmg_rpr_fitted_locations.PART_NUMBER` → `part_number`
- `oaseslive.drn_component_mods_history.PART_NUMBER` → `part_number`
- `oaseslive.drn_components_nsbl_history.PART_NUMBER` → `part_number`
- `oaseslive.drn_life_limits.PART_NUMBER` → `part_number`
- `oaseslive.drn_part_serial.PART_NUMBER` → `part_number`
- `oaseslive.dues_register.part_number` → `part_number`
- `oaseslive.dummy_part_numbers.PART_NUMBER` → `part_number`
- `oaseslive.extended_part_descriptions.PART_NUMBER` → `part_number`
- `oaseslive.fleet_chap_part_header_1.PART_NUMBER` → `part_number`
- `oaseslive.fleet_chap_part_header_2.PART_NUMBER` → `part_number`
- `oaseslive.fleet_chap_part_header_3.PART_NUMBER` → `part_number`
- `oaseslive.fleet_chapter_part_aircraft.PART_NUMBER` → `part_number`
- `oaseslive.fleet_forecast_plans_drn.PART_NUMBER` → `part_number`
- `oaseslive.float_history.PART_NUMBER` → `part_number`
- `oaseslive.hazardous_materials.PART_NUMBER` → `part_number`
- `oaseslive.ie96_historic.PART_NUMBER` → `part_number`
- `oaseslive.inherited_acquisition_costs.PART_NUMBER` → `part_number`
- `oaseslive.invoice_trail_entries.PART_NUMBER` → `part_number`
- `oaseslive.latest_repair_values.PART_NUMBER` → `part_number`
- `oaseslive.loaned_units.part_number` → `part_number`
- `oaseslive.long_serial_number_xref.part_number` → `part_number`
- `oaseslive.maint_cost_budget_materials.PART_NUMBER` → `part_number`
- `oaseslive.maint_material_costs.PART_NUMBER` → `part_number`
- `oaseslive.maintenance_cat_incl_parts.PART_NUMBER` → `part_number`
- `oaseslive.material_pool_agreement_pn.PART_NUMBER` → `part_number`
- `oaseslive.maximum_preload_pick_quantity.PART_NUMBER` → `part_number`
- `oaseslive.monthly_loans_in.PART_NUMBER` → `part_number`
- `oaseslive.monthly_loans_out.PART_NUMBER` → `part_number`
- `oaseslive.n_s_extended_part_descriptions.PART_NUMBER` → `part_number`
- `oaseslive.non_stock_parts.part_number` → `part_number`
- `oaseslive.non_stock_parts_bkp_oases382.PART_NUMBER` → `part_number`
- `oaseslive.nrc_materials.part_number` → `part_number`
- `oaseslive.oeim_credit_warranty.part_number` → `part_number`
- `oaseslive.oeim_invoice_materials.part_number` → `part_number`
- `oaseslive.oeim_invoice_snap_part_master.PART_NUMBER` → `part_number`
- `oaseslive.oeim_invoice_snap_pm_bkup.PART_NUMBER` → `part_number`
- `oaseslive.oeim_invoice_snap_serl_master.PART_NUMBER` → `part_number`
- `oaseslive.oeim_invoice_warranty.part_number` → `part_number`
- `oaseslive.oeim_invoice_warranty_refunds.part_number` → `part_number`
- `oaseslive.oeim_quote_dismissed.PART_NUMBER` → `part_number`
- `oaseslive.order_goods_received.part_number` → `part_number`
- `oaseslive.order_history.PART_NUMBER` → `part_number`
- `oaseslive.orders_to_part_number_xref.PART_NUMBER` → `part_number`
- `oaseslive.ordr_goods_bkp.PART_NUMBER` → `part_number`
- `oaseslive.original_purchase_values.part_number` → `part_number`
- `oaseslive.part_change_warning_chapters.PART_NUMBER` → `part_number`
- `oaseslive.part_change_warnings.PART_NUMBER` → `part_number`
- `oaseslive.part_customs_tariff_territory.PART_NUMBER` → `part_number`
- `oaseslive.part_master.part_number` → `part_number`
- `oaseslive.part_master_bkp_oases382.PART_NUMBER` → `part_number`
- `oaseslive.part_number_amendment_history.PART_NUMBER` → `part_number`
- `oaseslive.part_number_chapters.PART_NUMBER` → `part_number`
- `oaseslive.part_number_chapters_dj-82.PART_NUMBER` → `part_number`
- `oaseslive.part_number_essentiality_codes.PART_NUMBER` → `part_number`
- `oaseslive.part_number_marketing_codes.PART_NUMBER` → `part_number`
- `oaseslive.part_number_order_retention.PART_NUMBER` → `part_number`
- `oaseslive.part_number_owner_float_levels.part_number` → `part_number`
- `oaseslive.part_number_properties.part_number` → `part_number`
- `oaseslive.part_number_properties_serials.part_number` → `part_number`
- `oaseslive.part_number_shelf_life_details.PART_NUMBER` → `part_number`
- `oaseslive.part_number_technical_notes.PART_NUMBER` → `part_number`
- `oaseslive.part_number_vat_codes.PART_NUMBER` → `part_number`
- `oaseslive.part_serial_documents.PART_NUMBER` → `part_number`
- `oaseslive.part_serial_master_list.PART_NUMBER` → `part_number`
- `oaseslive.part_xref_to_pick_history.PART_NUMBER` → `part_number`
- `oaseslive.parts_customs_tariff_codes.PART_NUMBER` → `part_number`
- `oaseslive.parts_received_without_cost.PART_NUMBER` → `part_number`
- `oaseslive.parts_requiring_export_licence.PART_NUMBER` → `part_number`
- `oaseslive.planners_notes_xref.PART_NUMBER` → `part_number`
- `oaseslive.prefered_bins.part_number` → `part_number`
- `oaseslive.preferred_suppliers_by_part.part_number` → `part_number`
- `oaseslive.preorder_lines.PART_NUMBER` → `part_number`
- `oaseslive.purchase_demand_by_part.PART_NUMBER` → `part_number`
- `oaseslive.quotes_by_part.PART_NUMBER` → `part_number`
- `oaseslive.quotes_for_part_by_account.PART_NUMBER` → `part_number`
- `oaseslive.random_stock_check_parts.PART_NUMBER` → `part_number`
- `oaseslive.removals.part_number` → `part_number`
- `oaseslive.requests_for_quotes_lines.PART_NUMBER` → `part_number`
- `oaseslive.requirements.part_number` → `part_number`
- `oaseslive.rfc_components.part_number` → `part_number`
- `oaseslive.rfc_download_effectivity.PART_NUMBER` → `part_number`
- `oaseslive.rfc_effectivity_part.part_number` → `part_number`
- `oaseslive.rfq_by_part_number.PART_NUMBER` → `part_number`
- `oaseslive.rfq_history.part_number` → `part_number`
- `oaseslive.rotable_batch_locations.part_number` → `part_number`
- `oaseslive.rotable_float_values.PART_NUMBER` → `part_number`
- `oaseslive.rotable_history.part_number` → `part_number`
- `oaseslive.rotables_below_re_order.PART_NUMBER` → `part_number`
- `oaseslive.sales_history.part_number` → `part_number`
- `oaseslive.sales_notes_for_part.part_number` → `part_number`
- `oaseslive.sales_orders_by_part.PART_NUMBER` → `part_number`
- `oaseslive.sales_prices.part_number` → `part_number`
- `oaseslive.sales_quotes_out_history.PART_NUMBER` → `part_number`
- `oaseslive.sales_request_quote_detail.part_number` → `part_number`
- `oaseslive.sales_requests_by_part.PART_NUMBER` → `part_number`
- `oaseslive.schedule_forecast_xref.PART_NUMBER` → `part_number`
- `oaseslive.schedule_source.PART_NUMBER` → `part_number`
- `oaseslive.serial_numbers_by_part.PART_NUMBER` → `part_number`
- `oaseslive.shelf_li_dt_bkp_2020.PART_NUMBER` → `part_number`
- `oaseslive.shelf_life_dates.part_number` → `part_number`
- `oaseslive.shelf_life_dates_oases6834.PART_NUMBER` → `part_number`
- `oaseslive.shipment_demands.part_number` → `part_number`
- `oaseslive.shipment_item.PART_NUMBER` → `part_number`
- `oaseslive.short_long_serials.PART_NUMBER` → `part_number`
- `oaseslive.stock_audits.PART_NUMBER` → `part_number`
- `oaseslive.stock_by_bin.PART_NUMBER` → `part_number`
- `oaseslive.strip_report_header_1.PART_NUMBER` → `part_number`
- `oaseslive.task_activity_link.PART_NUMBER` → `part_number`
- `oaseslive.units_of_measure.part_number` → `part_number`

### oaseslive.access_dim_accounts_info

**References (Outgoing):**

- `INFO_ID` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `ACCOUNT_ID` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `VAT_CODE` → `oaseslive.amp_workcard_activations.workcard_activation_id`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

**Referenced By (Incoming):**

- `oaseslive.access_dim_accounts_info.INFO_ID` → `INFO_ID`
- `oaseslive.access_dim_accounts_info.ACCOUNT_ID` → `INFO_ID`
- `oaseslive.access_dim_sales_info.INFO_ID` → `INFO_ID`
- `oaseslive.account_amendment_history.account_code` → `INFO_ID`
- `oaseslive.account_ata_spec_2000_xref.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.account_available_warehouses.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.account_buying_contacts.account_code` → `INFO_ID`
- `oaseslive.account_header_1.account_code` → `INFO_ID`
- `oaseslive.account_header_2.account_code` → `INFO_ID`
- `oaseslive.account_location_email_address.account_code` → `INFO_ID`
- `oaseslive.account_location_header_1.account_code` → `INFO_ID`
- `oaseslive.account_location_header_2.account_code` → `INFO_ID`
- `oaseslive.account_location_header_3.account_code` → `INFO_ID`
- `oaseslive.account_location_header_4.account_code` → `INFO_ID`
- `oaseslive.account_location_header_5.account_code` → `INFO_ID`
- `oaseslive.account_location_header_6.account_code` → `INFO_ID`
- `oaseslive.account_location_header_6.account_id` → `INFO_ID`
- `oaseslive.account_location_header_7.account_code` → `INFO_ID`
- `oaseslive.account_location_header_8.account_code` → `INFO_ID`
- `oaseslive.account_location_header_9.account_code` → `INFO_ID`
- `oaseslive.account_location_notes.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.account_location_properties.account_code` → `INFO_ID`
- `oaseslive.account_supplier_approvals.account_code` → `INFO_ID`
- `oaseslive.airway_bill_references.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.contacts_xref.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.cq_quotes.account_code` → `INFO_ID`
- `oaseslive.credit_works_orders.account_code` → `INFO_ID`
- `oaseslive.customer_contracts.account_code` → `INFO_ID`
- `oaseslive.daily_loans_out.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.delivery_note_header_1.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.delivery_note_header_4.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.ie96_historic.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.invoice_lines.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.invoices.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.loaned_units.account_code` → `INFO_ID`
- `oaseslive.maintenance_cost_quotes.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.oeim_invoice_works_orders.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.order_header_1.account_code` → `INFO_ID`
- `oaseslive.order_numbers_by_supplier.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.preferred_suppliers_by_part.account_code` → `INFO_ID`
- `oaseslive.preorders.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.quotes_by_part.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.quotes_for_part_by_account.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.repair_approval_data.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.requirement_priority_sla.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.rfq_history.account_code` → `INFO_ID`
- `oaseslive.rfq_quote_received.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.rfq_quote_received_notes.account_code` → `INFO_ID`
- `oaseslive.rfq_supplier_details.account_code` → `INFO_ID`
- `oaseslive.rfq_supplier_notes.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.rfq_to_order_xref.account_code` → `INFO_ID`
- `oaseslive.rotable_batch_locations.account_code` → `INFO_ID`
- `oaseslive.rotable_history.account_code` → `INFO_ID`
- `oaseslive.sales_orders.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.sales_prices.account_code` → `INFO_ID`
- `oaseslive.sales_quotes_out_history.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.sales_request_quote_header.ACCOUNT_CODE` → `INFO_ID`
- `oaseslive.shipment_order_demands.account_code` → `INFO_ID`
- `oaseslive.supplier_loan_contract_rates.account_code` → `INFO_ID`
- `oaseslive.third_party_account_id.ACCOUNT_ID` → `INFO_ID`
- `oaseslive.third_party_account_id.ACCOUNT_CODE` → `INFO_ID`

### oaseslive.access_dim_sales_info

**References (Outgoing):**

- `INFO_ID` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `AUDIT_NUMBER` → `oaseslive.amp_audit_notes.FLEET_CODE`
- `VAT_CODE` → `oaseslive.amp_workcard_activations.workcard_activation_id`
- `CUSTOMER_CODE` → `oaseslive.customer_contract_rates.contract_id`
- `SALES_ORDER_NUMBER` → `oaseslive.customer_sales_order_xref.CUSTOMER_SALES_ORDER_NUMBER`

### oaseslive.accomp_bkup

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `ACCOMPLISHMENT_ID` → `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID`
- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `VISIT_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `PACKAGE_CODE` → `oaseslive.amp_package_notes.fleet`
- `REPORT_ID` → `oaseslive.amp_report_documents.FLEET`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `PARAGRAPH_ID` → `oaseslive.paragraph_cancels.RFC_ID`

### oaseslive.accomp_hist_delta_1763

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `ACCOMPLISHMENT_ID` → `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID`
- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `VISIT_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `PACKAGE_CODE` → `oaseslive.amp_package_notes.fleet`
- `REPORT_ID` → `oaseslive.amp_report_documents.FLEET`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `DAMAGE_ID` → `oaseslive.dmg_rpr_damage.DAMAGE_ID`
- `DOCUMENT_IMAGE_ID` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`
- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `PARAGRAPH_ID` → `oaseslive.paragraph_cancels.RFC_ID`

### oaseslive.accomp_hist_lost_sched

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `ACCOMPLISHMENT_ID` → `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID`
- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `VISIT_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `PACKAGE_CODE` → `oaseslive.amp_package_notes.fleet`
- `REPORT_ID` → `oaseslive.amp_report_documents.FLEET`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `PARAGRAPH_ID` → `oaseslive.paragraph_cancels.RFC_ID`

### oaseslive.accomp_hist_lost_sched_val

**References (Outgoing):**

- `ACCOMPLISHMENT_ID` → `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID`
- `LIFE_CODE_LEVEL_ID` → `oaseslive.life_code_levels.life_code_level_id`

### oaseslive.accomp_values_bkup

**References (Outgoing):**

- `ACCOMPLISHMENT_ID` → `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID`
- `LIFE_CODE_LEVEL_ID` → `oaseslive.life_code_levels.life_code_level_id`

### oaseslive.accomplishment_history

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `ACCOMPLISHMENT_ID` → `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID`
- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `VISIT_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `PACKAGE_CODE` → `oaseslive.amp_package_notes.fleet`
- `REPORT_ID` → `oaseslive.amp_report_documents.FLEET`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `DAMAGE_ID` → `oaseslive.dmg_rpr_damage.DAMAGE_ID`
- `DOCUMENT_IMAGE_ID` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`
- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `PARAGRAPH_ID` → `oaseslive.paragraph_cancels.RFC_ID`

**Referenced By (Incoming):**

- `oaseslive.accomp_bkup.ACCOMPLISHMENT_ID` → `ACCOMPLISHMENT_ID`
- `oaseslive.accomp_hist_delta_1763.ACCOMPLISHMENT_ID` → `ACCOMPLISHMENT_ID`
- `oaseslive.accomp_hist_lost_sched.ACCOMPLISHMENT_ID` → `ACCOMPLISHMENT_ID`
- `oaseslive.accomp_hist_lost_sched_val.ACCOMPLISHMENT_ID` → `ACCOMPLISHMENT_ID`
- `oaseslive.accomp_values_bkup.ACCOMPLISHMENT_ID` → `ACCOMPLISHMENT_ID`
- `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID` → `ACCOMPLISHMENT_ID`
- `oaseslive.accomplishment_history_values.ACCOMPLISHMENT_ID` → `ACCOMPLISHMENT_ID`
- `oaseslive.accs_var_corrections_bkp.ACCOMPLISHMENT_ID` → `ACCOMPLISHMENT_ID`
- `oaseslive.amp_revision_history.HISTORY_ID` → `ACCOMPLISHMENT_ID`
- `oaseslive.component_movement_hist_life.history_id` → `ACCOMPLISHMENT_ID`
- `oaseslive.component_movement_history_ext.history_id` → `ACCOMPLISHMENT_ID`
- `oaseslive.component_movt_hist_ext_8661.HISTORY_ID` → `ACCOMPLISHMENT_ID`
- `oaseslive.maint_accomplishment_costs.ACCOMPLISHMENT_ID` → `ACCOMPLISHMENT_ID`
- `oaseslive.mel_revision_history.HISTORY_ID` → `ACCOMPLISHMENT_ID`
- `oaseslive.order_change_history.HISTORY_ID` → `ACCOMPLISHMENT_ID`
- `oaseslive.rfc_accomplishment.accomplishment_code` → `ACCOMPLISHMENT_ID`
- `oaseslive.rfc_download_origin_codes.ACCOMPLISHMENT_CODE` → `ACCOMPLISHMENT_ID`
- `oaseslive.rfc_header.accomplishment_code` → `ACCOMPLISHMENT_ID`
- `oaseslive.rp_milestone_history.HISTORY_ID` → `ACCOMPLISHMENT_ID`

### oaseslive.accomplishment_history_values

**References (Outgoing):**

- `ACCOMPLISHMENT_ID` → `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID`
- `LIFE_CODE_LEVEL_ID` → `oaseslive.life_code_levels.life_code_level_id`

### oaseslive.account_amendment_history

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`

### oaseslive.account_ata_spec_2000_xref

**References (Outgoing):**

- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`

### oaseslive.account_available_warehouses

**References (Outgoing):**

- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `WAREHOUSE_CODE` → `oaseslive.account_available_warehouses.ACCOUNT_CODE`

**Referenced By (Incoming):**

- `oaseslive.account_available_warehouses.WAREHOUSE_CODE` → `ACCOUNT_CODE`
- `oaseslive.bins.warehouse_code` → `ACCOUNT_CODE`
- `oaseslive.condition_pick_table.WAREHOUSE_CODE` → `ACCOUNT_CODE`
- `oaseslive.random_stock_check_bins.WAREHOUSE_CODE` → `ACCOUNT_CODE`
- `oaseslive.random_stock_check_date.WAREHOUSE_CODE` → `ACCOUNT_CODE`
- `oaseslive.random_stock_check_log.WAREHOUSE_CODE` → `ACCOUNT_CODE`
- `oaseslive.random_stock_check_parts.WAREHOUSE_CODE` → `ACCOUNT_CODE`
- `oaseslive.rp_block_resource.WAREHOUSE_CODE` → `ACCOUNT_CODE`
- `oaseslive.rp_employee_calendar_addition.warehouse_code` → `ACCOUNT_CODE`
- `oaseslive.rp_employee_calendar_pattern.warehouse_code` → `ACCOUNT_CODE`

### oaseslive.account_buying_contacts

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `mobile_number` → `oaseslive.bkp_mobile_permissions.OASES_SECURITY_TOKEN`

### oaseslive.account_header_1

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`

### oaseslive.account_header_2

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`

### oaseslive.account_location_email_address

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`

### oaseslive.account_location_header_1

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`

### oaseslive.account_location_header_2

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`

### oaseslive.account_location_header_3

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`

### oaseslive.account_location_header_4

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`

### oaseslive.account_location_header_5

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `currency_code` → `oaseslive.currency_codes.currency_code`

### oaseslive.account_location_header_6

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `account_id` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `state_code` → `oaseslive.release_to_service_statement.RELEASE_STATEMENT`

### oaseslive.account_location_header_7

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`

### oaseslive.account_location_header_8

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`

### oaseslive.account_location_header_9

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `customer_number` → `oaseslive.customer_contract_rates.contract_id`
- `end_use_number` → `oaseslive.end_use_codes.END_USE_CODE`

### oaseslive.account_location_notes

**References (Outgoing):**

- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`

### oaseslive.account_location_properties

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`

### oaseslive.account_supplier_approvals

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `supplier_approval_number` → `oaseslive.account_supplier_approvals.account_code`

**Referenced By (Incoming):**

- `oaseslive.account_supplier_approvals.supplier_approval_number` → `account_code`
- `oaseslive.consumable_history.approval_code` → `account_code`
- `oaseslive.order_supplier_approval.SUPPLIER_APPROVAL_NUMBER` → `account_code`

### oaseslive.account_system_header

**References (Outgoing):**

- `KEY_ID` → `oaseslive.osys_key_to_reportid.OSYSKEY`

### oaseslive.accounts_references

**Referenced By (Incoming):**

- `oaseslive.customs_status_codes.reference_number` → `accounts_reference`

### oaseslive.accs_var_corrections_bkp

**References (Outgoing):**

- `ACCOMPLISHMENT_ID` → `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID`

### oaseslive.accum_cycles_static_data

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

**Referenced By (Incoming):**

- `oaseslive.drn_cycles.CYCLE_NUMBER` → `PARENT_PART_NUMBER`

### oaseslive.add_extension_permissions

**References (Outgoing):**

- `USER_ID` → `oaseslive.dataset_locks_by_user.USER_ID`

**Referenced By (Incoming):**

- `oaseslive.bkp_mobile_permissions.PERMISSION_ID` → `USER_ID`
- `oaseslive.defect_extensions.EXTENSION_ID` → `USER_ID`
- `oaseslive.extensions.EXTENSION_ID` → `USER_ID`
- `oaseslive.rfc_status.permission_id` → `USER_ID`
- `oaseslive.security_audit_log_header.PERMISSION_ID` → `USER_ID`
- `oaseslive.security_group_perm_attribute.PERMISSION_ID` → `USER_ID`
- `oaseslive.security_group_permissions.PERMISSION_ID` → `USER_ID`
- `oaseslive.security_permission_def_attrib.PERMISSION_ID` → `USER_ID`
- `oaseslive.security_policy_perm_attribute.PERMISSION_ID` → `USER_ID`
- `oaseslive.security_policy_permissions.PERMISSION_ID` → `USER_ID`
- `oaseslive.security_user_perm_attribute.PERMISSION_ID` → `USER_ID`
- `oaseslive.security_user_permissions.PERMISSION_ID` → `USER_ID`
- `oaseslive.security_user_permissions_bkp.PERMISSION_ID` → `USER_ID`

### oaseslive.aircraft_assembles

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`

**Referenced By (Incoming):**

- `oaseslive.accomp_bkup.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.accomp_hist_delta_1763.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.accomp_hist_lost_sched.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.accomplishment_history.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.aircraft_assembles.aircraft_code` → `aircraft_code`
- `oaseslive.aircraft_build.aircraft_code` → `aircraft_code`
- `oaseslive.aircraft_build_chapters.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.aircraft_documents.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.aircraft_exclusions.aircraft_code` → `aircraft_code`
- `oaseslive.aircraft_flight_hours_1.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.aircraft_flight_hours_2.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.aircraft_header_1.aircraft_code` → `aircraft_code`
- `oaseslive.aircraft_header_2.aircraft_code` → `aircraft_code`
- `oaseslive.aircraft_lease_details.aircraft_code` → `aircraft_code`
- `oaseslive.aircraft_leased_apu.aircraft_code` → `aircraft_code`
- `oaseslive.aircraft_leased_engines.aircraft_code` → `aircraft_code`
- `oaseslive.aircraft_leased_landing_gear.aircraft_code` → `aircraft_code`
- `oaseslive.aircraft_leased_propellers.aircraft_code` → `aircraft_code`
- `oaseslive.aircraft_life.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.aircraft_life_dbf1065.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.aircraft_major_checks.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.aircraft_reg_xref.aircraft_code` → `aircraft_code`
- `oaseslive.aircraft_short_reg_xref.aircraft_code` → `aircraft_code`
- `oaseslive.aircraft_subchapter_statistics.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.aircraft_weight.aircraft_code` → `aircraft_code`
- `oaseslive.aircraft_weight_7487bkp.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.aircraft_weight_conf_xref.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.amp_access_panel_effectivity.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.amp_accesspanel_effectivity_jn.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.amp_datmig_accomplishments.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.amp_document_effectivity.aircraft_code` → `aircraft_code`
- `oaseslive.amp_document_effectivity_bk.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.amp_workcard_ac_effectivity.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.amp_workcard_ac_effectivity_jn.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.assemble_thrust_life_code.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.cfd_xref_to_tech_log.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.completion_fleet_ata_pos.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.completion_life_values.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.completion_maint_mod.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.component_movement_history_ext.aircraft_code` → `aircraft_code`
- `oaseslive.component_movt_hist_ext_8661.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.components.aircraft_code` → `aircraft_code`
- `oaseslive.components_bkp_dj95.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.components_bkp_dj97.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.components_oases971.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.cq_quotes.aircraft_code` → `aircraft_code`
- `oaseslive.crs_signature_text.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.customer_contracts.aircraft_code` → `aircraft_code`
- `oaseslive.deferred_defect_xref_to_cfd_no.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.dmg_rpr_damage_numbering.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.dmg_rpr_doc_effectivity.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.dmg_rpr_document_order.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.dmg_rpr_fitted_locations.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.dmg_rpr_location.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.drn_cycles.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.drn_fleet_ata.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.drn_life_limits.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.drn_maint_mod.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.drn_maint_mod_notes.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.drn_maintenance_history.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.drn_maintenance_history_notes.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.drn_mod_desc_order_hist.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.drn_modification_history.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.drn_modification_history_notes.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.fleet_chapter_part_aircraft.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.fleet_forecast_plans.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.flown_sectors.aircraft_code` → `aircraft_code`
- `oaseslive.flown_sectors_bkp.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.flown_sectors_con_680.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.flown_sectors_delta1817.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.forecast_cache.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.forecast_cache_revisions.aircraft_code` → `aircraft_code`
- `oaseslive.future_flights.aircraft_code` → `aircraft_code`
- `oaseslive.le80_defect_temp.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.life_code_entry.aircraft_code` → `aircraft_code`
- `oaseslive.life_code_entry_backup.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.life_code_entry_dbf1065.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.lmc_base_data_options.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.maint_associated_cost_aircraft.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.maint_cost_budget_adsb.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.maint_cost_budget_aircraft.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.maint_cost_budget_cfds.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.maint_cost_budget_defects.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.maint_cost_budget_packages.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.maint_cost_budget_visits.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.maint_cost_budget_workcards.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.material_pool_agreement_ac.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.measurement_alerts_aircraft.aircraft_code` → `aircraft_code`
- `oaseslive.no_narrative_default.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.pirep_index_data.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.planners_notes_xref.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.rd_xref_to_tech_logs.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.removals.aircraft_code` → `aircraft_code`
- `oaseslive.repetitive_defect_header_1.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.rfc_aircraft.aircraft_code` → `aircraft_code`
- `oaseslive.sample_fleets.aircraft_code` → `aircraft_code`
- `oaseslive.sample_fleets_jn.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.schedule_forecast_xref.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.schedule_source.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.security_user_effectivity.aircraft_code` → `aircraft_code`
- `oaseslive.sub_fleets.aircraft_code` → `aircraft_code`
- `oaseslive.sub_fleets_jn.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.task_activity_link.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.tech_log_1.aircraft_code` → `aircraft_code`
- `oaseslive.tech_log_2.aircraft_code` → `aircraft_code`
- `oaseslive.tech_log_3.aircraft_code` → `aircraft_code`
- `oaseslive.tech_log_defect_text.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.tech_log_nrc_xref.aircraft_code` → `aircraft_code`
- `oaseslive.tech_log_rectification_text.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.tech_log_workcard_link.AIRCRAFT_CODE` → `aircraft_code`
- `oaseslive.units_of_measure.aircraft_code` → `aircraft_code`

### oaseslive.aircraft_build

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.aircraft_build_chapters

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.aircraft_documents

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `AIRCRAFT_DOCUMENT_ID` → `oaseslive.aircraft_documents.AIRCRAFT_DOCUMENT_ID`
- `DOCUMENT_IMAGE_ID` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`

**Referenced By (Incoming):**

- `oaseslive.aircraft_documents.AIRCRAFT_DOCUMENT_ID` → `AIRCRAFT_DOCUMENT_ID`
- `oaseslive.amp_document_effectivity.document_id` → `AIRCRAFT_DOCUMENT_ID`
- `oaseslive.amp_document_effectivity_bk.DOCUMENT_ID` → `AIRCRAFT_DOCUMENT_ID`
- `oaseslive.amp_documents_by_workcard.document_id` → `AIRCRAFT_DOCUMENT_ID`
- `oaseslive.amp_documents_by_workcard_bk.DOCUMENT_ID` → `AIRCRAFT_DOCUMENT_ID`
- `oaseslive.amp_manufacturers_documents.DOCUMENT_ID` → `AIRCRAFT_DOCUMENT_ID`
- `oaseslive.document_classes.DOCUMENT_ID` → `AIRCRAFT_DOCUMENT_ID`
- `oaseslive.esign_off_nrc.DOCUMENT_ID` → `AIRCRAFT_DOCUMENT_ID`
- `oaseslive.manufacturers_work_documents.DOCUMENT_ID` → `AIRCRAFT_DOCUMENT_ID`
- `oaseslive.nrc_documents.document_id` → `AIRCRAFT_DOCUMENT_ID`
- `oaseslive.shipment_documents.DOCUMENT_ID` → `AIRCRAFT_DOCUMENT_ID`

### oaseslive.aircraft_exclusions

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `aircraft_exclusion_id` → `oaseslive.aircraft_exclusions.aircraft_exclusion_id`

**Referenced By (Incoming):**

- `oaseslive.aircraft_exclusions.aircraft_exclusion_id` → `aircraft_exclusion_id`

### oaseslive.aircraft_flight_hours_1

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`

**Referenced By (Incoming):**

- `oaseslive.flown_sectors.flight_number` → `AIRCRAFT_CODE`
- `oaseslive.flown_sectors_bkp.FLIGHT_NUMBER` → `AIRCRAFT_CODE`
- `oaseslive.flown_sectors_con_680.FLIGHT_NUMBER` → `AIRCRAFT_CODE`
- `oaseslive.flown_sectors_delta1817.FLIGHT_NUMBER` → `AIRCRAFT_CODE`

### oaseslive.aircraft_flight_hours_2

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.aircraft_header_1

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `line_number` → `oaseslive.invoice_line_notes.INVOICE_NUMBER`

### oaseslive.aircraft_header_2

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `effectivity_code` → `oaseslive.amp_access_panel_effectivity.AP_AC_EFFECTIVITY_ID`

### oaseslive.aircraft_lease_details

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`

**Referenced By (Incoming):**

- `oaseslive.oeim_transaction_log_details.DETAIL_NUMBER` → `aircraft_code`

### oaseslive.aircraft_leased_apu

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.aircraft_leased_engines

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.aircraft_leased_landing_gear

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.aircraft_leased_propellers

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.aircraft_life

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `LIFE_CODE_LEVEL_ID` → `oaseslive.life_code_levels.life_code_level_id`

**Referenced By (Incoming):**

- `oaseslive.assemble_thrust_life_code.LIFE_CODE` → `AIRCRAFT_CODE`
- `oaseslive.life_code_levels.life_code` → `AIRCRAFT_CODE`
- `oaseslive.life_codes.life_code` → `AIRCRAFT_CODE`
- `oaseslive.measurement_alerts_aircraft.life_code` → `AIRCRAFT_CODE`
- `oaseslive.measurement_alerts_fleet.life_code` → `AIRCRAFT_CODE`

### oaseslive.aircraft_life_dbf1065

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `LIFE_CODE_LEVEL_ID` → `oaseslive.life_code_levels.life_code_level_id`

### oaseslive.aircraft_major_checks

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `VISIT_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `PACKAGE_CODE` → `oaseslive.amp_package_notes.fleet`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.aircraft_reg_xref

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.aircraft_short_reg_xref

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.aircraft_statistics

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`

### oaseslive.aircraft_subchapter_statistics

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.aircraft_types

**Referenced By (Incoming):**

- `oaseslive.rp_calendar_addition_type.type_id` → `aircraft_type`
- `oaseslive.rp_dependencies.TYPE_ID` → `aircraft_type`
- `oaseslive.rp_employee_calendar_addition.type_id` → `aircraft_type`

### oaseslive.aircraft_weight

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.aircraft_weight_7487bkp

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.aircraft_weight_conf

**References (Outgoing):**

- `CONF_ID` → `oaseslive.aircraft_weight_conf.CONF_ID`

**Referenced By (Incoming):**

- `oaseslive.aircraft_weight_conf.CONF_ID` → `CONF_ID`
- `oaseslive.aircraft_weight_conf_entries.CONF_ID` → `CONF_ID`
- `oaseslive.aircraft_weight_conf_xref.CONF_ID` → `CONF_ID`

### oaseslive.aircraft_weight_conf_entries

**References (Outgoing):**

- `CONF_ID` → `oaseslive.aircraft_weight_conf.CONF_ID`

### oaseslive.aircraft_weight_conf_xref

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `CONF_ID` → `oaseslive.aircraft_weight_conf.CONF_ID`

### oaseslive.airway_bill_references

**References (Outgoing):**

- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `DELIVERY_NOTE_NUMBER` → `oaseslive.delivery_note_extended_remarks.DELIVERY_NOTE_NUMBER`
- `SHIPMENT_ID` → `oaseslive.shipment.SHIPMENT_ID`

**Referenced By (Incoming):**

- `oaseslive.batches_by_airway_bill.AIRWAY_BILL_NUMBER` → `AWB_ID`
- `oaseslive.order_line_additional_info.AIRWAY_BILL_NUMBER` → `AWB_ID`

### oaseslive.alert_colors

**Referenced By (Incoming):**

- `oaseslive.forecast_cache.ALERT_NUMBER` → `ALERT_TYPE_ID`
- `oaseslive.planners_notes_xref.ALERT_NUMBER` → `ALERT_TYPE_ID`
- `oaseslive.rd_xref_to_tech_logs.ALERT_NUMBER` → `ALERT_TYPE_ID`
- `oaseslive.rdi_history.ALERT_NUMBER` → `ALERT_TYPE_ID`
- `oaseslive.repetitive_defect_header_1.ALERT_NUMBER` → `ALERT_TYPE_ID`
- `oaseslive.repetitive_defect_header_2.ALERT_NUMBER` → `ALERT_TYPE_ID`
- `oaseslive.repetitive_defect_narrative.ALERT_NUMBER` → `ALERT_TYPE_ID`
- `oaseslive.repetitive_defect_tech_logs.ALERT_NUMBER` → `ALERT_TYPE_ID`
- `oaseslive.requirements.alert_number` → `ALERT_TYPE_ID`
- `oaseslive.tech_log_2.alert_number` → `ALERT_TYPE_ID`

### oaseslive.alternate_parts

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `ALTERNATE_PART_NUMBER` → `oaseslive.alternate_parts.PART_NUMBER`

**Referenced By (Incoming):**

- `oaseslive.alternate_parts.ALTERNATE_PART_NUMBER` → `PART_NUMBER`
- `oaseslive.fleet_chap_part_header_1.ALTERNATE_PART_NUMBER` → `PART_NUMBER`
- `oaseslive.pick_hist_7890_bkp.ALTERNATE_PART_NUMBER` → `PART_NUMBER`
- `oaseslive.pick_history.ALTERNATE_PART_NUMBER` → `PART_NUMBER`
- `oaseslive.rfc_aircraft.na_id` → `PART_NUMBER`
- `oaseslive.rfc_components.na_id` → `PART_NUMBER`
- `oaseslive.rfc_na_notes.na_id` → `PART_NUMBER`
- `oaseslive.rfc_na_notes.na_code` → `PART_NUMBER`

### oaseslive.amp_acc_panel_desc_osd_33348

**References (Outgoing):**

- `ACCESS_PANEL_CODE` → `oaseslive.amp_access_panel_desc_hdr.fleet`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`

### oaseslive.amp_access_panel_desc_hdr

**References (Outgoing):**

- `revision_id` → `oaseslive.amp_revisions.revision_id`

**Referenced By (Incoming):**

- `oaseslive.amp_acc_panel_desc_osd_33348.ACCESS_PANEL_CODE` → `fleet`
- `oaseslive.amp_access_panel_descriptions.access_panel_code` → `fleet`
- `oaseslive.amp_access_panel_effectivity.ACCESS_PANEL_CODE` → `fleet`
- `oaseslive.amp_accesspanel_effectivity_jn.ACCESS_PANEL_CODE` → `fleet`
- `oaseslive.cq_quote_nrc_access_panels.ACCESS_PANEL_CODE` → `fleet`
- `oaseslive.nrc_access_panels.access_panel_code` → `fleet`

### oaseslive.amp_access_panel_descriptions

**References (Outgoing):**

- `access_panel_code` → `oaseslive.amp_access_panel_desc_hdr.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`

### oaseslive.amp_access_panel_effectivity

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `ACCESS_PANEL_CODE` → `oaseslive.amp_access_panel_desc_hdr.fleet`
- `FLEET_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `SUB_FLEET_ID` → `oaseslive.sub_fleets.sub_fleet_id`

**Referenced By (Incoming):**

- `oaseslive.aircraft_header_2.effectivity_code` → `AP_AC_EFFECTIVITY_ID`

### oaseslive.amp_access_panel_notes

**References (Outgoing):**

- `revision_id` → `oaseslive.amp_revisions.revision_id`

### oaseslive.amp_access_panels_by_workcard

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`
- `sequence_number` → `oaseslive.nrc_high_sequence_control.KEY_ID`

**Referenced By (Incoming):**

- `oaseslive.aircraft_statistics.WORKCARD_NUMBER` → `fleet`
- `oaseslive.amp_access_panels_by_workcard.workcard_number` → `fleet`
- `oaseslive.amp_audit_notes.WORKCARD_NUMBER` → `fleet`
- `oaseslive.amp_comments.workcard_number` → `fleet`
- `oaseslive.amp_document_effectivity.workcard_id` → `fleet`
- `oaseslive.amp_document_effectivity_bk.WORKCARD_ID` → `fleet`
- `oaseslive.amp_documents_by_workcard.workcard_number` → `fleet`
- `oaseslive.amp_documents_by_workcard.workcard_id` → `fleet`
- `oaseslive.amp_documents_by_workcard_bk.WORKCARD_NUMBER` → `fleet`
- `oaseslive.amp_documents_by_workcard_bk.WORKCARD_ID` → `fleet`
- `oaseslive.amp_material_effectivity.WORKCARD_ID` → `fleet`
- `oaseslive.amp_material_effectivity_jn.WORKCARD_ID` → `fleet`
- `oaseslive.amp_materials_required_by_wc.workcard_number` → `fleet`
- `oaseslive.amp_packages_by_workcard.workcard_number` → `fleet`
- `oaseslive.amp_planning_notes.WORKCARD_NUMBER` → `fleet`
- `oaseslive.amp_wc_aircraft_exclusions.workcard_number` → `fleet`
- `oaseslive.amp_wcard_extended_desc_41.WORKCARD_NUMBER` → `fleet`
- `oaseslive.amp_workcard_ac_effectivity.WORKCARD_ID` → `fleet`
- `oaseslive.amp_workcard_ac_effectivity_jn.WORKCARD_ID` → `fleet`
- `oaseslive.amp_workcard_accomplishments.WORKCARD_NUMBER` → `fleet`
- `oaseslive.amp_workcard_activations.workcard_number` → `fleet`
- `oaseslive.amp_workcard_call_workcard.workcard_number` → `fleet`
- `oaseslive.amp_workcard_cancellations.WORKCARD_NUMBER` → `fleet`
- `oaseslive.amp_workcard_extended_desc.workcard_number` → `fleet`
- `oaseslive.amp_workcard_header_1.workcard_number` → `fleet`
- `oaseslive.amp_workcard_header_1.workcard_id` → `fleet`
- `oaseslive.amp_workcard_header_1_43216.WORKCARD_NUMBER` → `fleet`
- `oaseslive.amp_workcard_header_1_43216.WORKCARD_ID` → `fleet`
- `oaseslive.amp_workcard_header_2.workcard_number` → `fleet`
- `oaseslive.amp_workcard_header_4.workcard_number` → `fleet`
- `oaseslive.amp_workcard_header_5.workcard_number` → `fleet`
- `oaseslive.amp_workcard_header_properties.workcard_number` → `fleet`
- `oaseslive.amp_workcard_lcl_applicability.WORKCARD_NUMBER` → `fleet`
- `oaseslive.amp_workcard_narrative.workcard_number` → `fleet`
- `oaseslive.amp_workcard_not_with_workcard.workcard_number` → `fleet`
- `oaseslive.amp_workcard_previously_acc_by.workcard_number` → `fleet`
- `oaseslive.amp_workcard_publications.WORKCARD_ID` → `fleet`
- `oaseslive.amp_workcards_by_package.workcard_number` → `fleet`
- `oaseslive.amp_workcards_by_section.workcard_number` → `fleet`
- `oaseslive.bar_codes.WORKCARD_NUMBER` → `fleet`
- `oaseslive.cq_quote_cards.workcard_number` → `fleet`
- `oaseslive.cq_quote_materials.workcard_number` → `fleet`
- `oaseslive.dmg_rpr_inspections.WORKCARD_NUMBER` → `fleet`
- `oaseslive.dmg_rpr_interim_repairs.WORKCARD_NUMBER` → `fleet`
- `oaseslive.dmg_rpr_permanent_repairs.WORKCARD_NUMBER` → `fleet`
- `oaseslive.dmg_rpr_time_limited_repairs.WORKCARD_NUMBER` → `fleet`
- `oaseslive.engineering_support_history.WORKCARD_NUMBER` → `fleet`
- `oaseslive.fleet_statistics.WORKCARD_NUMBER` → `fleet`
- `oaseslive.forecast_cache.WORKCARD_CODE` → `fleet`
- `oaseslive.forecast_variation_details.WORKCARD_NUMBER` → `fleet`
- `oaseslive.lmc_base_data_reported_wc.WORKCARD_NUMBER` → `fleet`
- `oaseslive.maint_card_pref_cost_cats.WORKCARD_NUMBER` → `fleet`
- `oaseslive.maint_cost_budget_adsb.WORKCARD_ID` → `fleet`
- `oaseslive.maint_cost_budget_adsb.WORKCARD_NUMBER` → `fleet`
- `oaseslive.maint_cost_budget_workcards.WORKCARD_ID` → `fleet`
- `oaseslive.maint_cost_budget_workcards.WORKCARD_NUMBER` → `fleet`
- `oaseslive.nrc_defect_notes.WORKCARD_NUMBER` → `fleet`
- `oaseslive.nrc_print_history.WORKCARD_NUMBER` → `fleet`
- `oaseslive.nrc_rectification_notes.WORKCARD_NUMBER` → `fleet`
- `oaseslive.nrc_requirements_actions.workcard_number` → `fleet`
- `oaseslive.nrc_status_history.WORKCARD_NUMBER` → `fleet`
- `oaseslive.nrc_xref_to_scheduled_workcard.WORKCARD_NUMBER` → `fleet`
- `oaseslive.oeim_credit_warranty.card_number` → `fleet`
- `oaseslive.oeim_invoice_cards.card_number` → `fleet`
- `oaseslive.oeim_invoice_inclusive_hrs.card_number` → `fleet`
- `oaseslive.oeim_invoice_materials.card_number` → `fleet`
- `oaseslive.oeim_invoice_warranty.card_number` → `fleet`
- `oaseslive.oeim_invoice_warranty_refunds.card_number` → `fleet`
- `oaseslive.oeim_quote_dismissed.WORKCARD_NUMBER` → `fleet`
- `oaseslive.rfc_frequency_phases.workcard_number` → `fleet`
- `oaseslive.rp_dependencies.WORKCARD_NUMBER` → `fleet`
- `oaseslive.rp_employee_allocation.WORKCARD_NUMBER` → `fleet`
- `oaseslive.rp_wo_base_workcard_plan.WORKCARD_NUMBER` → `fleet`
- `oaseslive.rp_wo_workcard_plan.workcard_number` → `fleet`
- `oaseslive.schedule_forecast_xref.WORKCARD_NUMBER` → `fleet`
- `oaseslive.schedule_forecast_xref.WORKCARD_ID` → `fleet`
- `oaseslive.sfdc_component_changes.WORKCARD_NUMBER` → `fleet`
- `oaseslive.structural_damage.workcard_number` → `fleet`
- `oaseslive.task_activity_link.WORKCARD_NUMBER` → `fleet`
- `oaseslive.tech_log_2.workcard_number` → `fleet`
- `oaseslive.tech_log_workcard_link.WORKCARD_NUMBER` → `fleet`
- `oaseslive.units_of_measure.workcard_id` → `fleet`

### oaseslive.amp_accesspanel_effectivity_jn

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `ACCESS_PANEL_CODE` → `oaseslive.amp_access_panel_desc_hdr.fleet`
- `FLEET_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `SUB_FLEET_ID` → `oaseslive.sub_fleets.sub_fleet_id`

### oaseslive.amp_audit_notes

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `FLEET_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `VISIT_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `PACKAGE_CODE` → `oaseslive.amp_package_notes.fleet`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`

**Referenced By (Incoming):**

- `oaseslive.access_dim_sales_info.AUDIT_NUMBER` → `FLEET_CODE`
- `oaseslive.audit_trail.AUDIT_ID` → `FLEET_CODE`
- `oaseslive.audit_trail_ids.AUDIT_ID` → `FLEET_CODE`
- `oaseslive.audit_trail_meta_data.AUDIT_ID` → `FLEET_CODE`

### oaseslive.amp_comments

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `fleet_code` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `visit_code` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `package_code` → `oaseslive.amp_package_notes.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`

### oaseslive.amp_component_intervals

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `component_interval_id` → `oaseslive.amp_component_intervals.component_interval_id`
- `revision_id` → `oaseslive.amp_revisions.revision_id`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `component_life_limit_id` → `oaseslive.component_life_limits.component_life_limit_id`

**Referenced By (Incoming):**

- `oaseslive.amp_component_intervals.component_interval_id` → `component_interval_id`
- `oaseslive.amp_component_intervals_limits.component_interval_id` → `component_interval_id`
- `oaseslive.amp_component_intervals_stages.component_interval_id` → `component_interval_id`
- `oaseslive.amp_component_reset_on_compl.COMPONENT_INTERVAL_ID` → `component_interval_id`

### oaseslive.amp_component_intervals_limits

**References (Outgoing):**

- `component_interval_id` → `oaseslive.amp_component_intervals.component_interval_id`
- `life_code_level_id` → `oaseslive.life_code_levels.life_code_level_id`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_stage_limits.LIMIT_ID` → `component_interval_id`

### oaseslive.amp_component_intervals_stages

**References (Outgoing):**

- `component_interval_id` → `oaseslive.amp_component_intervals.component_interval_id`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_stage_limits.STAGE_ID` → `component_interval_id`
- `oaseslive.dmg_rpr_stages.STAGE_ID` → `component_interval_id`
- `oaseslive.rfc_evaluation_stages.stage_code` → `component_interval_id`
- `oaseslive.rfc_status.stage_code` → `component_interval_id`

### oaseslive.amp_component_reset_on_compl

**References (Outgoing):**

- `COMPONENT_INTERVAL_ID` → `oaseslive.amp_component_intervals.component_interval_id`
- `COMPONENT_LIFE_LIMIT_ID` → `oaseslive.component_life_limits.component_life_limit_id`

### oaseslive.amp_data_migration_log

**References (Outgoing):**

- `LOG_NUMBER` → `oaseslive.amp_data_migration_log.LOG_NUMBER`

**Referenced By (Incoming):**

- `oaseslive.amp_data_migration_log.LOG_NUMBER` → `LOG_NUMBER`
- `oaseslive.oases_message_log.LOG_NUMBER` → `LOG_NUMBER`
- `oaseslive.oeim_transaction_log_details.LOG_NUMBER` → `LOG_NUMBER`
- `oaseslive.oeim_transaction_log_header.LOG_NUMBER` → `LOG_NUMBER`
- `oaseslive.rfc_print_history_log.LOG_ID` → `LOG_NUMBER`
- `oaseslive.rfc_transaction_log.LOG_ID` → `LOG_NUMBER`

### oaseslive.amp_datmig_accomplishments

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `VISIT_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `PACKAGE_CODE` → `oaseslive.amp_package_notes.fleet`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.amp_datmig_comp_task_lookup

**References (Outgoing):**

- `PACKAGE_CODE` → `oaseslive.amp_package_notes.fleet`

**Referenced By (Incoming):**

- `oaseslive.employee_presence_log.TASK_NUMBER` → `FLEET`
- `oaseslive.oeim_invoice_snap_sfdc_book.TASK_NUMBER` → `FLEET`
- `oaseslive.sfdc_bookings.TASK_NUMBER` → `FLEET`
- `oaseslive.sfdc_deleted_bookings.TASK_NUMBER` → `FLEET`
- `oaseslive.sfdc_open_bookings.TASK_NUMBER` → `FLEET`
- `oaseslive.tool_check_out_in.task_number` → `FLEET`

### oaseslive.amp_datmig_fleet_visit_pack

**Referenced By (Incoming):**

- `oaseslive.accomp_bkup.VISIT_CODE` → `FLEET`
- `oaseslive.accomp_hist_delta_1763.VISIT_CODE` → `FLEET`
- `oaseslive.accomp_hist_lost_sched.VISIT_CODE` → `FLEET`
- `oaseslive.accomplishment_history.VISIT_CODE` → `FLEET`
- `oaseslive.aircraft_major_checks.VISIT_CODE` → `FLEET`
- `oaseslive.amp_access_panel_effectivity.FLEET_CODE` → `FLEET`
- `oaseslive.amp_accesspanel_effectivity_jn.FLEET_CODE` → `FLEET`
- `oaseslive.amp_audit_notes.FLEET_CODE` → `FLEET`
- `oaseslive.amp_audit_notes.VISIT_CODE` → `FLEET`
- `oaseslive.amp_comments.fleet_code` → `FLEET`
- `oaseslive.amp_comments.visit_code` → `FLEET`
- `oaseslive.amp_datmig_accomplishments.VISIT_CODE` → `FLEET`
- `oaseslive.amp_packages_by_visit.VISIT_CODE` → `FLEET`
- `oaseslive.amp_planning_notes.FLEET_CODE` → `FLEET`
- `oaseslive.amp_planning_notes.VISIT_CODE` → `FLEET`
- `oaseslive.amp_visit_notes.visit_code` → `FLEET`
- `oaseslive.amp_visits.visit_code` → `FLEET`
- `oaseslive.assemble_thrust_life_code.FLEET_CODE` → `FLEET`
- `oaseslive.dmg_rpr_doc_effectivity.FLEET_CODE` → `FLEET`
- `oaseslive.dmg_rpr_document_order.FLEET_CODE` → `FLEET`
- `oaseslive.fleet_assembles.FLEET_CODE` → `FLEET`
- `oaseslive.forecast_cache.VISIT_CODE` → `FLEET`
- `oaseslive.forecast_cache_revisions.fleet_code` → `FLEET`
- `oaseslive.maint_cost_budget_visits.VISIT_CODE` → `FLEET`
- `oaseslive.planners_notes_xref.VISIT_CODE` → `FLEET`
- `oaseslive.sample_fleets.fleet_code` → `FLEET`
- `oaseslive.sample_fleets_jn.FLEET_CODE` → `FLEET`
- `oaseslive.schedule_forecast_xref.VISIT_CODE` → `FLEET`
- `oaseslive.sub_fleet_header.fleet_code` → `FLEET`
- `oaseslive.task_activity_link.VISIT_CODE` → `FLEET`

### oaseslive.amp_datmig_llp

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.amp_document_effectivity

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `document_id` → `oaseslive.aircraft_documents.AIRCRAFT_DOCUMENT_ID`
- `workcard_id` → `oaseslive.amp_access_panels_by_workcard.fleet`

### oaseslive.amp_document_effectivity_bk

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `DOCUMENT_ID` → `oaseslive.aircraft_documents.AIRCRAFT_DOCUMENT_ID`
- `WORKCARD_ID` → `oaseslive.amp_access_panels_by_workcard.fleet`

### oaseslive.amp_documents_by_workcard

**References (Outgoing):**

- `document_id` → `oaseslive.aircraft_documents.AIRCRAFT_DOCUMENT_ID`
- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `workcard_id` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`
- `sequence_number` → `oaseslive.nrc_high_sequence_control.KEY_ID`

### oaseslive.amp_documents_by_workcard_bk

**References (Outgoing):**

- `DOCUMENT_ID` → `oaseslive.aircraft_documents.AIRCRAFT_DOCUMENT_ID`
- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `WORKCARD_ID` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `SEQUENCE_NUMBER` → `oaseslive.nrc_high_sequence_control.KEY_ID`

### oaseslive.amp_manufacturers_documents

**References (Outgoing):**

- `DOCUMENT_ID` → `oaseslive.aircraft_documents.AIRCRAFT_DOCUMENT_ID`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`

### oaseslive.amp_material_effectivity

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `WORKCARD_ID` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `SUB_FLEET_ID` → `oaseslive.sub_fleets.sub_fleet_id`

**Referenced By (Incoming):**

- `oaseslive.maint_cost_budget_materials.MATERIAL_ID` → `WORKCARD_MATERIAL_ID`

### oaseslive.amp_material_effectivity_jn

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `WORKCARD_ID` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `SUB_FLEET_ID` → `oaseslive.sub_fleets.sub_fleet_id`

### oaseslive.amp_materials_required_by_wc

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`
- `sequence_number` → `oaseslive.nrc_high_sequence_control.KEY_ID`

### oaseslive.amp_package_notes

**References (Outgoing):**

- `package_code` → `oaseslive.amp_package_notes.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`

**Referenced By (Incoming):**

- `oaseslive.accomp_bkup.PACKAGE_CODE` → `fleet`
- `oaseslive.accomp_hist_delta_1763.PACKAGE_CODE` → `fleet`
- `oaseslive.accomp_hist_lost_sched.PACKAGE_CODE` → `fleet`
- `oaseslive.accomplishment_history.PACKAGE_CODE` → `fleet`
- `oaseslive.aircraft_major_checks.PACKAGE_CODE` → `fleet`
- `oaseslive.amp_audit_notes.PACKAGE_CODE` → `fleet`
- `oaseslive.amp_comments.package_code` → `fleet`
- `oaseslive.amp_datmig_accomplishments.PACKAGE_CODE` → `fleet`
- `oaseslive.amp_datmig_comp_task_lookup.PACKAGE_CODE` → `fleet`
- `oaseslive.amp_package_notes.package_code` → `fleet`
- `oaseslive.amp_packages.package_code` → `fleet`
- `oaseslive.amp_packages_by_visit.PACKAGE_CODE` → `fleet`
- `oaseslive.amp_planning_notes.PACKAGE_CODE` → `fleet`
- `oaseslive.amp_workcards_by_package.package_code` → `fleet`
- `oaseslive.cq_quote_cards.package_code` → `fleet`
- `oaseslive.cq_quote_packages.package_code` → `fleet`
- `oaseslive.forecast_cache.PACKAGE_CODE` → `fleet`
- `oaseslive.maint_cost_budget_packages.PACKAGE_CODE` → `fleet`
- `oaseslive.maint_pack_pref_cost_cats.PACKAGE_CODE` → `fleet`
- `oaseslive.oeim_invoice_cards.package_code` → `fleet`
- `oaseslive.oeim_invoice_materials.package_code` → `fleet`
- `oaseslive.oeim_invoice_packages.package_code` → `fleet`
- `oaseslive.oeim_invoice_warranty.package_code` → `fleet`
- `oaseslive.oeim_quote_dismissed.PACKAGE_CODE` → `fleet`
- `oaseslive.package.PACKAGE_ID` → `fleet`
- `oaseslive.package_items.PACKAGE_ID` → `fleet`
- `oaseslive.planners_notes_xref.PACKAGE_CODE` → `fleet`
- `oaseslive.schedule_forecast_xref.PACKAGE_CODE` → `fleet`
- `oaseslive.task_activity_link.PACKAGE_CODE` → `fleet`

### oaseslive.amp_packages

**References (Outgoing):**

- `package_code` → `oaseslive.amp_package_notes.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`

**Referenced By (Incoming):**

- `oaseslive.fleet_forecast_plans_amp.PACKAGE_CODES` → `fleet`

### oaseslive.amp_packages_by_visit

**References (Outgoing):**

- `VISIT_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `PACKAGE_CODE` → `oaseslive.amp_package_notes.fleet`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`

### oaseslive.amp_packages_by_workcard

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`
- `sequence_number` → `oaseslive.nrc_high_sequence_control.KEY_ID`

### oaseslive.amp_planning_notes

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `FLEET_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `VISIT_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `PACKAGE_CODE` → `oaseslive.amp_package_notes.fleet`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`

**Referenced By (Incoming):**

- `oaseslive.fleet_forecast_plans.PLAN_ID` → `FLEET_CODE`
- `oaseslive.fleet_forecast_plans_amp.PLAN_ID` → `FLEET_CODE`
- `oaseslive.fleet_forecast_plans_drn.PLAN_ID` → `FLEET_CODE`
- `oaseslive.fleet_forecast_plans_rfc.PLAN_ID` → `FLEET_CODE`

### oaseslive.amp_report_documents

**References (Outgoing):**

- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `DOCUMENT_IMAGE_ID` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`

**Referenced By (Incoming):**

- `oaseslive.accomp_bkup.REPORT_ID` → `FLEET`
- `oaseslive.accomp_hist_delta_1763.REPORT_ID` → `FLEET`
- `oaseslive.accomp_hist_lost_sched.REPORT_ID` → `FLEET`
- `oaseslive.accomplishment_history.REPORT_ID` → `FLEET`
- `oaseslive.completion_maint_mod.REPORT_ID` → `FLEET`
- `oaseslive.component_movement_history_ext.report_id` → `FLEET`
- `oaseslive.component_movt_hist_ext_8661.REPORT_ID` → `FLEET`
- `oaseslive.delays.report_id` → `FLEET`
- `oaseslive.drn_component_mods_history.REPORT_ID` → `FLEET`
- `oaseslive.drn_maintenance_history.REPORT_ID` → `FLEET`
- `oaseslive.drn_modification_history.REPORT_ID` → `FLEET`
- `oaseslive.flown_sectors.report_id` → `FLEET`
- `oaseslive.flown_sectors_bkp.REPORT_ID` → `FLEET`
- `oaseslive.flown_sectors_con_680.REPORT_ID` → `FLEET`
- `oaseslive.flown_sectors_delta1817.REPORT_ID` → `FLEET`
- `oaseslive.life_code_entry.report_id` → `FLEET`
- `oaseslive.life_code_entry_backup.REPORT_ID` → `FLEET`
- `oaseslive.life_code_entry_dbf1065.REPORT_ID` → `FLEET`
- `oaseslive.netline_import_index.REPORT_ID` → `FLEET`
- `oaseslive.oases_reports.REPORT_ID` → `FLEET`
- `oaseslive.osys_key_to_reportid.REPORT_ID` → `FLEET`
- `oaseslive.pdc_import_index.report_id` → `FLEET`
- `oaseslive.sabre_flight_map.REPORT_ID` → `FLEET`
- `oaseslive.tech_log_3.report_id` → `FLEET`
- `oaseslive.tech_log_documents.REPORT_ID` → `FLEET`

### oaseslive.amp_revision_history

**References (Outgoing):**

- `HISTORY_ID` → `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `USER_ID` → `oaseslive.dataset_locks_by_user.USER_ID`

### oaseslive.amp_revision_status

**References (Outgoing):**

- `REVISION_STATUS_ID` → `oaseslive.amp_revision_status.REVISION_STATUS_ID`

**Referenced By (Incoming):**

- `oaseslive.amp_revision_status.REVISION_STATUS_ID` → `REVISION_STATUS_ID`
- `oaseslive.amp_revisions.revision_status_id` → `REVISION_STATUS_ID`
- `oaseslive.cq_quote_status.status_id` → `REVISION_STATUS_ID`
- `oaseslive.cq_quote_status_contacts.STATUS_ID` → `REVISION_STATUS_ID`
- `oaseslive.nrc_status_history.STATUS_CODE` → `REVISION_STATUS_ID`
- `oaseslive.planners_notes.STATUS_ID` → `REVISION_STATUS_ID`
- `oaseslive.planners_notes_statuses.STATUS_ID` → `REVISION_STATUS_ID`
- `oaseslive.rd_xref_to_tech_logs.STATUS_CODE` → `REVISION_STATUS_ID`
- `oaseslive.shipment_status_type.STATUS_ID` → `REVISION_STATUS_ID`

### oaseslive.amp_revisions

**References (Outgoing):**

- `revision_status_id` → `oaseslive.amp_revision_status.REVISION_STATUS_ID`
- `revision_id` → `oaseslive.amp_revisions.revision_id`
- `user_id` → `oaseslive.dataset_locks_by_user.USER_ID`

**Referenced By (Incoming):**

- `oaseslive.accomp_bkup.REVISION_ID` → `revision_id`
- `oaseslive.accomp_hist_delta_1763.REVISION_ID` → `revision_id`
- `oaseslive.accomp_hist_lost_sched.REVISION_ID` → `revision_id`
- `oaseslive.accomplishment_history.REVISION_ID` → `revision_id`
- `oaseslive.amp_acc_panel_desc_osd_33348.REVISION_ID` → `revision_id`
- `oaseslive.amp_access_panel_desc_hdr.revision_id` → `revision_id`
- `oaseslive.amp_access_panel_descriptions.revision_id` → `revision_id`
- `oaseslive.amp_access_panel_effectivity.REVISION_ID` → `revision_id`
- `oaseslive.amp_access_panel_notes.revision_id` → `revision_id`
- `oaseslive.amp_access_panels_by_workcard.revision_id` → `revision_id`
- `oaseslive.amp_accesspanel_effectivity_jn.REVISION_ID` → `revision_id`
- `oaseslive.amp_audit_notes.REVISION_ID` → `revision_id`
- `oaseslive.amp_comments.revision_id` → `revision_id`
- `oaseslive.amp_component_intervals.revision_id` → `revision_id`
- `oaseslive.amp_documents_by_workcard.revision_id` → `revision_id`
- `oaseslive.amp_documents_by_workcard_bk.REVISION_ID` → `revision_id`
- `oaseslive.amp_manufacturers_documents.REVISION_ID` → `revision_id`
- `oaseslive.amp_materials_required_by_wc.revision_id` → `revision_id`
- `oaseslive.amp_package_notes.revision_id` → `revision_id`
- `oaseslive.amp_packages.revision_id` → `revision_id`
- `oaseslive.amp_packages_by_visit.REVISION_ID` → `revision_id`
- `oaseslive.amp_packages_by_workcard.revision_id` → `revision_id`
- `oaseslive.amp_planning_notes.REVISION_ID` → `revision_id`
- `oaseslive.amp_report_documents.REVISION_ID` → `revision_id`
- `oaseslive.amp_revision_history.REVISION_ID` → `revision_id`
- `oaseslive.amp_revisions.revision_id` → `revision_id`
- `oaseslive.amp_visit_notes.revision_id` → `revision_id`
- `oaseslive.amp_visits.revision_id` → `revision_id`
- `oaseslive.amp_wc_aircraft_exclusions.revision_id` → `revision_id`
- `oaseslive.amp_wcard_extended_desc_41.REVISION_ID` → `revision_id`
- `oaseslive.amp_workcard_accomplishments.REVISION_ID` → `revision_id`
- `oaseslive.amp_workcard_activations.revision_id` → `revision_id`
- `oaseslive.amp_workcard_call_workcard.revision_id` → `revision_id`
- `oaseslive.amp_workcard_cancellations.REVISION_ID` → `revision_id`
- `oaseslive.amp_workcard_extended_desc.revision_id` → `revision_id`
- `oaseslive.amp_workcard_h3_7487bkp.REVISION_ID` → `revision_id`
- `oaseslive.amp_workcard_header_1.revision_id` → `revision_id`
- `oaseslive.amp_workcard_header_1_43216.REVISION_ID` → `revision_id`
- `oaseslive.amp_workcard_header_2.revision_id` → `revision_id`
- `oaseslive.amp_workcard_header_3.revision_id` → `revision_id`
- `oaseslive.amp_workcard_header_4.revision_id` → `revision_id`
- `oaseslive.amp_workcard_header_5.revision_number` → `revision_id`
- `oaseslive.amp_workcard_header_5.revision_id` → `revision_id`
- `oaseslive.amp_workcard_header_properties.revision_id` → `revision_id`
- `oaseslive.amp_workcard_lcl_applicability.REVISION_ID` → `revision_id`
- `oaseslive.amp_workcard_narrative.revision_id` → `revision_id`
- `oaseslive.amp_workcard_not_with_workcard.revision_id` → `revision_id`
- `oaseslive.amp_workcard_previously_acc_by.revision_id` → `revision_id`
- `oaseslive.amp_workcards_by_package.revision_id` → `revision_id`
- `oaseslive.amp_workcards_by_section.revision_id` → `revision_id`
- `oaseslive.fleet_forecast_plans.REVISION_ID` → `revision_id`
- `oaseslive.forecast_cache.REVISION_ID` → `revision_id`
- `oaseslive.forecast_cache_ac_details.revision_id` → `revision_id`
- `oaseslive.forecast_cache_revisions.revision_id` → `revision_id`
- `oaseslive.maint_cost_budget_adsb.REVISION_ID` → `revision_id`
- `oaseslive.maint_cost_budget_packages.REVISION_ID` → `revision_id`
- `oaseslive.maint_cost_budget_visits.REVISION_ID` → `revision_id`
- `oaseslive.maint_cost_budget_workcards.REVISION_ID` → `revision_id`
- `oaseslive.manufacturers_work_documents.REVISION_ID` → `revision_id`
- `oaseslive.mel_items.revision_id` → `revision_id`
- `oaseslive.mel_references.revision_id` → `revision_id`
- `oaseslive.mel_revision_history.REVISION_ID` → `revision_id`
- `oaseslive.mel_revisions.revision_id` → `revision_id`
- `oaseslive.planners_notes_xref.REVISION_ID` → `revision_id`
- `oaseslive.rp_dependencies.REVISION_ID` → `revision_id`
- `oaseslive.tech_log_3.revision_id` → `revision_id`

### oaseslive.amp_visit_notes

**References (Outgoing):**

- `visit_code` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `revision_id` → `oaseslive.amp_revisions.revision_id`

### oaseslive.amp_visits

**References (Outgoing):**

- `visit_code` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `revision_id` → `oaseslive.amp_revisions.revision_id`
- `sequence_number` → `oaseslive.nrc_high_sequence_control.KEY_ID`

**Referenced By (Incoming):**

- `oaseslive.fleet_forecast_plans_amp.VISIT_CODES` → `fleet`

### oaseslive.amp_wc_aircraft_exclusions

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`
- `sequence_number` → `oaseslive.nrc_high_sequence_control.KEY_ID`

### oaseslive.amp_wc_in_limits_bak

**References (Outgoing):**

- `WORKCARD_INTERVAL_ID` → `oaseslive.amp_workcard_intervals_limits.workcard_interval_id`
- `LIFE_CODE_LEVEL_ID` → `oaseslive.life_code_levels.life_code_level_id`

### oaseslive.amp_wc_in_stages_bak

**References (Outgoing):**

- `WORKCARD_INTERVAL_ID` → `oaseslive.amp_workcard_intervals_limits.workcard_interval_id`

### oaseslive.amp_wcard_extended_desc_41

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`

### oaseslive.amp_workcard_ac_effectivity

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `WORKCARD_ID` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `SUB_FLEET_ID` → `oaseslive.sub_fleets.sub_fleet_id`

### oaseslive.amp_workcard_ac_effectivity_jn

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `WORKCARD_ID` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `SUB_FLEET_ID` → `oaseslive.sub_fleets.sub_fleet_id`

### oaseslive.amp_workcard_accomplishments

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`

### oaseslive.amp_workcard_activations

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`
- `workcard_activation_id` → `oaseslive.amp_workcard_activations.workcard_activation_id`

**Referenced By (Incoming):**

- `oaseslive.access_dim_accounts_info.VAT_CODE` → `workcard_activation_id`
- `oaseslive.access_dim_sales_info.VAT_CODE` → `workcard_activation_id`
- `oaseslive.amp_workcard_activations.workcard_activation_id` → `workcard_activation_id`
- `oaseslive.invoice_lines.VAT_CODE` → `workcard_activation_id`
- `oaseslive.oeim_invoice_snap_vat_codes.VAT_CODE` → `workcard_activation_id`
- `oaseslive.order_goods_received_invoices.VAT_CODE` → `workcard_activation_id`
- `oaseslive.order_line_quotes_data.VAT_CODE` → `workcard_activation_id`
- `oaseslive.order_lines.vat_code` → `workcard_activation_id`
- `oaseslive.part_number_vat_codes.VAT_CODE` → `workcard_activation_id`
- `oaseslive.preorder_lines.VAT_CODE` → `workcard_activation_id`
- `oaseslive.stock_groups.vat_code` → `workcard_activation_id`
- `oaseslive.stock_groups_bkp_oases382.VAT_CODE` → `workcard_activation_id`

### oaseslive.amp_workcard_call_workcard

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`
- `workcard_call_workcard_id` → `oaseslive.amp_workcard_call_workcard.workcard_call_workcard_id`
- `call_workcard_number` → `oaseslive.amp_workcard_call_workcard.workcard_call_workcard_id`

**Referenced By (Incoming):**

- `oaseslive.amp_workcard_call_workcard.workcard_call_workcard_id` → `workcard_call_workcard_id`
- `oaseslive.amp_workcard_call_workcard.call_workcard_number` → `workcard_call_workcard_id`

### oaseslive.amp_workcard_cancellations

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `WORKCARD_CANCELLATION_ID` → `oaseslive.amp_workcard_cancellations.WORKCARD_CANCELLATION_ID`

**Referenced By (Incoming):**

- `oaseslive.amp_workcard_cancellations.WORKCARD_CANCELLATION_ID` → `WORKCARD_CANCELLATION_ID`

### oaseslive.amp_workcard_extended_desc

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`

### oaseslive.amp_workcard_h3_7487bkp

**References (Outgoing):**

- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `PHASE_CODE` → `oaseslive.rfc_frequency_phase_header.rfc_id`

### oaseslive.amp_workcard_header_1

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `workcard_id` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`

### oaseslive.amp_workcard_header_1_43216

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `WORKCARD_ID` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`

### oaseslive.amp_workcard_header_2

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`

### oaseslive.amp_workcard_header_3

**References (Outgoing):**

- `revision_id` → `oaseslive.amp_revisions.revision_id`
- `phase_code` → `oaseslive.rfc_frequency_phase_header.rfc_id`

### oaseslive.amp_workcard_header_4

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`

### oaseslive.amp_workcard_header_5

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `revision_number` → `oaseslive.amp_revisions.revision_id`
- `revision_id` → `oaseslive.amp_revisions.revision_id`

### oaseslive.amp_workcard_header_properties

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`

### oaseslive.amp_workcard_intervals_limits

**References (Outgoing):**

- `workcard_interval_id` → `oaseslive.amp_workcard_intervals_limits.workcard_interval_id`
- `life_code_level_id` → `oaseslive.life_code_levels.life_code_level_id`

**Referenced By (Incoming):**

- `oaseslive.amp_wc_in_limits_bak.WORKCARD_INTERVAL_ID` → `workcard_interval_id`
- `oaseslive.amp_wc_in_stages_bak.WORKCARD_INTERVAL_ID` → `workcard_interval_id`
- `oaseslive.amp_workcard_intervals_limits.workcard_interval_id` → `workcard_interval_id`
- `oaseslive.amp_workcard_intervals_stages.workcard_interval_id` → `workcard_interval_id`
- `oaseslive.forecast_cache.WORKCARD_INTERVAL_ID` → `workcard_interval_id`
- `oaseslive.planners_notes_xref.WORKCARD_INTERVAL_ID` → `workcard_interval_id`
- `oaseslive.schedule_forecast_xref.WORKCARD_INTERVAL_ID` → `workcard_interval_id`

### oaseslive.amp_workcard_intervals_stages

**References (Outgoing):**

- `workcard_interval_id` → `oaseslive.amp_workcard_intervals_limits.workcard_interval_id`

### oaseslive.amp_workcard_lcl_applicability

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `LIFE_CODE_LEVEL_ID` → `oaseslive.life_code_levels.life_code_level_id`

**Referenced By (Incoming):**

- `oaseslive.part_applicability_codes.APPLICABILITY_CODE` → `LIFE_CODE_LEVEL_ID`

### oaseslive.amp_workcard_narrative

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`

### oaseslive.amp_workcard_not_with_workcard

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`
- `workcard_not_with_workcard_id` → `oaseslive.amp_workcard_not_with_workcard.workcard_not_with_workcard_id`
- `not_with_workcard_number` → `oaseslive.amp_workcard_not_with_workcard.workcard_not_with_workcard_id`

**Referenced By (Incoming):**

- `oaseslive.amp_workcard_not_with_workcard.workcard_not_with_workcard_id` → `workcard_not_with_workcard_id`
- `oaseslive.amp_workcard_not_with_workcard.not_with_workcard_number` → `workcard_not_with_workcard_id`

### oaseslive.amp_workcard_previously_acc_by

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`
- `workcard_previously_acc_id` → `oaseslive.amp_workcard_previously_acc_by.workcard_previously_acc_id`

**Referenced By (Incoming):**

- `oaseslive.amp_workcard_previously_acc_by.workcard_previously_acc_id` → `workcard_previously_acc_id`

### oaseslive.amp_workcard_publications

**References (Outgoing):**

- `WORKCARD_ID` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `PUBLICATION_ID` → `oaseslive.amp_workcard_publications.PUBLICATION_ID`
- `PUBLICATION_CODE` → `oaseslive.amp_workcard_publications.PUBLICATION_ID`

**Referenced By (Incoming):**

- `oaseslive.amp_workcard_publications.PUBLICATION_ID` → `PUBLICATION_ID`
- `oaseslive.amp_workcard_publications.PUBLICATION_CODE` → `PUBLICATION_ID`
- `oaseslive.rfc_header_publications.PUBLICATION_CODE` → `PUBLICATION_ID`
- `oaseslive.rfc_publications.PUBLICATION_CODE` → `PUBLICATION_ID`

### oaseslive.amp_workcard_saved_reports

**References (Outgoing):**

- `SAVED_REPORT_ID` → `oaseslive.amp_workcard_saved_reports.SAVED_REPORT_ID`

**Referenced By (Incoming):**

- `oaseslive.amp_workcard_saved_reports.SAVED_REPORT_ID` → `SAVED_REPORT_ID`
- `oaseslive.amp_workcard_saved_reports_hdr.SAVED_REPORT_ID` → `SAVED_REPORT_ID`

### oaseslive.amp_workcard_saved_reports_hdr

**References (Outgoing):**

- `SAVED_REPORT_ID` → `oaseslive.amp_workcard_saved_reports.SAVED_REPORT_ID`

### oaseslive.amp_workcard_sections

**References (Outgoing):**

- `section_id` → `oaseslive.amp_workcard_sections.section_id`
- `section_code` → `oaseslive.amp_workcard_sections.section_id`

**Referenced By (Incoming):**

- `oaseslive.amp_workcard_sections.section_id` → `section_id`
- `oaseslive.amp_workcard_sections.section_code` → `section_id`
- `oaseslive.amp_workcards_by_section.section_id` → `section_id`
- `oaseslive.dmg_rpr_damage.SECTION_ID` → `section_id`
- `oaseslive.dmg_rpr_measurement_sections.SECTION_ID` → `section_id`
- `oaseslive.dmg_rpr_section_details.SECTION_ID` → `section_id`
- `oaseslive.dmg_rpr_section_fleet_details.SECTION_ID` → `section_id`
- `oaseslive.dmg_rpr_subject_sections.SECTION_ID` → `section_id`
- `oaseslive.rfc_header.section_id` → `section_id`
- `oaseslive.rfc_statement_sections.SECTION_ID` → `section_id`
- `oaseslive.rfc_statement_sections.SECTION_CODE` → `section_id`

### oaseslive.amp_workcards_by_package

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `package_code` → `oaseslive.amp_package_notes.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`

**Referenced By (Incoming):**

- `oaseslive.fleet_forecast_plans_amp.WORKCARD_NUMBERS` → `fleet`

### oaseslive.amp_workcards_by_section

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `revision_id` → `oaseslive.amp_revisions.revision_id`
- `section_id` → `oaseslive.amp_workcard_sections.section_id`
- `user_id` → `oaseslive.dataset_locks_by_user.USER_ID`

### oaseslive.assemble_thrust_life_code

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `LIFE_CODE` → `oaseslive.aircraft_life.AIRCRAFT_CODE`
- `FLEET_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `LIFE_CODE_ID` → `oaseslive.assemble_thrust_life_code.LIFE_CODE_ID`

**Referenced By (Incoming):**

- `oaseslive.assemble_thrust_life_code.LIFE_CODE_ID` → `LIFE_CODE_ID`

### oaseslive.assembly_model_header

**References (Outgoing):**

- `MODEL_ID` → `oaseslive.assembly_model_header.MODEL_ID`

**Referenced By (Incoming):**

- `oaseslive.assembly_model_header.MODEL_ID` → `MODEL_ID`
- `oaseslive.assembly_model_nodes.MODEL_ID` → `MODEL_ID`

### oaseslive.assembly_model_nodes

**References (Outgoing):**

- `MODEL_ID` → `oaseslive.assembly_model_header.MODEL_ID`
- `NODE_ID` → `oaseslive.assembly_model_nodes.MODEL_ID`

**Referenced By (Incoming):**

- `oaseslive.assembly_model_nodes.NODE_ID` → `MODEL_ID`

### oaseslive.audit_trail

**References (Outgoing):**

- `AUDIT_ID` → `oaseslive.amp_audit_notes.FLEET_CODE`
- `USER_ID` → `oaseslive.dataset_locks_by_user.USER_ID`

### oaseslive.audit_trail_ids

**References (Outgoing):**

- `AUDIT_ID` → `oaseslive.amp_audit_notes.FLEET_CODE`

### oaseslive.audit_trail_meta_data

**References (Outgoing):**

- `AUDIT_ID` → `oaseslive.amp_audit_notes.FLEET_CODE`
- `META_ID` → `oaseslive.audit_trail_meta_data.META_ID`

**Referenced By (Incoming):**

- `oaseslive.audit_trail_meta_data.META_ID` → `META_ID`

### oaseslive.awsdms_validation_failures_v1

**Referenced By (Incoming):**

- `oaseslive.life_code_levels.validation_code` → `TASK_NAME`

### oaseslive.b737ng_activity_import_table

**Referenced By (Incoming):**

- `oaseslive.sfdc_activity.ACTIVITY_ID` → `SCHEDULE_REFERENCE`

### oaseslive.bar_codes

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `BAR_CODE` → `oaseslive.bar_codes.WORKS_ORDER_NUMBER`
- `WORKS_ORDER_NUMBER` → `oaseslive.credit_works_order_cards.credit_note_no`

**Referenced By (Incoming):**

- `oaseslive.bar_codes.BAR_CODE` → `WORKS_ORDER_NUMBER`

### oaseslive.batch_file_header

**Referenced By (Incoming):**

- `oaseslive.batch_history.BATCH_NUMBER` → `KEY`
- `oaseslive.batch_notes.BATCH_NUMBER` → `KEY`
- `oaseslive.batch_notes_gu4240.BATCH_NUMBER` → `KEY`
- `oaseslive.batch_orders.BATCH_NUMBER` → `KEY`
- `oaseslive.batch_record_1.batch_number` → `KEY`
- `oaseslive.batch_record_1_gu4240.BATCH_NUMBER` → `KEY`
- `oaseslive.batch_record_2.BATCH_NUMBER` → `KEY`
- `oaseslive.batch_record_camo.BATCH_NUMBER` → `KEY`
- `oaseslive.batches_by_airway_bill.BATCH_NUMBER` → `KEY`
- `oaseslive.batches_by_customs_entry.BATCH_NUMBER` → `KEY`
- `oaseslive.component_movement_history_ext.batch_number` → `KEY`
- `oaseslive.component_movt_hist_ext_8661.BATCH_NUMBER` → `KEY`
- `oaseslive.consumable_batch_locations.batch_number` → `KEY`
- `oaseslive.consumable_history.batch_number` → `KEY`
- `oaseslive.consumable_repair_xref_to_part.BATCH_NUMBER` → `KEY`
- `oaseslive.credit_works_order_cards.batch_number` → `KEY`
- `oaseslive.delivery_note_item_header_1.batch_number` → `KEY`
- `oaseslive.goods_received_sheet_document.BATCH_NUMBER` → `KEY`
- `oaseslive.ie96_historic.BATCH_NUMBER` → `KEY`
- `oaseslive.inherited_acquisition_costs.BATCH_NUMBER` → `KEY`
- `oaseslive.invoice_lines.BATCH_NUMBER` → `KEY`
- `oaseslive.invoice_trail_entries.BATCH_NUMBER` → `KEY`
- `oaseslive.maint_material_costs.BATCH_NUMBER` → `KEY`
- `oaseslive.nrc_tools.batch_number` → `KEY`
- `oaseslive.oeim_credit_warranty.batch_number` → `KEY`
- `oaseslive.oeim_invoice_materials.batch_number` → `KEY`
- `oaseslive.oeim_invoice_warranty.batch_number` → `KEY`
- `oaseslive.oeim_invoice_warranty_refunds.batch_number` → `KEY`
- `oaseslive.order_history.BATCH_NUMBER` → `KEY`
- `oaseslive.pick_hist_7890_bkp.BATCH_NUMBER` → `KEY`
- `oaseslive.pick_history.BATCH_NUMBER` → `KEY`
- `oaseslive.preorder_line_stock_info.BATCH_NUMBER` → `KEY`
- `oaseslive.repair_approval_data.BATCH_NUMBER` → `KEY`
- `oaseslive.requirement_recharge_details.BATCH_NUMBER` → `KEY`
- `oaseslive.rotable_batch_locations.batch_number` → `KEY`
- `oaseslive.rotable_history.batch_number` → `KEY`
- `oaseslive.sales_history.batch_number` → `KEY`
- `oaseslive.sales_order_dispatches.batch_number` → `KEY`
- `oaseslive.shelf_li_dt_bkp_2020.BATCH_NUMBER` → `KEY`
- `oaseslive.shelf_life_dates.batch_number` → `KEY`
- `oaseslive.shelf_life_dates_oases6834.BATCH_NUMBER` → `KEY`
- `oaseslive.shipment_demands.batch_number` → `KEY`
- `oaseslive.shipment_item.BATCH_NUMBER` → `KEY`
- `oaseslive.stock_audit_batches.BATCH_NUMBER` → `KEY`
- `oaseslive.stock_documents.BATCH_NUMBER` → `KEY`
- `oaseslive.tool_check_out_in.batch_number` → `KEY`

### oaseslive.batch_history

**References (Outgoing):**

- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `USER_ID` → `oaseslive.dataset_locks_by_user.USER_ID`

### oaseslive.batch_notes

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.batch_notes_gu4240

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.batch_orders

**References (Outgoing):**

- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

**Referenced By (Incoming):**

- `oaseslive.airway_bill_references.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.batch_orders.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.batch_record_1.order_number` → `BATCH_NUMBER`
- `oaseslive.batch_record_1_gu4240.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.consumable_history.order_number` → `BATCH_NUMBER`
- `oaseslive.consumable_repair_xref_to_part.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.credit_works_order_cards.order_number` → `BATCH_NUMBER`
- `oaseslive.delivery_note_header_1.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.dmg_rpr_document_order.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.freight_costs.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.ie96_historic.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.invoice_lines.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.invoice_trail_entries.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.loaned_units.order_number` → `BATCH_NUMBER`
- `oaseslive.monthly_loans_in.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.oeim_credit_warranty.order_number` → `BATCH_NUMBER`
- `oaseslive.oeim_invoice_materials.order_number` → `BATCH_NUMBER`
- `oaseslive.oeim_invoice_warranty.order_number` → `BATCH_NUMBER`
- `oaseslive.oeim_invoice_warranty_refunds.order_number` → `BATCH_NUMBER`
- `oaseslive.ord_po_unit_conv_delta1827.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_change_history.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_customs_info.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_delivery_note_remarks.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_email_chasing.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_goods_received.order_number` → `BATCH_NUMBER`
- `oaseslive.order_goods_received_invoices.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_header_1.order_number` → `BATCH_NUMBER`
- `oaseslive.order_header_2.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_header_3.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_header_4.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_history.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_line_additional_info.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_line_additional_info_2.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_line_notes.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_line_quotes_data.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_line_requirement_xref.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_line_weight_dimension.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_lines.order_number` → `BATCH_NUMBER`
- `oaseslive.order_numbers_by_supplier.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_print_date.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_purchase_unit_conversion.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_requirement_allocation.order_number` → `BATCH_NUMBER`
- `oaseslive.order_supplier_approval.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_text.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_workshop_works_orders.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.orders_by_due_date.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.orders_to_part_number_xref.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.ordr_goods_bkp.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.parts_received_without_cost.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.pick_hist_7890_bkp.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.pick_history.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.quote_email_chasing.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.rfq_to_order_xref.order_number` → `BATCH_NUMBER`
- `oaseslive.rotable_history.order_number` → `BATCH_NUMBER`
- `oaseslive.sage_order_line_details.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.sales_history.order_number` → `BATCH_NUMBER`
- `oaseslive.sap_order_header.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.sap_order_line.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.shipment_order_demands.order_number` → `BATCH_NUMBER`
- `oaseslive.strip_report_header_1.ORDER_NUMBER` → `BATCH_NUMBER`
- `oaseslive.taskcard_wo_order_line.ORDER_NUMBER` → `BATCH_NUMBER`

### oaseslive.batch_record_1

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `oaseslive.batch_file_header.KEY`
- `order_number` → `oaseslive.batch_orders.BATCH_NUMBER`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `currency_code` → `oaseslive.currency_codes.currency_code`
- `goods_received_number` → `oaseslive.goods_received_sheet_document.BATCH_NUMBER`

### oaseslive.batch_record_1_gu4240

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`
- `GOODS_RECEIVED_NUMBER` → `oaseslive.goods_received_sheet_document.BATCH_NUMBER`

### oaseslive.batch_record_2

**References (Outgoing):**

- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `CUSTOMS_ENTRY_NUMBER` → `oaseslive.batches_by_customs_entry.CUSTOMS_ENTRY_NUMBER`
- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`

### oaseslive.batch_record_camo

**References (Outgoing):**

- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`

### oaseslive.batches_by_airway_bill

**References (Outgoing):**

- `AIRWAY_BILL_NUMBER` → `oaseslive.airway_bill_references.AWB_ID`
- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`

### oaseslive.batches_by_customs_entry

**References (Outgoing):**

- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `CUSTOMS_ENTRY_NUMBER` → `oaseslive.batches_by_customs_entry.CUSTOMS_ENTRY_NUMBER`

**Referenced By (Incoming):**

- `oaseslive.batch_record_2.CUSTOMS_ENTRY_NUMBER` → `CUSTOMS_ENTRY_NUMBER`
- `oaseslive.batches_by_customs_entry.CUSTOMS_ENTRY_NUMBER` → `CUSTOMS_ENTRY_NUMBER`
- `oaseslive.maintenance_cost_entry.ENTRY_ID` → `CUSTOMS_ENTRY_NUMBER`
- `oaseslive.shipment_item_customs.CUSTOMS_ENTRY_NUMBER` → `CUSTOMS_ENTRY_NUMBER`

### oaseslive.bins

**References (Outgoing):**

- `warehouse_code` → `oaseslive.account_available_warehouses.ACCOUNT_CODE`
- `bin_number` → `oaseslive.bins.bin_number`

**Referenced By (Incoming):**

- `oaseslive.bins.bin_number` → `bin_number`
- `oaseslive.ie96_historic.BIN_NUMBER` → `bin_number`
- `oaseslive.order_lines.bin_number` → `bin_number`
- `oaseslive.preorder_line_stock_info.BIN_NUMBER` → `bin_number`
- `oaseslive.random_stock_check_bins.BIN_NUMBER` → `bin_number`
- `oaseslive.rotable_batch_locations.bin_number` → `bin_number`
- `oaseslive.stock_audit_batches.BIN_NUMBER` → `bin_number`
- `oaseslive.stock_audit_bins.BIN_NUMBER` → `bin_number`
- `oaseslive.stock_by_bin.BIN_NUMBER` → `bin_number`

### oaseslive.bkp_mobile_permissions

**References (Outgoing):**

- `PERMISSION_ID` → `oaseslive.add_extension_permissions.USER_ID`

**Referenced By (Incoming):**

- `oaseslive.account_buying_contacts.mobile_number` → `OASES_SECURITY_TOKEN`

### oaseslive.block_countries

**References (Outgoing):**

- `block_code` → `oaseslive.block_countries.block_code`

**Referenced By (Incoming):**

- `oaseslive.block_countries.block_code` → `block_code`
- `oaseslive.economic_blocks.block_code` → `block_code`
- `oaseslive.order_standard_text_blocks.BLOCK_NUMBER` → `block_code`
- `oaseslive.rp_block_resource.BLOCK_ID` → `block_code`
- `oaseslive.rp_block_resource_days.BLOCK_ID` → `block_code`

### oaseslive.bulk_batch_header

**References (Outgoing):**

- `BULK_BATCH_NUMBER` → `oaseslive.bulk_batch_header.BULK_BATCH_NUMBER`

**Referenced By (Incoming):**

- `oaseslive.bulk_batch_header.BULK_BATCH_NUMBER` → `BULK_BATCH_NUMBER`

### oaseslive.cfd_categories

**Referenced By (Incoming):**

- `oaseslive.requirements.cfd_number` → `cfd_category`

### oaseslive.cfd_categorires_bkpoases405

**Referenced By (Incoming):**

- `oaseslive.oeim_invoice_snap_users.OASES_ID` → `CFD_CATEGORY`

### oaseslive.cfd_xref_to_tech_log

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.company_codes

**References (Outgoing):**

- `COMPANY_CODE` → `oaseslive.company_codes.COMPANY_CODE`

**Referenced By (Incoming):**

- `oaseslive.company_codes.COMPANY_CODE` → `COMPANY_CODE`
- `oaseslive.company_form_details.COMPANY_CODE` → `COMPANY_CODE`
- `oaseslive.delivery_note_header_1.COMPANY_CODE` → `COMPANY_CODE`
- `oaseslive.order_header_1.company_code` → `COMPANY_CODE`
- `oaseslive.preorders.COMPANY_CODE` → `COMPANY_CODE`
- `oaseslive.sales_orders.COMPANY_CODE` → `COMPANY_CODE`
- `oaseslive.sales_request_quote_header.COMPANY_CODE` → `COMPANY_CODE`
- `oaseslive.shipment.COMPANY_CODE` → `COMPANY_CODE`

### oaseslive.company_form_attachments

**References (Outgoing):**

- `ATTACHMENT_ID` → `oaseslive.company_form_attachments.ATTACHMENT_ID`
- `COMPANY_FORM_ID` → `oaseslive.company_form_attachments.ATTACHMENT_ID`

**Referenced By (Incoming):**

- `oaseslive.company_form_attachments.ATTACHMENT_ID` → `ATTACHMENT_ID`
- `oaseslive.company_form_attachments.COMPANY_FORM_ID` → `ATTACHMENT_ID`
- `oaseslive.company_form_details.COMPANY_FORM_ID` → `ATTACHMENT_ID`
- `oaseslive.company_form_details.FORM_NUMBER` → `ATTACHMENT_ID`
- `oaseslive.form_number.FORM_NUMBER` → `ATTACHMENT_ID`

### oaseslive.company_form_details

**References (Outgoing):**

- `COMPANY_CODE` → `oaseslive.company_codes.COMPANY_CODE`
- `COMPANY_FORM_ID` → `oaseslive.company_form_attachments.ATTACHMENT_ID`
- `FORM_NUMBER` → `oaseslive.company_form_attachments.ATTACHMENT_ID`

### oaseslive.completion_fleet_ata_pos

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.completion_life_values

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `LIFE_CODE_LEVEL_ID` → `oaseslive.life_code_levels.life_code_level_id`

### oaseslive.completion_maint_mod

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `REPORT_ID` → `oaseslive.amp_report_documents.FLEET`

### oaseslive.completion_part_serial

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`

**Referenced By (Incoming):**

- `oaseslive.accomp_bkup.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.accomp_hist_delta_1763.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.accomp_hist_lost_sched.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.accomplishment_history.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.aircraft_build.serial_number` → `PART_NUMBER`
- `oaseslive.aircraft_leased_apu.serial_number` → `PART_NUMBER`
- `oaseslive.aircraft_leased_engines.serial_number` → `PART_NUMBER`
- `oaseslive.aircraft_leased_landing_gear.serial_number` → `PART_NUMBER`
- `oaseslive.aircraft_leased_propellers.serial_number` → `PART_NUMBER`
- `oaseslive.aircraft_major_checks.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.amp_component_intervals.serial_number` → `PART_NUMBER`
- `oaseslive.amp_datmig_accomplishments.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.amp_datmig_llp.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.batch_notes.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.batch_notes_gu4240.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.batch_record_1.serial_number` → `PART_NUMBER`
- `oaseslive.batch_record_1_gu4240.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.completion_life_values.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.completion_part_serial.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.component_life.serial_number` → `PART_NUMBER`
- `oaseslive.component_movement_hist_life.serial_number` → `PART_NUMBER`
- `oaseslive.component_movement_history.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.component_movement_history_ext.serial_number` → `PART_NUMBER`
- `oaseslive.component_movt_hist_ext_8661.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.components.serial_number` → `PART_NUMBER`
- `oaseslive.components_bkp_dj95.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.components_bkp_dj97.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.components_oases971.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.credit_works_order_cards.serial_number` → `PART_NUMBER`
- `oaseslive.daily_loans_out.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.dmg_rpr_damage.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.dmg_rpr_fitted_locations.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.drn_component_mods_history.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.drn_components_nsbl_history.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.drn_life_limits.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.drn_part_serial.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.dues_register.serial_number` → `PART_NUMBER`
- `oaseslive.fleet_forecast_plans_drn.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.ie96_historic.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.inherited_acquisition_costs.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.invoice_trail_entries.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.latest_repair_values.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.loaned_units.serial_number` → `PART_NUMBER`
- `oaseslive.long_serial_number_xref.serial_number` → `PART_NUMBER`
- `oaseslive.maint_material_costs.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.monthly_loans_in.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.monthly_loans_out.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.oeim_credit_warranty.serial_number` → `PART_NUMBER`
- `oaseslive.oeim_invoice_materials.serial_number` → `PART_NUMBER`
- `oaseslive.oeim_invoice_snap_serl_master.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.oeim_invoice_warranty.serial_number` → `PART_NUMBER`
- `oaseslive.oeim_invoice_warranty_refunds.serial_number` → `PART_NUMBER`
- `oaseslive.order_history.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.original_purchase_values.serial_number` → `PART_NUMBER`
- `oaseslive.part_number_properties_serials.serial_number` → `PART_NUMBER`
- `oaseslive.part_serial_documents.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.pick_hist_7890_bkp.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.pick_history.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.planners_notes_xref.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.preorder_line_stock_info.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.rfc_components.serial_number` → `PART_NUMBER`
- `oaseslive.rotable_batch_locations.serial_number` → `PART_NUMBER`
- `oaseslive.rotable_history.serial_number` → `PART_NUMBER`
- `oaseslive.sales_history.serial_number` → `PART_NUMBER`
- `oaseslive.sales_order_dispatches.serial_number` → `PART_NUMBER`
- `oaseslive.schedule_forecast_xref.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.schedule_source.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.serial_numbers_by_part.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.shelf_li_dt_bkp_2020.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.shelf_life_dates.serial_number` → `PART_NUMBER`
- `oaseslive.shelf_life_dates_oases6834.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.shipment_demands.serial_number` → `PART_NUMBER`
- `oaseslive.shipment_item.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.strip_report_header_1.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.task_activity_link.SERIAL_NUMBER` → `PART_NUMBER`
- `oaseslive.units_of_measure.serial_number` → `PART_NUMBER`

### oaseslive.component_life

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `life_code_level_id` → `oaseslive.life_code_levels.life_code_level_id`

### oaseslive.component_life_limits

**References (Outgoing):**

- `component_life_limit_id` → `oaseslive.component_life_limits.component_life_limit_id`

**Referenced By (Incoming):**

- `oaseslive.amp_component_intervals.component_life_limit_id` → `component_life_limit_id`
- `oaseslive.amp_component_reset_on_compl.COMPONENT_LIFE_LIMIT_ID` → `component_life_limit_id`
- `oaseslive.component_life_limits.component_life_limit_id` → `component_life_limit_id`
- `oaseslive.component_movement_history_ext.component_life_limit_id` → `component_life_limit_id`
- `oaseslive.component_movt_hist_ext_8661.COMPONENT_LIFE_LIMIT_ID` → `component_life_limit_id`
- `oaseslive.forecast_cache.COMPONENT_LIFE_LIMIT_ID` → `component_life_limit_id`
- `oaseslive.part_number_shelf_life_details.COMPONENT_LIFE_LIMIT_ID` → `component_life_limit_id`
- `oaseslive.shelf_li_dt_bkp_2020.COMPONENT_LIFE_LIMIT_ID` → `component_life_limit_id`
- `oaseslive.shelf_life_dates.component_life_limit_id` → `component_life_limit_id`
- `oaseslive.shelf_life_dates_oases6834.COMPONENT_LIFE_LIMIT_ID` → `component_life_limit_id`
- `oaseslive.units_of_measure.component_life_limit_id` → `component_life_limit_id`

### oaseslive.component_mods_history_by_part

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.component_movement_hist_life

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `history_id` → `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `life_code_level_id` → `oaseslive.life_code_levels.life_code_level_id`

**Referenced By (Incoming):**

- `oaseslive.consumable_history.movement_code` → `part_number`
- `oaseslive.demand_reason_to_movement_code.MOVEMENT_CODE` → `part_number`
- `oaseslive.movement_codes.movement_code` → `part_number`
- `oaseslive.order_lines.movement_code` → `part_number`
- `oaseslive.preorder_line_stock_info.MOVEMENT_CODE` → `part_number`
- `oaseslive.repair_approval_data.MOVEMENT_CODE` → `part_number`
- `oaseslive.requests_for_quotes_lines.MOVEMENT_CODE` → `part_number`
- `oaseslive.rotable_batch_locations.movement_code` → `part_number`
- `oaseslive.rotable_history.movement_code` → `part_number`

### oaseslive.component_movement_history

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.component_movement_history_ext

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `history_id` → `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID`
- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `report_id` → `oaseslive.amp_report_documents.FLEET`
- `batch_number` → `oaseslive.batch_file_header.KEY`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `component_life_limit_id` → `oaseslive.component_life_limits.component_life_limit_id`

### oaseslive.component_movt_hist_ext_8661

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `HISTORY_ID` → `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID`
- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `REPORT_ID` → `oaseslive.amp_report_documents.FLEET`
- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `COMPONENT_LIFE_LIMIT_ID` → `oaseslive.component_life_limits.component_life_limit_id`

### oaseslive.components

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.components_bkp_dj95

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.components_bkp_dj97

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.components_oases971

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.condition_codes

**References (Outgoing):**

- `condition_code` → `oaseslive.condition_codes.condition_code`

**Referenced By (Incoming):**

- `oaseslive.condition_codes.condition_code` → `condition_code`
- `oaseslive.order_history.CONDITION_CODE` → `condition_code`
- `oaseslive.order_line_additional_info.CONDITION_CODE` → `condition_code`
- `oaseslive.preorder_lines.CONDITION_CODE` → `condition_code`
- `oaseslive.rfq_history.condition_code` → `condition_code`
- `oaseslive.sales_history.condition_code` → `condition_code`
- `oaseslive.sales_prices.condition_code` → `condition_code`
- `oaseslive.sales_quotes_out_history.CONDITION_CODE` → `condition_code`

### oaseslive.condition_pick_table

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `WAREHOUSE_CODE` → `oaseslive.account_available_warehouses.ACCOUNT_CODE`
- `PICK_NUMBER` → `oaseslive.condition_pick_table.PART_NUMBER`
- `REQUIREMENT_NUMBER` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`

**Referenced By (Incoming):**

- `oaseslive.condition_pick_table.PICK_NUMBER` → `PART_NUMBER`
- `oaseslive.delivery_note_item_header_2.pick_number` → `PART_NUMBER`
- `oaseslive.part_xref_to_pick_history.PICK_NUMBER` → `PART_NUMBER`
- `oaseslive.pick_hist_7890_bkp.PICK_NUMBER` → `PART_NUMBER`
- `oaseslive.pick_history.PICK_NUMBER` → `PART_NUMBER`
- `oaseslive.shipment_requirement_demands.pick_number` → `PART_NUMBER`

### oaseslive.consumable_batch_locations

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `oaseslive.batch_file_header.KEY`

### oaseslive.consumable_history

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `approval_code` → `oaseslive.account_supplier_approvals.account_code`
- `batch_number` → `oaseslive.batch_file_header.KEY`
- `order_number` → `oaseslive.batch_orders.BATCH_NUMBER`
- `movement_code` → `oaseslive.component_movement_hist_life.part_number`
- `requirement_number` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`
- `authority_code` → `oaseslive.rfc_regulating_authority.authority_code`

**Referenced By (Incoming):**

- `oaseslive.shipment_demands.consumable_history_id` → `id`

### oaseslive.consumable_repair_xref_to_part

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_permanent_repairs.REPAIR_ID` → `PART_NUMBER`

### oaseslive.consumables_below_re_order

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.contacts_xref

**References (Outgoing):**

- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`

### oaseslive.continents

**References (Outgoing):**

- `continent_id` → `oaseslive.continents.continent_id`

**Referenced By (Incoming):**

- `oaseslive.continents.continent_id` → `continent_id`
- `oaseslive.countries.continent_id` → `continent_id`

### oaseslive.corrosion_categories

**References (Outgoing):**

- `corrosion_code` → `oaseslive.corrosion_categories.corrosion_code`

**Referenced By (Incoming):**

- `oaseslive.corrosion_categories.corrosion_code` → `corrosion_code`
- `oaseslive.nrc_defect_details.corrosion_code` → `corrosion_code`
- `oaseslive.tech_log_3.corrosion_code` → `corrosion_code`

### oaseslive.cost_codes

**References (Outgoing):**

- `cost_code` → `oaseslive.cost_codes.id`

**Referenced By (Incoming):**

- `oaseslive.cost_codes.cost_code` → `id`
- `oaseslive.cq_fixed_charge_xref.cost_code` → `id`
- `oaseslive.cq_quote_cards.cost_code` → `id`
- `oaseslive.cq_quote_nrcs.cost_code` → `id`
- `oaseslive.cq_quote_packages.cost_code` → `id`
- `oaseslive.customer_contract_rates.cost_code` → `id`
- `oaseslive.customer_contract_stop_incl.cost_code` → `id`
- `oaseslive.default_labour_rates.cost_code` → `id`
- `oaseslive.fixed_charges.cost_code` → `id`
- `oaseslive.maint_cost_budget_workcards.COST_CODE` → `id`
- `oaseslive.maint_cost_hourly_rates.COST_CODE` → `id`
- `oaseslive.maintenance_cost_entry.COST_ID` → `id`
- `oaseslive.maintenance_cost_types.COST_ID` → `id`
- `oaseslive.mandatory_parts.COST_CODE` → `id`
- `oaseslive.oeim_invoice_fixed_charges.cost_code` → `id`
- `oaseslive.oeim_invoice_packages.cost_code` → `id`
- `oaseslive.oeim_invoice_snap_con_rates.COST_CODE` → `id`
- `oaseslive.oeim_invoice_snap_cost_codes.COST_CODE` → `id`
- `oaseslive.requirement_recharge_details.COST_CODE` → `id`

### oaseslive.countries

**References (Outgoing):**

- `continent_id` → `oaseslive.continents.continent_id`

### oaseslive.cq_documents

**References (Outgoing):**

- `QUOTE_ID` → `oaseslive.cq_quote_cards.quote_id`
- `DOCUMENT_IMAGE_ID` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`

### oaseslive.cq_fixed_charge_xref

**References (Outgoing):**

- `cost_code` → `oaseslive.cost_codes.id`
- `fixed_charge_id` → `oaseslive.cq_fixed_charge_xref.quote_id`
- `quote_id` → `oaseslive.cq_quote_cards.quote_id`

**Referenced By (Incoming):**

- `oaseslive.cq_fixed_charge_xref.fixed_charge_id` → `quote_id`

### oaseslive.cq_quote_cards

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `package_code` → `oaseslive.amp_package_notes.fleet`
- `cost_code` → `oaseslive.cost_codes.id`
- `quote_id` → `oaseslive.cq_quote_cards.quote_id`

**Referenced By (Incoming):**

- `oaseslive.cq_documents.QUOTE_ID` → `quote_id`
- `oaseslive.cq_fixed_charge_xref.quote_id` → `quote_id`
- `oaseslive.cq_quote_cards.quote_id` → `quote_id`
- `oaseslive.cq_quote_materials.quote_id` → `quote_id`
- `oaseslive.cq_quote_nrc_access_panels.QUOTE_ID` → `quote_id`
- `oaseslive.cq_quote_nrcs.quote_id` → `quote_id`
- `oaseslive.cq_quote_packages.quote_id` → `quote_id`
- `oaseslive.cq_quotes.quote_id` → `quote_id`
- `oaseslive.maint_cost_mro_wo_quotes.QUOTE_ID` → `quote_id`
- `oaseslive.maintenance_cost_quotes.QUOTE_ID` → `quote_id`

### oaseslive.cq_quote_materials

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `quote_id` → `oaseslive.cq_quote_cards.quote_id`

### oaseslive.cq_quote_nrc_access_panels

**References (Outgoing):**

- `ACCESS_PANEL_CODE` → `oaseslive.amp_access_panel_desc_hdr.fleet`
- `QUOTE_ID` → `oaseslive.cq_quote_cards.quote_id`
- `QUOTE_NRC_ID` → `oaseslive.cq_quote_nrc_access_panels.QUOTE_ID`

**Referenced By (Incoming):**

- `oaseslive.cq_quote_nrc_access_panels.QUOTE_NRC_ID` → `QUOTE_ID`
- `oaseslive.cq_quote_nrcs.quote_nrc_id` → `QUOTE_ID`
- `oaseslive.esign_off_nrc.NRC_NUMBER` → `QUOTE_ID`
- `oaseslive.maint_nrc_costs.NRC_NUMBER` → `QUOTE_ID`
- `oaseslive.nrc_access_panels.nrc_number` → `QUOTE_ID`
- `oaseslive.nrc_documents.nrc_number` → `QUOTE_ID`
- `oaseslive.nrc_materials.nrc_number` → `QUOTE_ID`
- `oaseslive.nrc_properties.NRC_NUMBER` → `QUOTE_ID`
- `oaseslive.nrc_tools.nrc_number` → `QUOTE_ID`
- `oaseslive.nrc_workcard_narrative.NRC_NUMBER` → `QUOTE_ID`
- `oaseslive.nrc_xref_to_scheduled_workcard.NRC_NUMBER` → `QUOTE_ID`
- `oaseslive.rdi_to_nrc.NRC_NUMBER` → `QUOTE_ID`
- `oaseslive.rp_employee_allocation.NRC_NUMBER` → `QUOTE_ID`
- `oaseslive.rp_wo_base_nrc_plan.NRC_NUMBER` → `QUOTE_ID`
- `oaseslive.rp_wo_nrc_plan.nrc_number` → `QUOTE_ID`

### oaseslive.cq_quote_nrcs

**References (Outgoing):**

- `cost_code` → `oaseslive.cost_codes.id`
- `quote_id` → `oaseslive.cq_quote_cards.quote_id`
- `quote_nrc_id` → `oaseslive.cq_quote_nrc_access_panels.QUOTE_ID`

### oaseslive.cq_quote_packages

**References (Outgoing):**

- `package_code` → `oaseslive.amp_package_notes.fleet`
- `cost_code` → `oaseslive.cost_codes.id`
- `quote_id` → `oaseslive.cq_quote_cards.quote_id`

### oaseslive.cq_quote_status

**References (Outgoing):**

- `status_id` → `oaseslive.amp_revision_status.REVISION_STATUS_ID`
- `policy_id` → `oaseslive.security_policy.POLICY_ID`

### oaseslive.cq_quote_status_contacts

**References (Outgoing):**

- `STATUS_ID` → `oaseslive.amp_revision_status.REVISION_STATUS_ID`

### oaseslive.cq_quotes

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `quote_id` → `oaseslive.cq_quote_cards.quote_id`

### oaseslive.credit_works_order_cards

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `oaseslive.batch_file_header.KEY`
- `order_number` → `oaseslive.batch_orders.BATCH_NUMBER`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `requirement_number` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`

**Referenced By (Incoming):**

- `oaseslive.bar_codes.WORKS_ORDER_NUMBER` → `credit_note_no`
- `oaseslive.forecast_cache.WORKS_ORDER_NUMBER` → `credit_note_no`
- `oaseslive.order_header_2.WORKS_ORDER_NUMBER` → `credit_note_no`
- `oaseslive.stock_works_order_markups.WORKS_ORDER_NUMBER` → `credit_note_no`
- `oaseslive.strip_report_header_1.WORKS_ORDER_NUMBER` → `credit_note_no`

### oaseslive.credit_works_orders

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`

### oaseslive.crs_signature_text

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `CRS_TEXT_ID` → `oaseslive.crs_text.CRS_TEXT_ID`

### oaseslive.crs_text

**References (Outgoing):**

- `CRS_TEXT_ID` → `oaseslive.crs_text.CRS_TEXT_ID`

**Referenced By (Incoming):**

- `oaseslive.crs_signature_text.CRS_TEXT_ID` → `CRS_TEXT_ID`
- `oaseslive.crs_text.CRS_TEXT_ID` → `CRS_TEXT_ID`

### oaseslive.currency_codes

**References (Outgoing):**

- `currency_code` → `oaseslive.currency_codes.currency_code`

**Referenced By (Incoming):**

- `oaseslive.account_location_header_5.currency_code` → `currency_code`
- `oaseslive.batch_record_1.currency_code` → `currency_code`
- `oaseslive.batch_record_1_gu4240.CURRENCY_CODE` → `currency_code`
- `oaseslive.batch_record_2.CURRENCY_CODE` → `currency_code`
- `oaseslive.currency_codes.currency_code` → `currency_code`
- `oaseslive.invoice_lines.CURRENCY_CODE` → `currency_code`
- `oaseslive.invoice_trail_entries.CURRENCY_CODE` → `currency_code`
- `oaseslive.invoices.CURRENCY_CODE` → `currency_code`
- `oaseslive.latest_repair_values.CURRENCY_CODE` → `currency_code`
- `oaseslive.maint_associated_costs.CURRENCY_CODE` → `currency_code`
- `oaseslive.maintenance_cost_invoices.CURRENCY_CODE` → `currency_code`
- `oaseslive.maintenance_cost_quotes.CURRENCY_CODE` → `currency_code`
- `oaseslive.material_pool_agreement.CURRENCY_CODE` → `currency_code`
- `oaseslive.oeim_invoice_snap_currencies.CURRENCY_CODE` → `currency_code`
- `oaseslive.order_goods_received_invoices.CURRENCY_CODE` → `currency_code`
- `oaseslive.order_header_1.currency_code` → `currency_code`
- `oaseslive.order_history.CURRENCY_CODE` → `currency_code`
- `oaseslive.order_line_quotes_data.CURRENCY_CODE` → `currency_code`
- `oaseslive.original_purchase_values.currency_code` → `currency_code`
- `oaseslive.preorders.CURRENCY_CODE` → `currency_code`
- `oaseslive.quotes_by_part.CURRENCY_CODE` → `currency_code`
- `oaseslive.requirement_recharge_details.CURRENCY_CODE` → `currency_code`
- `oaseslive.rfq_history.currency_code` → `currency_code`
- `oaseslive.rfq_quote_received.CURRENCY_CODE` → `currency_code`
- `oaseslive.sales_history.currency_code` → `currency_code`
- `oaseslive.sales_orders.CURRENCY_CODE` → `currency_code`
- `oaseslive.sales_prices.currency_code` → `currency_code`
- `oaseslive.sales_quotes_out_history.CURRENCY_CODE` → `currency_code`
- `oaseslive.sales_request_quote_header.CURRENCY_CODE` → `currency_code`
- `oaseslive.shipment.CURRENCY_CODE` → `currency_code`
- `oaseslive.strip_report_header_1.CURRENCY_CODE` → `currency_code`

### oaseslive.customer_contract_rates

**References (Outgoing):**

- `cost_code` → `oaseslive.cost_codes.id`
- `contract_id` → `oaseslive.customer_contract_rates.contract_id`
- `time_category_id` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

**Referenced By (Incoming):**

- `oaseslive.access_dim_sales_info.CUSTOMER_CODE` → `contract_id`
- `oaseslive.account_location_header_9.customer_number` → `contract_id`
- `oaseslive.customer_contract_rates.contract_id` → `contract_id`
- `oaseslive.customer_contract_stop_incl.contract_id` → `contract_id`
- `oaseslive.customer_contracts.contract_id` → `contract_id`
- `oaseslive.maint_cost_time_categories.CONTRACT_ID` → `contract_id`
- `oaseslive.time_categories.contract_id` → `contract_id`

### oaseslive.customer_contract_stop_incl

**References (Outgoing):**

- `cost_code` → `oaseslive.cost_codes.id`
- `contract_id` → `oaseslive.customer_contract_rates.contract_id`
- `time_category_id` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

### oaseslive.customer_contracts

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `contract_id` → `oaseslive.customer_contract_rates.contract_id`
- `markup_code` → `oaseslive.freight_cost_markups.FREIGHT_COST_MARKUP_ID`

### oaseslive.customer_sales_order_xref

**References (Outgoing):**

- `CUSTOMER_SALES_ORDER_NUMBER` → `oaseslive.customer_sales_order_xref.CUSTOMER_SALES_ORDER_NUMBER`
- `SALES_ORDER_NUMBER` → `oaseslive.customer_sales_order_xref.CUSTOMER_SALES_ORDER_NUMBER`

**Referenced By (Incoming):**

- `oaseslive.access_dim_sales_info.SALES_ORDER_NUMBER` → `CUSTOMER_SALES_ORDER_NUMBER`
- `oaseslive.customer_sales_order_xref.CUSTOMER_SALES_ORDER_NUMBER` → `CUSTOMER_SALES_ORDER_NUMBER`
- `oaseslive.customer_sales_order_xref.SALES_ORDER_NUMBER` → `CUSTOMER_SALES_ORDER_NUMBER`
- `oaseslive.requirements.sales_order_number` → `CUSTOMER_SALES_ORDER_NUMBER`
- `oaseslive.sales_invoices_xref.SALES_ORDER_NUMBER` → `CUSTOMER_SALES_ORDER_NUMBER`
- `oaseslive.sales_order_dispatches.sales_order_number` → `CUSTOMER_SALES_ORDER_NUMBER`
- `oaseslive.sales_order_lines.sales_order_number` → `CUSTOMER_SALES_ORDER_NUMBER`
- `oaseslive.sales_order_notes.SALES_ORDER_NUMBER` → `CUSTOMER_SALES_ORDER_NUMBER`
- `oaseslive.sales_order_payments.SALES_ORDER_NUMBER` → `CUSTOMER_SALES_ORDER_NUMBER`
- `oaseslive.sales_orders.SALES_ORDER_NUMBER` → `CUSTOMER_SALES_ORDER_NUMBER`
- `oaseslive.sales_orders_by_part.SALES_ORDER_NUMBER` → `CUSTOMER_SALES_ORDER_NUMBER`
- `oaseslive.sales_request_quote_detail.sales_order_number` → `CUSTOMER_SALES_ORDER_NUMBER`

### oaseslive.customs_status_codes

**References (Outgoing):**

- `reference_number` → `oaseslive.accounts_references.accounts_reference`

**Referenced By (Incoming):**

- `oaseslive.shipment_item_customs.CUSTOMS_STATUS_CODE` → `customs_status`

### oaseslive.customs_tariff_codes

**References (Outgoing):**

- `customs_tariff_code` → `oaseslive.customs_tariff_codes.customs_tariff_code`

**Referenced By (Incoming):**

- `oaseslive.customs_tariff_codes.customs_tariff_code` → `customs_tariff_code`
- `oaseslive.customs_tariff_codes_territory.CUSTOMS_TARIFF_CODE` → `customs_tariff_code`
- `oaseslive.part_customs_tariff_territory.CUSTOMS_TARIFF_CODE` → `customs_tariff_code`
- `oaseslive.parts_customs_tariff_codes.CUSTOMS_TARIFF_CODE` → `customs_tariff_code`

### oaseslive.customs_tariff_codes_territory

**References (Outgoing):**

- `CUSTOMS_TARIFF_CODE` → `oaseslive.customs_tariff_codes.customs_tariff_code`

### oaseslive.daily_loans_out

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.dataset_locks_by_lock_type

**References (Outgoing):**

- `USER_ID` → `oaseslive.dataset_locks_by_user.USER_ID`

### oaseslive.dataset_locks_by_user

**References (Outgoing):**

- `USER_ID` → `oaseslive.dataset_locks_by_user.USER_ID`

**Referenced By (Incoming):**

- `oaseslive.add_extension_permissions.USER_ID` → `USER_ID`
- `oaseslive.amp_revision_history.USER_ID` → `USER_ID`
- `oaseslive.amp_revisions.user_id` → `USER_ID`
- `oaseslive.amp_workcards_by_section.user_id` → `USER_ID`
- `oaseslive.audit_trail.USER_ID` → `USER_ID`
- `oaseslive.batch_history.USER_ID` → `USER_ID`
- `oaseslive.dataset_locks_by_lock_type.USER_ID` → `USER_ID`
- `oaseslive.dataset_locks_by_user.USER_ID` → `USER_ID`
- `oaseslive.float_history.USER_ID` → `USER_ID`
- `oaseslive.mel_revision_history.USER_ID` → `USER_ID`
- `oaseslive.mel_revisions.user_id` → `USER_ID`
- `oaseslive.part_number_amendment_history.USER_ID` → `USER_ID`
- `oaseslive.rdi_history.USER_ID` → `USER_ID`
- `oaseslive.repetitive_defect_narrative.USER_ID` → `USER_ID`
- `oaseslive.sales_order_payments.USER_ID` → `USER_ID`
- `oaseslive.sales_request_quote_header.USER_ID` → `USER_ID`

### oaseslive.default_labour_rates

**References (Outgoing):**

- `cost_code` → `oaseslive.cost_codes.id`
- `window_id` → `oaseslive.default_labour_windows.window_id`
- `time_category_id` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

### oaseslive.default_labour_windows

**References (Outgoing):**

- `window_id` → `oaseslive.default_labour_windows.window_id`

**Referenced By (Incoming):**

- `oaseslive.default_labour_rates.window_id` → `window_id`
- `oaseslive.default_labour_windows.window_id` → `window_id`

### oaseslive.defect_extensions

**References (Outgoing):**

- `EXTENSION_ID` → `oaseslive.add_extension_permissions.USER_ID`
- `DEFECT_ID` → `oaseslive.defect_extensions.DEFECT_ID`

**Referenced By (Incoming):**

- `oaseslive.defect_extensions.DEFECT_ID` → `DEFECT_ID`
- `oaseslive.defect_stage_employees.defect_id` → `DEFECT_ID`
- `oaseslive.engineering_support_history.DEFECT_NUMBER` → `DEFECT_ID`
- `oaseslive.maint_historic_defects.DEFECT_ID` → `DEFECT_ID`
- `oaseslive.nrc_defect_details.defect_id` → `DEFECT_ID`
- `oaseslive.nrc_defect_notes.DEFECT_NUMBER` → `DEFECT_ID`
- `oaseslive.nrc_print_history.DEFECT_NUMBER` → `DEFECT_ID`
- `oaseslive.nrc_rectification_notes.DEFECT_NUMBER` → `DEFECT_ID`
- `oaseslive.nrc_requirements_actions.defect_number` → `DEFECT_ID`
- `oaseslive.nrc_status_history.DEFECT_NUMBER` → `DEFECT_ID`
- `oaseslive.nrc_xref_to_scheduled_workcard.DEFECT_NUMBER` → `DEFECT_ID`
- `oaseslive.oeim_invoice_snap_sfdc_book.DEFECT_CODE` → `DEFECT_ID`
- `oaseslive.osys_defect_act_to_defect_id.DEFECT_ID` → `DEFECT_ID`
- `oaseslive.osys_defect_to_defect_id.DEFECT_NUMBER` → `DEFECT_ID`
- `oaseslive.osys_defect_to_defect_id.DEFECT_ID` → `DEFECT_ID`
- `oaseslive.osys_defect_to_tech_log_line.DEFECT_NUMBER` → `DEFECT_ID`
- `oaseslive.requirements.defect_number` → `DEFECT_ID`
- `oaseslive.requirements.defect_id` → `DEFECT_ID`
- `oaseslive.sfdc_bookings.DEFECT_CODE` → `DEFECT_ID`
- `oaseslive.sfdc_deleted_bookings.DEFECT_CODE` → `DEFECT_ID`
- `oaseslive.sfdc_open_bookings.DEFECT_CODE` → `DEFECT_ID`
- `oaseslive.sold_hours_history.DEFECT_NUMBER` → `DEFECT_ID`
- `oaseslive.structural_damage.defect_number` → `DEFECT_ID`
- `oaseslive.tech_log_3.defect_id` → `DEFECT_ID`

### oaseslive.defect_maint_stages

**References (Outgoing):**

- `defect_stage_id` → `oaseslive.defect_stage_employees.defect_id`

### oaseslive.defect_stage_employees

**References (Outgoing):**

- `defect_id` → `oaseslive.defect_extensions.DEFECT_ID`
- `defect_stage_id` → `oaseslive.defect_stage_employees.defect_id`
- `employee_id` → `oaseslive.defect_stage_employees.defect_id`
- `licence_id` → `oaseslive.email_licence.LICENSE_ID`

**Referenced By (Incoming):**

- `oaseslive.defect_maint_stages.defect_stage_id` → `defect_id`
- `oaseslive.defect_stage_employees.defect_stage_id` → `defect_id`
- `oaseslive.defect_stage_employees.employee_id` → `defect_id`
- `oaseslive.employee_experience_details.EMPLOYEE_NUMBER` → `defect_id`
- `oaseslive.employee_presence.EMPLOYEE_NUMBER` → `defect_id`
- `oaseslive.employee_presence_log.EMPLOYEE_NUMBER` → `defect_id`
- `oaseslive.employee_training_details.EMPLOYEE_NUMBER` → `defect_id`
- `oaseslive.employees.employee_number` → `defect_id`
- `oaseslive.employees_licences.employee_number` → `defect_id`
- `oaseslive.oeim_invoice_snap_employees.EMPLOYEE_NUMBER` → `defect_id`
- `oaseslive.oeim_invoice_snap_sfdc_book.EMPLOYEE_NUMBER` → `defect_id`
- `oaseslive.order_header_4.EMPLOYEE_NUMBER` → `defect_id`
- `oaseslive.preorders.EMPLOYEE_NUMBER` → `defect_id`
- `oaseslive.rp_employee_allocation_header.EMPLOYEE_NUMBER` → `defect_id`
- `oaseslive.rp_employee_calendar_addition.employee_number` → `defect_id`
- `oaseslive.rp_employee_calendar_pattern.employee_number` → `defect_id`
- `oaseslive.sfdc_activity.DEFECT_STAGE_ID` → `defect_id`
- `oaseslive.sfdc_bookings.EMPLOYEE_NUMBER` → `defect_id`
- `oaseslive.sfdc_deleted_bookings.EMPLOYEE_NUMBER` → `defect_id`
- `oaseslive.sfdc_open_bookings.EMPLOYEE_NUMBER` → `defect_id`
- `oaseslive.tool_check_out_in.employee_number` → `defect_id`

### oaseslive.deferred_defect_xref_to_cfd_no

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.delay_codes

**References (Outgoing):**

- `delay_code_id` → `oaseslive.delay_codes.delay_code_id`
- `delay_code` → `oaseslive.delay_codes.delay_code_id`

**Referenced By (Incoming):**

- `oaseslive.delay_codes.delay_code_id` → `delay_code_id`
- `oaseslive.delay_codes.delay_code` → `delay_code_id`
- `oaseslive.delays.delay_id` → `delay_code_id`
- `oaseslive.delays.delay_code_id` → `delay_code_id`

### oaseslive.delays

**References (Outgoing):**

- `report_id` → `oaseslive.amp_report_documents.FLEET`
- `delay_id` → `oaseslive.delay_codes.delay_code_id`
- `delay_code_id` → `oaseslive.delay_codes.delay_code_id`

### oaseslive.delivery_note_extended_remarks

**References (Outgoing):**

- `DELIVERY_NOTE_NUMBER` → `oaseslive.delivery_note_extended_remarks.DELIVERY_NOTE_NUMBER`

**Referenced By (Incoming):**

- `oaseslive.airway_bill_references.DELIVERY_NOTE_NUMBER` → `DELIVERY_NOTE_NUMBER`
- `oaseslive.delivery_note_extended_remarks.DELIVERY_NOTE_NUMBER` → `DELIVERY_NOTE_NUMBER`
- `oaseslive.delivery_note_header_1.DELIVERY_NOTE_NUMBER` → `DELIVERY_NOTE_NUMBER`
- `oaseslive.delivery_note_header_2.DELIVERY_NOTE_NUMBER` → `DELIVERY_NOTE_NUMBER`
- `oaseslive.delivery_note_header_3.DELIVERY_NOTE_NUMBER` → `DELIVERY_NOTE_NUMBER`
- `oaseslive.delivery_note_header_4.DELIVERY_NOTE_NUMBER` → `DELIVERY_NOTE_NUMBER`
- `oaseslive.delivery_note_item_header_1.delivery_note_number` → `DELIVERY_NOTE_NUMBER`
- `oaseslive.delivery_note_item_header_2.delivery_note_number` → `DELIVERY_NOTE_NUMBER`
- `oaseslive.delivery_note_master_list.DELIVERY_NOTE_NUMBER` → `DELIVERY_NOTE_NUMBER`
- `oaseslive.monthly_loans_out.DELIVERY_NOTE_NUMBER` → `DELIVERY_NOTE_NUMBER`
- `oaseslive.order_header_3.DELIVERY_NOTE_NUMBER` → `DELIVERY_NOTE_NUMBER`
- `oaseslive.rotable_history.delivery_note_number` → `DELIVERY_NOTE_NUMBER`
- `oaseslive.sales_order_dispatches.delivery_note_number` → `DELIVERY_NOTE_NUMBER`

### oaseslive.delivery_note_header_1

**References (Outgoing):**

- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `COMPANY_CODE` → `oaseslive.company_codes.COMPANY_CODE`
- `DELIVERY_NOTE_NUMBER` → `oaseslive.delivery_note_extended_remarks.DELIVERY_NOTE_NUMBER`

### oaseslive.delivery_note_header_2

**References (Outgoing):**

- `DELIVERY_NOTE_NUMBER` → `oaseslive.delivery_note_extended_remarks.DELIVERY_NOTE_NUMBER`

### oaseslive.delivery_note_header_3

**References (Outgoing):**

- `DELIVERY_NOTE_NUMBER` → `oaseslive.delivery_note_extended_remarks.DELIVERY_NOTE_NUMBER`

### oaseslive.delivery_note_header_4

**References (Outgoing):**

- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `DELIVERY_NOTE_NUMBER` → `oaseslive.delivery_note_extended_remarks.DELIVERY_NOTE_NUMBER`

### oaseslive.delivery_note_item_header_1

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `oaseslive.batch_file_header.KEY`
- `delivery_note_number` → `oaseslive.delivery_note_extended_remarks.DELIVERY_NOTE_NUMBER`
- `requirement_number` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`

**Referenced By (Incoming):**

- `oaseslive.dues_register.item_number` → `delivery_note_number`
- `oaseslive.maint_cost_budget_adsb.ITEM_ID` → `delivery_note_number`
- `oaseslive.maint_cost_budget_cfds.ITEM_ID` → `delivery_note_number`
- `oaseslive.maint_cost_budget_costs.ITEM_ID` → `delivery_note_number`
- `oaseslive.maint_cost_budget_labour_ests.ITEM_ID` → `delivery_note_number`
- `oaseslive.maint_cost_budget_materials.ITEM_ID` → `delivery_note_number`
- `oaseslive.maint_cost_budget_packages.ITEM_ID` → `delivery_note_number`
- `oaseslive.maint_cost_budget_visits.ITEM_ID` → `delivery_note_number`
- `oaseslive.maint_cost_budget_workcards.ITEM_ID` → `delivery_note_number`
- `oaseslive.package_items.ITEM_ID` → `delivery_note_number`
- `oaseslive.shipment_item_demands.ITEM_ID` → `delivery_note_number`

### oaseslive.delivery_note_item_header_2

**References (Outgoing):**

- `pick_number` → `oaseslive.condition_pick_table.PART_NUMBER`
- `delivery_note_number` → `oaseslive.delivery_note_extended_remarks.DELIVERY_NOTE_NUMBER`

### oaseslive.delivery_note_master_list

**References (Outgoing):**

- `DELIVERY_NOTE_NUMBER` → `oaseslive.delivery_note_extended_remarks.DELIVERY_NOTE_NUMBER`

### oaseslive.demand_reason_to_movement_code

**References (Outgoing):**

- `MOVEMENT_CODE` → `oaseslive.component_movement_hist_life.part_number`
- `REASON_ID` → `oaseslive.demand_reason_to_movement_code.ID`

**Referenced By (Incoming):**

- `oaseslive.demand_reason_to_movement_code.REASON_ID` → `ID`
- `oaseslive.shipment_demands.reason_id` → `ID`
- `oaseslive.shipment_item_demands.DEMAND_ID` → `ID`
- `oaseslive.shipment_order_demands.demand_id` → `ID`
- `oaseslive.shipment_requirement_demands.demand_id` → `ID`
- `oaseslive.shipment_stocktransfer_demands.demand_id` → `ID`
- `oaseslive.shipment_works_orders_demands.demand_id` → `ID`

### oaseslive.departments

**References (Outgoing):**

- `DEPARTMENT_ID` → `oaseslive.departments.DEPARTMENT_ID`
- `EXPORT_CODE` → `oaseslive.export_codes.EXPORT_ID`

**Referenced By (Incoming):**

- `oaseslive.departments.DEPARTMENT_ID` → `DEPARTMENT_ID`
- `oaseslive.oeim_invoice_snap_departments.DEPARTMENT_ID` → `DEPARTMENT_ID`

### oaseslive.dmg_rpr_action_taken_details

**References (Outgoing):**

- `ACTION_TAKEN_ID` → `oaseslive.dmg_rpr_action_taken_details.ACTION_TAKEN_ID`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_action_taken_details.ACTION_TAKEN_ID` → `ACTION_TAKEN_ID`

### oaseslive.dmg_rpr_attachments

**References (Outgoing):**

- `DAMAGE_ID` → `oaseslive.dmg_rpr_damage.DAMAGE_ID`
- `DOCUMENT_IMAGE_ID` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`

### oaseslive.dmg_rpr_ca_approval_details

**References (Outgoing):**

- `CA_APPROVAL_ID` → `oaseslive.dmg_rpr_ca_approval_details.CA_APPROVAL_ID`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_ca_approval_details.CA_APPROVAL_ID` → `CA_APPROVAL_ID`

### oaseslive.dmg_rpr_corrosion_levels

**References (Outgoing):**

- `CORROSION_LEVEL_ID` → `oaseslive.dmg_rpr_corrosion_levels.CORROSION_LEVEL_ID`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_corrosion_levels.CORROSION_LEVEL_ID` → `CORROSION_LEVEL_ID`

### oaseslive.dmg_rpr_damage

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `SECTION_ID` → `oaseslive.amp_workcard_sections.section_id`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `DAMAGE_ID` → `oaseslive.dmg_rpr_damage.DAMAGE_ID`
- `DAMAGE_TYPE_ID` → `oaseslive.dmg_rpr_damage_types.DAMAGE_TYPE_ID`
- `ZONE_CODE` → `oaseslive.dmg_rpr_measurement_zones.MEASUREMENT_ZONE_ID`

**Referenced By (Incoming):**

- `oaseslive.accomp_hist_delta_1763.DAMAGE_ID` → `DAMAGE_ID`
- `oaseslive.accomplishment_history.DAMAGE_ID` → `DAMAGE_ID`
- `oaseslive.dmg_rpr_attachments.DAMAGE_ID` → `DAMAGE_ID`
- `oaseslive.dmg_rpr_damage.DAMAGE_ID` → `DAMAGE_ID`
- `oaseslive.dmg_rpr_damage_numbering.DAMAGE_ID` → `DAMAGE_ID`
- `oaseslive.dmg_rpr_damage_numbering.DAMAGE_NUMBER` → `DAMAGE_ID`
- `oaseslive.dmg_rpr_dmg_2d_position_labels.DAMAGE_ID` → `DAMAGE_ID`
- `oaseslive.dmg_rpr_dmg_2d_positions.DAMAGE_ID` → `DAMAGE_ID`
- `oaseslive.dmg_rpr_fitted_locations.DAMAGE_ID` → `DAMAGE_ID`
- `oaseslive.dmg_rpr_inspections.DAMAGE_ID` → `DAMAGE_ID`
- `oaseslive.dmg_rpr_interim_repairs.DAMAGE_ID` → `DAMAGE_ID`
- `oaseslive.dmg_rpr_location.DAMAGE_ID` → `DAMAGE_ID`
- `oaseslive.dmg_rpr_location_measurement.DAMAGE_ID` → `DAMAGE_ID`
- `oaseslive.dmg_rpr_permanent_repairs.DAMAGE_ID` → `DAMAGE_ID`
- `oaseslive.dmg_rpr_repair_req_details.DAMAGE_ID` → `DAMAGE_ID`
- `oaseslive.dmg_rpr_time_limited_repairs.DAMAGE_ID` → `DAMAGE_ID`

### oaseslive.dmg_rpr_damage_numbering

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `DAMAGE_ID` → `oaseslive.dmg_rpr_damage.DAMAGE_ID`
- `DAMAGE_NUMBER` → `oaseslive.dmg_rpr_damage.DAMAGE_ID`

### oaseslive.dmg_rpr_damage_types

**References (Outgoing):**

- `DAMAGE_TYPE_ID` → `oaseslive.dmg_rpr_damage_types.DAMAGE_TYPE_ID`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_damage.DAMAGE_TYPE_ID` → `DAMAGE_TYPE_ID`
- `oaseslive.dmg_rpr_damage_types.DAMAGE_TYPE_ID` → `DAMAGE_TYPE_ID`

### oaseslive.dmg_rpr_dmg_2d_position_labels

**References (Outgoing):**

- `DAMAGE_ID` → `oaseslive.dmg_rpr_damage.DAMAGE_ID`
- `LABEL_ID` → `oaseslive.dmg_rpr_dmg_2d_position_labels.LABEL_ID`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_dmg_2d_position_labels.LABEL_ID` → `LABEL_ID`
- `oaseslive.dmg_rpr_dmg_2d_positions.POSITION_ID` → `LABEL_ID`
- `oaseslive.dmg_rpr_location.POSITION_ID` → `LABEL_ID`

### oaseslive.dmg_rpr_dmg_2d_positions

**References (Outgoing):**

- `DAMAGE_ID` → `oaseslive.dmg_rpr_damage.DAMAGE_ID`
- `POSITION_ID` → `oaseslive.dmg_rpr_dmg_2d_position_labels.LABEL_ID`

### oaseslive.dmg_rpr_doc_effectivity

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `FLEET_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `DMG_RPR_DOC_EFFECTIVITY_ID` → `oaseslive.dmg_rpr_doc_effectivity.DMG_RPR_DOC_EFFECTIVITY_ID`
- `SUB_FLEET_ID` → `oaseslive.sub_fleets.sub_fleet_id`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_doc_effectivity.DMG_RPR_DOC_EFFECTIVITY_ID` → `DMG_RPR_DOC_EFFECTIVITY_ID`

### oaseslive.dmg_rpr_doc_subject

**References (Outgoing):**

- `SUBJECT_ID` → `oaseslive.dmg_rpr_doc_subject.SUBJECT_ID`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_doc_subject.SUBJECT_ID` → `SUBJECT_ID`
- `oaseslive.dmg_rpr_documents.SUBJECT_ID` → `SUBJECT_ID`
- `oaseslive.dmg_rpr_subject_sections.SUBJECT_ID` → `SUBJECT_ID`
- `oaseslive.dmg_rpr_subject_zones.SUBJECT_ID` → `SUBJECT_ID`

### oaseslive.dmg_rpr_document_order

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `FLEET_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `SUB_FLEET_ID` → `oaseslive.sub_fleets.sub_fleet_id`

### oaseslive.dmg_rpr_documents

**References (Outgoing):**

- `SUBJECT_ID` → `oaseslive.dmg_rpr_doc_subject.SUBJECT_ID`
- `DOCUMENT_IMAGE_ID` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`

### oaseslive.dmg_rpr_fitted_locations

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `DAMAGE_ID` → `oaseslive.dmg_rpr_damage.DAMAGE_ID`

### oaseslive.dmg_rpr_idnt_inspect

**References (Outgoing):**

- `INSPECTION_ID` → `oaseslive.dmg_rpr_inspection_type_dtls.INSPECTION_TYPE_ID`

### oaseslive.dmg_rpr_idnt_inspect_info

**References (Outgoing):**

- `INSPECTION_ID` → `oaseslive.dmg_rpr_inspection_type_dtls.INSPECTION_TYPE_ID`

### oaseslive.dmg_rpr_inspection_type_dtls

**References (Outgoing):**

- `INSPECTION_TYPE_ID` → `oaseslive.dmg_rpr_inspection_type_dtls.INSPECTION_TYPE_ID`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_idnt_inspect.INSPECTION_ID` → `INSPECTION_TYPE_ID`
- `oaseslive.dmg_rpr_idnt_inspect_info.INSPECTION_ID` → `INSPECTION_TYPE_ID`
- `oaseslive.dmg_rpr_inspection_type_dtls.INSPECTION_TYPE_ID` → `INSPECTION_TYPE_ID`
- `oaseslive.dmg_rpr_inspections.INSPECTION_ID` → `INSPECTION_TYPE_ID`
- `oaseslive.dmg_rpr_inspections.INSPECTION_TYPE_ID` → `INSPECTION_TYPE_ID`
- `oaseslive.dmg_rpr_stages.INSPECTION_ID` → `INSPECTION_TYPE_ID`

### oaseslive.dmg_rpr_inspections

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `DAMAGE_ID` → `oaseslive.dmg_rpr_damage.DAMAGE_ID`
- `INSPECTION_ID` → `oaseslive.dmg_rpr_inspection_type_dtls.INSPECTION_TYPE_ID`
- `INSPECTION_TYPE_ID` → `oaseslive.dmg_rpr_inspection_type_dtls.INSPECTION_TYPE_ID`
- `INTERIM_REPAIR_ID` → `oaseslive.dmg_rpr_interim_repairs.INTERIM_REPAIR_ID`
- `TIME_LIMITED_REPAIR_ID` → `oaseslive.dmg_rpr_time_limited_repairs.TIME_LIMITED_REPAIR_ID`
- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `PARAGRAPH_ID` → `oaseslive.paragraph_cancels.RFC_ID`
- `FREQUENCY_ID` → `oaseslive.rfc_frequency_phase_header.rfc_id`

### oaseslive.dmg_rpr_interim_repairs

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `DAMAGE_ID` → `oaseslive.dmg_rpr_damage.DAMAGE_ID`
- `INTERIM_REPAIR_ID` → `oaseslive.dmg_rpr_interim_repairs.INTERIM_REPAIR_ID`
- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `PARAGRAPH_ID` → `oaseslive.paragraph_cancels.RFC_ID`
- `FREQUENCY_ID` → `oaseslive.rfc_frequency_phase_header.rfc_id`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_inspections.INTERIM_REPAIR_ID` → `INTERIM_REPAIR_ID`
- `oaseslive.dmg_rpr_interim_repairs.INTERIM_REPAIR_ID` → `INTERIM_REPAIR_ID`
- `oaseslive.dmg_rpr_stages.INTERIM_REPAIR_ID` → `INTERIM_REPAIR_ID`

### oaseslive.dmg_rpr_location

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `DAMAGE_ID` → `oaseslive.dmg_rpr_damage.DAMAGE_ID`
- `POSITION_ID` → `oaseslive.dmg_rpr_dmg_2d_position_labels.LABEL_ID`
- `MATERIAL_TYPE_ID` → `oaseslive.dmg_rpr_material_types_dtls.MATERIAL_TYPE_ID`
- `SURFACE_FINISH_ID` → `oaseslive.dmg_rpr_surface_finish_details.SURFACE_FINISH_ID`

### oaseslive.dmg_rpr_location_measurement

**References (Outgoing):**

- `DAMAGE_ID` → `oaseslive.dmg_rpr_damage.DAMAGE_ID`
- `MEASUREMENT_ID` → `oaseslive.dmg_rpr_location_measurement.DAMAGE_ID`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_location_measurement.MEASUREMENT_ID` → `DAMAGE_ID`
- `oaseslive.dmg_rpr_measurement_sections.MEASUREMENT_ID` → `DAMAGE_ID`
- `oaseslive.dmg_rpr_measurement_zones.MEASUREMENT_ID` → `DAMAGE_ID`
- `oaseslive.dmg_rpr_measurements.MEASUREMENT_ID` → `DAMAGE_ID`

### oaseslive.dmg_rpr_mat_types_fld_dtls

**References (Outgoing):**

- `MATERIAL_TYPE_ID` → `oaseslive.dmg_rpr_material_types_dtls.MATERIAL_TYPE_ID`

### oaseslive.dmg_rpr_material_types_dtls

**References (Outgoing):**

- `MATERIAL_TYPE_ID` → `oaseslive.dmg_rpr_material_types_dtls.MATERIAL_TYPE_ID`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_location.MATERIAL_TYPE_ID` → `MATERIAL_TYPE_ID`
- `oaseslive.dmg_rpr_mat_types_fld_dtls.MATERIAL_TYPE_ID` → `MATERIAL_TYPE_ID`
- `oaseslive.dmg_rpr_material_types_dtls.MATERIAL_TYPE_ID` → `MATERIAL_TYPE_ID`

### oaseslive.dmg_rpr_measurement_sections

**References (Outgoing):**

- `SECTION_ID` → `oaseslive.amp_workcard_sections.section_id`
- `MEASUREMENT_ID` → `oaseslive.dmg_rpr_location_measurement.DAMAGE_ID`
- `MEASUREMENT_SECTION_ID` → `oaseslive.dmg_rpr_measurement_sections.MEASUREMENT_SECTION_ID`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_measurement_sections.MEASUREMENT_SECTION_ID` → `MEASUREMENT_SECTION_ID`

### oaseslive.dmg_rpr_measurement_zones

**References (Outgoing):**

- `MEASUREMENT_ID` → `oaseslive.dmg_rpr_location_measurement.DAMAGE_ID`
- `MEASUREMENT_ZONE_ID` → `oaseslive.dmg_rpr_measurement_zones.MEASUREMENT_ZONE_ID`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_damage.ZONE_CODE` → `MEASUREMENT_ZONE_ID`
- `oaseslive.dmg_rpr_measurement_zones.MEASUREMENT_ZONE_ID` → `MEASUREMENT_ZONE_ID`

### oaseslive.dmg_rpr_measurements

**References (Outgoing):**

- `MEASUREMENT_ID` → `oaseslive.dmg_rpr_location_measurement.DAMAGE_ID`

### oaseslive.dmg_rpr_permanent_repairs

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `REPAIR_ID` → `oaseslive.consumable_repair_xref_to_part.PART_NUMBER`
- `DAMAGE_ID` → `oaseslive.dmg_rpr_damage.DAMAGE_ID`
- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `PARAGRAPH_ID` → `oaseslive.paragraph_cancels.RFC_ID`
- `FREQUENCY_ID` → `oaseslive.rfc_frequency_phase_header.rfc_id`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_stages.PERMANENT_REPAIR_ID` → `REPAIR_ID`

### oaseslive.dmg_rpr_repair_req_details

**References (Outgoing):**

- `DAMAGE_ID` → `oaseslive.dmg_rpr_damage.DAMAGE_ID`
- `REQUIREMENT_NUMBER` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`

### oaseslive.dmg_rpr_section_details

**References (Outgoing):**

- `SECTION_ID` → `oaseslive.amp_workcard_sections.section_id`

### oaseslive.dmg_rpr_section_fleet_details

**References (Outgoing):**

- `SECTION_ID` → `oaseslive.amp_workcard_sections.section_id`

### oaseslive.dmg_rpr_stage_limits

**References (Outgoing):**

- `LIMIT_ID` → `oaseslive.amp_component_intervals_limits.component_interval_id`
- `STAGE_ID` → `oaseslive.amp_component_intervals_stages.component_interval_id`
- `LIFE_CODE_LEVEL_ID` → `oaseslive.life_code_levels.life_code_level_id`

### oaseslive.dmg_rpr_stages

**References (Outgoing):**

- `STAGE_ID` → `oaseslive.amp_component_intervals_stages.component_interval_id`
- `INSPECTION_ID` → `oaseslive.dmg_rpr_inspection_type_dtls.INSPECTION_TYPE_ID`
- `INTERIM_REPAIR_ID` → `oaseslive.dmg_rpr_interim_repairs.INTERIM_REPAIR_ID`
- `PERMANENT_REPAIR_ID` → `oaseslive.dmg_rpr_permanent_repairs.REPAIR_ID`
- `TIME_LIMITED_REPAIR_ID` → `oaseslive.dmg_rpr_time_limited_repairs.TIME_LIMITED_REPAIR_ID`

### oaseslive.dmg_rpr_subject_sections

**References (Outgoing):**

- `SECTION_ID` → `oaseslive.amp_workcard_sections.section_id`
- `SUBJECT_ID` → `oaseslive.dmg_rpr_doc_subject.SUBJECT_ID`
- `SUBJECT_SECTION_ID` → `oaseslive.dmg_rpr_subject_sections.SUBJECT_SECTION_ID`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_subject_sections.SUBJECT_SECTION_ID` → `SUBJECT_SECTION_ID`

### oaseslive.dmg_rpr_subject_zones

**References (Outgoing):**

- `SUBJECT_ID` → `oaseslive.dmg_rpr_doc_subject.SUBJECT_ID`
- `SUBJECT_ZONE_ID` → `oaseslive.dmg_rpr_subject_zones.SUBJECT_ZONE_ID`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_subject_zones.SUBJECT_ZONE_ID` → `SUBJECT_ZONE_ID`

### oaseslive.dmg_rpr_surface_finish_details

**References (Outgoing):**

- `SURFACE_FINISH_ID` → `oaseslive.dmg_rpr_surface_finish_details.SURFACE_FINISH_ID`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_location.SURFACE_FINISH_ID` → `SURFACE_FINISH_ID`
- `oaseslive.dmg_rpr_surface_finish_details.SURFACE_FINISH_ID` → `SURFACE_FINISH_ID`

### oaseslive.dmg_rpr_time_limited_repairs

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `DAMAGE_ID` → `oaseslive.dmg_rpr_damage.DAMAGE_ID`
- `TIME_LIMITED_REPAIR_ID` → `oaseslive.dmg_rpr_time_limited_repairs.TIME_LIMITED_REPAIR_ID`
- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `PARAGRAPH_ID` → `oaseslive.paragraph_cancels.RFC_ID`
- `FREQUENCY_ID` → `oaseslive.rfc_frequency_phase_header.rfc_id`

**Referenced By (Incoming):**

- `oaseslive.dmg_rpr_inspections.TIME_LIMITED_REPAIR_ID` → `TIME_LIMITED_REPAIR_ID`
- `oaseslive.dmg_rpr_stages.TIME_LIMITED_REPAIR_ID` → `TIME_LIMITED_REPAIR_ID`
- `oaseslive.dmg_rpr_time_limited_repairs.TIME_LIMITED_REPAIR_ID` → `TIME_LIMITED_REPAIR_ID`

### oaseslive.document_classes

**References (Outgoing):**

- `DOCUMENT_ID` → `oaseslive.aircraft_documents.AIRCRAFT_DOCUMENT_ID`

**Referenced By (Incoming):**

- `oaseslive.drn_class_codes.CLASS_CODE` → `DOCUMENT_ID`
- `oaseslive.drn_fleet_ata.CLASS_CODE` → `DOCUMENT_ID`
- `oaseslive.drn_maint_mod.CLASS_CODE` → `DOCUMENT_ID`
- `oaseslive.drn_maintenance_history.CLASS_CODE` → `DOCUMENT_ID`
- `oaseslive.drn_mod_desc_order_hist.CLASS_CODE` → `DOCUMENT_ID`
- `oaseslive.drn_modification_history.CLASS_CODE` → `DOCUMENT_ID`
- `oaseslive.drn_part_serial.CLASS_CODE` → `DOCUMENT_ID`
- `oaseslive.fleet_forecast_plans.CLASS_CODE` → `DOCUMENT_ID`
- `oaseslive.forecast_cache.CLASS_CODE` → `DOCUMENT_ID`

### oaseslive.document_image_source

**References (Outgoing):**

- `DOCUMENT_IMAGE_SOURCE_ID` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`

**Referenced By (Incoming):**

- `oaseslive.accomp_hist_delta_1763.DOCUMENT_IMAGE_ID` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.accomplishment_history.DOCUMENT_IMAGE_ID` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.aircraft_documents.DOCUMENT_IMAGE_ID` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.amp_report_documents.DOCUMENT_IMAGE_ID` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.cq_documents.DOCUMENT_IMAGE_ID` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.dmg_rpr_attachments.DOCUMENT_IMAGE_ID` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.dmg_rpr_documents.DOCUMENT_IMAGE_ID` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.document_image_types.DOCUMENT_IMAGE_SOURCE_ID` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.document_images.document_image_id` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.document_images_jn.DOCUMENT_IMAGE_ID` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.employees_licences.document_image_id` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.goods_received_sheet_document.DOCUMENT_IMAGE_ID` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.nrc_documents.document_image_id` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.part_serial_documents.DOCUMENT_IMAGE_ID` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.reliability_report_logo_desc.DOCUMENT_IMAGE_ID` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.requirement_source_codes.SOURCE_CODE` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.rfc_documents.DOCUMENT_IMAGE_ID` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.shipment_documents.DOCUMENT_IMAGE_ID` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.stock_documents.DOCUMENT_IMAGE_ID` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.strip_documents.DOCUMENT_IMAGE_ID` → `DOCUMENT_IMAGE_SOURCE_ID`
- `oaseslive.tech_log_documents.DOCUMENT_IMAGE_ID` → `DOCUMENT_IMAGE_SOURCE_ID`

### oaseslive.document_image_types

**References (Outgoing):**

- `DOCUMENT_IMAGE_SOURCE_ID` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`

### oaseslive.document_images

**References (Outgoing):**

- `document_image_id` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`

### oaseslive.document_images_jn

**References (Outgoing):**

- `DOCUMENT_IMAGE_ID` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`

### oaseslive.drn_class_codes

**References (Outgoing):**

- `CLASS_CODE` → `oaseslive.document_classes.DOCUMENT_ID`

### oaseslive.drn_component_mods_history

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `REPORT_ID` → `oaseslive.amp_report_documents.FLEET`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.drn_components_nsbl_history

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `LIFE_CODE_LEVEL_ID` → `oaseslive.life_code_levels.life_code_level_id`

### oaseslive.drn_cycles

**References (Outgoing):**

- `CYCLE_NUMBER` → `oaseslive.accum_cycles_static_data.PARENT_PART_NUMBER`
- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`

**Referenced By (Incoming):**

- `oaseslive.drn_maint_mod.DRN_CYCLE_NUMBER` → `FLEET`

### oaseslive.drn_fleet_ata

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `CLASS_CODE` → `oaseslive.document_classes.DOCUMENT_ID`

### oaseslive.drn_life_limits

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `LIFE_CODE_LEVEL_ID` → `oaseslive.life_code_levels.life_code_level_id`

### oaseslive.drn_maint_mod

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `CLASS_CODE` → `oaseslive.document_classes.DOCUMENT_ID`
- `DRN_CYCLE_NUMBER` → `oaseslive.drn_cycles.FLEET`

### oaseslive.drn_maint_mod_notes

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.drn_maintenance_history

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `REPORT_ID` → `oaseslive.amp_report_documents.FLEET`
- `CLASS_CODE` → `oaseslive.document_classes.DOCUMENT_ID`

### oaseslive.drn_maintenance_history_notes

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.drn_mod_desc_order_hist

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `CLASS_CODE` → `oaseslive.document_classes.DOCUMENT_ID`

### oaseslive.drn_modification_history

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `REPORT_ID` → `oaseslive.amp_report_documents.FLEET`
- `CLASS_CODE` → `oaseslive.document_classes.DOCUMENT_ID`

### oaseslive.drn_modification_history_notes

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.drn_part_serial

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `CLASS_CODE` → `oaseslive.document_classes.DOCUMENT_ID`

### oaseslive.dues_register

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `item_number` → `oaseslive.delivery_note_item_header_1.delivery_note_number`
- `requirement_number` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`

### oaseslive.dummy_part_numbers

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.easa_trace

**References (Outgoing):**

- `TRACE_ID` → `oaseslive.easa_trace.TRACE_ID`

**Referenced By (Incoming):**

- `oaseslive.easa_trace.TRACE_ID` → `TRACE_ID`
- `oaseslive.sabre_trace.TRACE_ID` → `TRACE_ID`

### oaseslive.economic_blocks

**References (Outgoing):**

- `block_code` → `oaseslive.block_countries.block_code`

### oaseslive.email_licence

**Referenced By (Incoming):**

- `oaseslive.defect_stage_employees.licence_id` → `LICENSE_ID`
- `oaseslive.employees_licences.licence_id` → `LICENSE_ID`
- `oaseslive.licence_categories.licence_id` → `LICENSE_ID`
- `oaseslive.sfdc_activity.LICENCE_ID` → `LICENSE_ID`

### oaseslive.email_notification

**References (Outgoing):**

- `CATEGORY_ID` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

**Referenced By (Incoming):**

- `oaseslive.security_user_notifications.NOTIFICATION_ID` → `ID`

### oaseslive.email_notification_categories

**References (Outgoing):**

- `category_id` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

**Referenced By (Incoming):**

- `oaseslive.measurement_alerts_aircraft.email_notification_cat_id` → `category_id`
- `oaseslive.measurement_alerts_fleet.email_notification_cat_id` → `category_id`

### oaseslive.email_template

**References (Outgoing):**

- `TEMPLATE_ID` → `oaseslive.email_template.TEMPLATE_ID`

**Referenced By (Incoming):**

- `oaseslive.email_template.TEMPLATE_ID` → `TEMPLATE_ID`
- `oaseslive.jasper_workcard_templates.TEMPLATE_ID` → `TEMPLATE_ID`

### oaseslive.employee_experience_details

**References (Outgoing):**

- `EMPLOYEE_NUMBER` → `oaseslive.defect_stage_employees.defect_id`
- `EXPERIENCE_ID` → `oaseslive.employee_experience_details.EXPERIENCE_ID`

**Referenced By (Incoming):**

- `oaseslive.employee_experience_details.EXPERIENCE_ID` → `EXPERIENCE_ID`

### oaseslive.employee_presence

**References (Outgoing):**

- `EMPLOYEE_NUMBER` → `oaseslive.defect_stage_employees.defect_id`

### oaseslive.employee_presence_log

**References (Outgoing):**

- `TASK_NUMBER` → `oaseslive.amp_datmig_comp_task_lookup.FLEET`
- `EMPLOYEE_NUMBER` → `oaseslive.defect_stage_employees.defect_id`

### oaseslive.employee_training_details

**References (Outgoing):**

- `EMPLOYEE_NUMBER` → `oaseslive.defect_stage_employees.defect_id`
- `TRAINING_ID` → `oaseslive.employee_training_details.EMPLOYEE_NUMBER`

**Referenced By (Incoming):**

- `oaseslive.employee_training_details.TRAINING_ID` → `EMPLOYEE_NUMBER`

### oaseslive.employees

**References (Outgoing):**

- `employee_number` → `oaseslive.defect_stage_employees.defect_id`

### oaseslive.employees_licences

**References (Outgoing):**

- `employee_number` → `oaseslive.defect_stage_employees.defect_id`
- `document_image_id` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`
- `licence_id` → `oaseslive.email_licence.LICENSE_ID`
- `scope_type_id` → `oaseslive.scope_type_rating.scope_type_id`

### oaseslive.end_use_codes

**References (Outgoing):**

- `END_USE_CODE` → `oaseslive.end_use_codes.END_USE_CODE`

**Referenced By (Incoming):**

- `oaseslive.account_location_header_9.end_use_number` → `END_USE_CODE`
- `oaseslive.end_use_codes.END_USE_CODE` → `END_USE_CODE`
- `oaseslive.sales_invoice_genled_xref.END_USE_CODE` → `END_USE_CODE`
- `oaseslive.stock_group_additional_data.end_use_code` → `END_USE_CODE`

### oaseslive.engineering_support_history

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `DEFECT_NUMBER` → `oaseslive.defect_extensions.DEFECT_ID`
- `ENGINEERING_SUPPORT_HISTORY_ID` → `oaseslive.engineering_support_history.ENGINEERING_SUPPORT_HISTORY_ID`

**Referenced By (Incoming):**

- `oaseslive.engineering_support_history.ENGINEERING_SUPPORT_HISTORY_ID` → `ENGINEERING_SUPPORT_HISTORY_ID`

### oaseslive.esign_off_nrc

**References (Outgoing):**

- `DOCUMENT_ID` → `oaseslive.aircraft_documents.AIRCRAFT_DOCUMENT_ID`
- `NRC_NUMBER` → `oaseslive.cq_quote_nrc_access_panels.QUOTE_ID`

### oaseslive.export_codes

**References (Outgoing):**

- `EXPORT_ID` → `oaseslive.export_codes.EXPORT_ID`
- `EXPORT_CODE` → `oaseslive.export_codes.EXPORT_ID`

**Referenced By (Incoming):**

- `oaseslive.departments.EXPORT_CODE` → `EXPORT_ID`
- `oaseslive.export_codes.EXPORT_ID` → `EXPORT_ID`
- `oaseslive.export_codes.EXPORT_CODE` → `EXPORT_ID`
- `oaseslive.oeim_invoice_snap_departments.EXPORT_CODE` → `EXPORT_ID`
- `oaseslive.oeim_invoice_snap_vat_codes.EXPORT_ID` → `EXPORT_ID`

### oaseslive.extended_part_descriptions

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.extensions

**References (Outgoing):**

- `EXTENSION_ID` → `oaseslive.add_extension_permissions.USER_ID`

### oaseslive.fixed_charges

**References (Outgoing):**

- `cost_code` → `oaseslive.cost_codes.id`

### oaseslive.fleet_assembles

**References (Outgoing):**

- `FLEET_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`

### oaseslive.fleet_chap_part_header_1

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `ALTERNATE_PART_NUMBER` → `oaseslive.alternate_parts.PART_NUMBER`

### oaseslive.fleet_chap_part_header_2

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.fleet_chap_part_header_3

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.fleet_chapter_part_aircraft

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.fleet_forecast_plans

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `PLAN_ID` → `oaseslive.amp_planning_notes.FLEET_CODE`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `CLASS_CODE` → `oaseslive.document_classes.DOCUMENT_ID`

### oaseslive.fleet_forecast_plans_amp

**References (Outgoing):**

- `PACKAGE_CODES` → `oaseslive.amp_packages.fleet`
- `PLAN_ID` → `oaseslive.amp_planning_notes.FLEET_CODE`
- `VISIT_CODES` → `oaseslive.amp_visits.fleet`
- `WORKCARD_NUMBERS` → `oaseslive.amp_workcards_by_package.fleet`

### oaseslive.fleet_forecast_plans_drn

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `PLAN_ID` → `oaseslive.amp_planning_notes.FLEET_CODE`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.fleet_forecast_plans_rfc

**References (Outgoing):**

- `PLAN_ID` → `oaseslive.amp_planning_notes.FLEET_CODE`
- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`

**Referenced By (Incoming):**

- `oaseslive.accomp_bkup.RFC_ID` → `PLAN_ID`
- `oaseslive.accomp_hist_delta_1763.RFC_ID` → `PLAN_ID`
- `oaseslive.accomp_hist_lost_sched.RFC_ID` → `PLAN_ID`
- `oaseslive.accomplishment_history.RFC_ID` → `PLAN_ID`
- `oaseslive.dmg_rpr_inspections.RFC_ID` → `PLAN_ID`
- `oaseslive.dmg_rpr_interim_repairs.RFC_ID` → `PLAN_ID`
- `oaseslive.dmg_rpr_permanent_repairs.RFC_ID` → `PLAN_ID`
- `oaseslive.dmg_rpr_time_limited_repairs.RFC_ID` → `PLAN_ID`
- `oaseslive.fleet_forecast_plans_rfc.RFC_ID` → `PLAN_ID`
- `oaseslive.forecast_cache.RFC_ID` → `PLAN_ID`
- `oaseslive.maint_cost_budget_adsb.RFC_ID` → `PLAN_ID`
- `oaseslive.paragraph_cancels.RFC_ID` → `PLAN_ID`
- `oaseslive.planners_notes_xref.RFC_ID` → `PLAN_ID`
- `oaseslive.rfc_aircraft.rfc_id` → `PLAN_ID`
- `oaseslive.rfc_components.rfc_id` → `PLAN_ID`
- `oaseslive.rfc_documents.RFC_ID` → `PLAN_ID`
- `oaseslive.rfc_effectivity_ata.rfc_id` → `PLAN_ID`
- `oaseslive.rfc_effectivity_fleet.rfc_id` → `PLAN_ID`
- `oaseslive.rfc_effectivity_part.rfc_id` → `PLAN_ID`
- `oaseslive.rfc_evaluation_history.RFC_ID` → `PLAN_ID`
- `oaseslive.rfc_frequency_phase_header.rfc_id` → `PLAN_ID`
- `oaseslive.rfc_frequency_phase_limits.rfc_id` → `PLAN_ID`
- `oaseslive.rfc_frequency_phases.rfc_id` → `PLAN_ID`
- `oaseslive.rfc_header.rfc_id` → `PLAN_ID`
- `oaseslive.rfc_header_publications.RFC_ID` → `PLAN_ID`
- `oaseslive.rfc_paragraphs.rfc_id` → `PLAN_ID`
- `oaseslive.rfc_print_history_log.RFC_ID` → `PLAN_ID`
- `oaseslive.rfc_relationships.rfc_id` → `PLAN_ID`
- `oaseslive.rfc_transaction_log.RFC_ID` → `PLAN_ID`
- `oaseslive.schedule_forecast_xref.RFC_ID` → `PLAN_ID`
- `oaseslive.schedule_source.RFC_ID` → `PLAN_ID`
- `oaseslive.temp_rfc_paragraphs.RFC_ID` → `PLAN_ID`

### oaseslive.fleet_header_2

**References (Outgoing):**

- `mel_revision_number` → `oaseslive.mel_revision_history.HISTORY_ID`

### oaseslive.fleet_statistics

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`

### oaseslive.float_history

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `USER_ID` → `oaseslive.dataset_locks_by_user.USER_ID`

### oaseslive.flown_sectors

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `flight_number` → `oaseslive.aircraft_flight_hours_1.AIRCRAFT_CODE`
- `report_id` → `oaseslive.amp_report_documents.FLEET`
- `sector_id` → `oaseslive.flown_sectors.aircraft_code`

**Referenced By (Incoming):**

- `oaseslive.flown_sectors.sector_id` → `aircraft_code`
- `oaseslive.flown_sectors_bkp.SECTOR_ID` → `aircraft_code`
- `oaseslive.flown_sectors_con_680.SECTOR_ID` → `aircraft_code`
- `oaseslive.flown_sectors_delta1817.SECTOR_ID` → `aircraft_code`
- `oaseslive.sectors.sector_id` → `aircraft_code`

### oaseslive.flown_sectors_bkp

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `FLIGHT_NUMBER` → `oaseslive.aircraft_flight_hours_1.AIRCRAFT_CODE`
- `REPORT_ID` → `oaseslive.amp_report_documents.FLEET`
- `SECTOR_ID` → `oaseslive.flown_sectors.aircraft_code`

### oaseslive.flown_sectors_con_680

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `FLIGHT_NUMBER` → `oaseslive.aircraft_flight_hours_1.AIRCRAFT_CODE`
- `REPORT_ID` → `oaseslive.amp_report_documents.FLEET`
- `SECTOR_ID` → `oaseslive.flown_sectors.aircraft_code`

### oaseslive.flown_sectors_delta1817

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `FLIGHT_NUMBER` → `oaseslive.aircraft_flight_hours_1.AIRCRAFT_CODE`
- `REPORT_ID` → `oaseslive.amp_report_documents.FLEET`
- `SECTOR_ID` → `oaseslive.flown_sectors.aircraft_code`

### oaseslive.forecast_cache

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `ALERT_NUMBER` → `oaseslive.alert_colors.ALERT_TYPE_ID`
- `WORKCARD_CODE` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `VISIT_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `PACKAGE_CODE` → `oaseslive.amp_package_notes.fleet`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `WORKCARD_INTERVAL_ID` → `oaseslive.amp_workcard_intervals_limits.workcard_interval_id`
- `COMPONENT_LIFE_LIMIT_ID` → `oaseslive.component_life_limits.component_life_limit_id`
- `WORKS_ORDER_NUMBER` → `oaseslive.credit_works_order_cards.credit_note_no`
- `CLASS_CODE` → `oaseslive.document_classes.DOCUMENT_ID`
- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`

### oaseslive.forecast_cache_ac_details

**References (Outgoing):**

- `revision_id` → `oaseslive.amp_revisions.revision_id`

### oaseslive.forecast_cache_revisions

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `fleet_code` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `revision_id` → `oaseslive.amp_revisions.revision_id`

### oaseslive.forecast_filter_groups

**References (Outgoing):**

- `GROUP_ID` → `oaseslive.forecast_filter_groups.GROUP_ID`

**Referenced By (Incoming):**

- `oaseslive.forecast_filter_groups.GROUP_ID` → `GROUP_ID`
- `oaseslive.forecast_filters.FILTER_ID` → `GROUP_ID`
- `oaseslive.forecast_filters.GROUP_ID` → `GROUP_ID`
- `oaseslive.security_group_perm_attribute.GROUP_ID` → `GROUP_ID`
- `oaseslive.security_group_permissions.GROUP_ID` → `GROUP_ID`
- `oaseslive.security_group_policies.GROUP_ID` → `GROUP_ID`
- `oaseslive.security_groups.GROUP_ID` → `GROUP_ID`
- `oaseslive.security_user_groups.GROUP_ID` → `GROUP_ID`

### oaseslive.forecast_filters

**References (Outgoing):**

- `FILTER_ID` → `oaseslive.forecast_filter_groups.GROUP_ID`
- `GROUP_ID` → `oaseslive.forecast_filter_groups.GROUP_ID`

### oaseslive.forecast_parameters

**References (Outgoing):**

- `PARAM_ID` → `oaseslive.forecast_parameters.PARAM_ID`

**Referenced By (Incoming):**

- `oaseslive.forecast_parameters.PARAM_ID` → `PARAM_ID`

### oaseslive.forecast_variation_details

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`

### oaseslive.form_number

**References (Outgoing):**

- `FORM_NUMBER` → `oaseslive.company_form_attachments.ATTACHMENT_ID`
- `FORM_NUMBER_ID` → `oaseslive.form_number.FORM_NUMBER_ID`

**Referenced By (Incoming):**

- `oaseslive.form_number.FORM_NUMBER_ID` → `FORM_NUMBER_ID`

### oaseslive.forward_schedule_summary_vals

**References (Outgoing):**

- `LIFE_CODE_LEVEL_ID` → `oaseslive.life_code_levels.life_code_level_id`

### oaseslive.freight_cost_markups

**References (Outgoing):**

- `FREIGHT_COST_MARKUP_ID` → `oaseslive.freight_cost_markups.FREIGHT_COST_MARKUP_ID`

**Referenced By (Incoming):**

- `oaseslive.customer_contracts.markup_code` → `FREIGHT_COST_MARKUP_ID`
- `oaseslive.freight_cost_markups.FREIGHT_COST_MARKUP_ID` → `FREIGHT_COST_MARKUP_ID`
- `oaseslive.freight_costs.FREIGHT_COST_ID` → `FREIGHT_COST_MARKUP_ID`
- `oaseslive.markups.MARKUP_CODE` → `FREIGHT_COST_MARKUP_ID`
- `oaseslive.parts_freight_tiered_markups.FREIGHT_COST_MARKUP_ID` → `FREIGHT_COST_MARKUP_ID`
- `oaseslive.tiered_markup_range.MARKUP_CODE` → `FREIGHT_COST_MARKUP_ID`

### oaseslive.freight_costs

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `FREIGHT_COST_ID` → `oaseslive.freight_cost_markups.FREIGHT_COST_MARKUP_ID`
- `SHIPMENT_ITEM_ID` → `oaseslive.shipment_item.SHIPMENT_ITEM_ID`

### oaseslive.future_flights

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.gl_global_codes

**References (Outgoing):**

- `GL_ID` → `oaseslive.gl_global_codes.GL_ID`

**Referenced By (Incoming):**

- `oaseslive.gl_global_codes.GL_ID` → `GL_ID`

### oaseslive.goods_received_sheet_document

**References (Outgoing):**

- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `DOCUMENT_IMAGE_ID` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`

**Referenced By (Incoming):**

- `oaseslive.batch_record_1.goods_received_number` → `BATCH_NUMBER`
- `oaseslive.batch_record_1_gu4240.GOODS_RECEIVED_NUMBER` → `BATCH_NUMBER`
- `oaseslive.invoice_lines.GOODS_RECEIVED_NUMBER` → `BATCH_NUMBER`
- `oaseslive.order_goods_received.goods_received_number` → `BATCH_NUMBER`
- `oaseslive.ordr_goods_bkp.GOODS_RECEIVED_NUMBER` → `BATCH_NUMBER`

### oaseslive.hazardous_materials

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.ie96_historic

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `BIN_NUMBER` → `oaseslive.bins.bin_number`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `INV_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`
- `PRICE_TYPE_CODE` → `oaseslive.price_types.price_type_code`

### oaseslive.inherited_acquisition_costs

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.invoice_categories

**Referenced By (Incoming):**

- `oaseslive.access_dim_accounts_info.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.ie96_historic.INV_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.invoice_line_notes.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.invoice_lines.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.invoice_trail_entries.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.invoices.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.maint_cost_mro_wo_invoices.INVOICE_ID` → `INVOICE_CATEGORY`
- `oaseslive.maintenance_cost_invoices.INVOICE_ID` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_cards.invoice_number` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_fixed_charges.invoice_number` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_inclusive_hrs.invoice_number` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_materials.invoice_number` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_packages.invoice_number` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_snap_con_rates.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_snap_cost_codes.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_snap_currencies.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_snap_departments.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_snap_employees.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_snap_part_master.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_snap_pay_types.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_snap_pm_bkup.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_snap_public_hol.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_snap_serl_master.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_snap_sfdc_book.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_snap_time_cats.invoice_number` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_snap_time_crits.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_snap_users.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_snap_vat_codes.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_warranty.invoice_number` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_warranty_refunds.invoice_number` → `INVOICE_CATEGORY`
- `oaseslive.oeim_invoice_works_orders.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.oeim_quote_dismissed.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.order_goods_received_invoices.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.order_history.INVOICE_NUMBER` → `INVOICE_CATEGORY`
- `oaseslive.sales_history.invoice_number` → `INVOICE_CATEGORY`
- `oaseslive.sales_invoices_xref.INVOICE_NUMBER` → `INVOICE_CATEGORY`

### oaseslive.invoice_line_notes

**References (Outgoing):**

- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

**Referenced By (Incoming):**

- `oaseslive.aircraft_header_1.line_number` → `INVOICE_NUMBER`

### oaseslive.invoice_lines

**References (Outgoing):**

- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `VAT_CODE` → `oaseslive.amp_workcard_activations.workcard_activation_id`
- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`
- `GOODS_RECEIVED_NUMBER` → `oaseslive.goods_received_sheet_document.BATCH_NUMBER`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.invoice_system_header

**References (Outgoing):**

- `KEY_ID` → `oaseslive.osys_key_to_reportid.OSYSKEY`

### oaseslive.invoice_trail_entries

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`
- `INVOICE_TRAIL_ID` → `oaseslive.invoice_trail_entries.INVOICE_TRAIL_ID`

**Referenced By (Incoming):**

- `oaseslive.invoice_trail_entries.INVOICE_TRAIL_ID` → `INVOICE_TRAIL_ID`

### oaseslive.invoices

**References (Outgoing):**

- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.jasper_workcard_templates

**References (Outgoing):**

- `TEMPLATE_ID` → `oaseslive.email_template.TEMPLATE_ID`

### oaseslive.lasers_system_header

**References (Outgoing):**

- `KEY_ID` → `oaseslive.osys_key_to_reportid.OSYSKEY`

### oaseslive.latest_repair_values

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`

### oaseslive.ldt

**References (Outgoing):**

- `LIFE_CODE_LEVEL_ID` → `oaseslive.life_code_levels.life_code_level_id`

### oaseslive.le80_defect_temp

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.licence_categories

**References (Outgoing):**

- `licence_id` → `oaseslive.email_licence.LICENSE_ID`

### oaseslive.life_code_entry

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `report_id` → `oaseslive.amp_report_documents.FLEET`
- `life_code_level_id` → `oaseslive.life_code_levels.life_code_level_id`

### oaseslive.life_code_entry_backup

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `REPORT_ID` → `oaseslive.amp_report_documents.FLEET`
- `LIFE_CODE_LEVEL_ID` → `oaseslive.life_code_levels.life_code_level_id`

### oaseslive.life_code_entry_dbf1065

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `REPORT_ID` → `oaseslive.amp_report_documents.FLEET`
- `LIFE_CODE_LEVEL_ID` → `oaseslive.life_code_levels.life_code_level_id`

### oaseslive.life_code_levels

**References (Outgoing):**

- `life_code` → `oaseslive.aircraft_life.AIRCRAFT_CODE`
- `validation_code` → `oaseslive.awsdms_validation_failures_v1.TASK_NAME`
- `life_code_level_id` → `oaseslive.life_code_levels.life_code_level_id`

**Referenced By (Incoming):**

- `oaseslive.accomp_hist_lost_sched_val.LIFE_CODE_LEVEL_ID` → `life_code_level_id`
- `oaseslive.accomp_values_bkup.LIFE_CODE_LEVEL_ID` → `life_code_level_id`
- `oaseslive.accomplishment_history_values.LIFE_CODE_LEVEL_ID` → `life_code_level_id`
- `oaseslive.aircraft_life.LIFE_CODE_LEVEL_ID` → `life_code_level_id`
- `oaseslive.aircraft_life_dbf1065.LIFE_CODE_LEVEL_ID` → `life_code_level_id`
- `oaseslive.amp_component_intervals_limits.life_code_level_id` → `life_code_level_id`
- `oaseslive.amp_wc_in_limits_bak.LIFE_CODE_LEVEL_ID` → `life_code_level_id`
- `oaseslive.amp_workcard_intervals_limits.life_code_level_id` → `life_code_level_id`
- `oaseslive.amp_workcard_lcl_applicability.LIFE_CODE_LEVEL_ID` → `life_code_level_id`
- `oaseslive.completion_life_values.LIFE_CODE_LEVEL_ID` → `life_code_level_id`
- `oaseslive.component_life.life_code_level_id` → `life_code_level_id`
- `oaseslive.component_movement_hist_life.life_code_level_id` → `life_code_level_id`
- `oaseslive.dmg_rpr_stage_limits.LIFE_CODE_LEVEL_ID` → `life_code_level_id`
- `oaseslive.drn_components_nsbl_history.LIFE_CODE_LEVEL_ID` → `life_code_level_id`
- `oaseslive.drn_life_limits.LIFE_CODE_LEVEL_ID` → `life_code_level_id`
- `oaseslive.forward_schedule_summary_vals.LIFE_CODE_LEVEL_ID` → `life_code_level_id`
- `oaseslive.ldt.LIFE_CODE_LEVEL_ID` → `life_code_level_id`
- `oaseslive.life_code_entry.life_code_level_id` → `life_code_level_id`
- `oaseslive.life_code_entry_backup.LIFE_CODE_LEVEL_ID` → `life_code_level_id`
- `oaseslive.life_code_entry_dbf1065.LIFE_CODE_LEVEL_ID` → `life_code_level_id`
- `oaseslive.life_code_levels.life_code_level_id` → `life_code_level_id`
- `oaseslive.measurement_alerts_aircraft.life_code_level_id` → `life_code_level_id`
- `oaseslive.measurement_alerts_fleet.life_code_level_id` → `life_code_level_id`
- `oaseslive.rfc_frequency_phase_limits.life_code_level_id` → `life_code_level_id`

### oaseslive.life_codes

**References (Outgoing):**

- `life_code` → `oaseslive.aircraft_life.AIRCRAFT_CODE`

### oaseslive.lmc_base_data_defs

**Referenced By (Incoming):**

- `oaseslive.lmc_base_data_reported_wc.LMC_BASE_DATA_ID` → `BD_DEF_ID`

### oaseslive.lmc_base_data_options

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `OPT_ID` → `oaseslive.lmc_base_data_options.OPT_ID`

**Referenced By (Incoming):**

- `oaseslive.lmc_base_data_options.OPT_ID` → `OPT_ID`

### oaseslive.lmc_base_data_reported_wc

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `LMC_BASE_DATA_ID` → `oaseslive.lmc_base_data_defs.BD_DEF_ID`

### oaseslive.loaned_units

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `order_number` → `oaseslive.batch_orders.BATCH_NUMBER`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.long_serial_number_xref

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `long_serial_number` → `oaseslive.long_serial_number_xref.part_number`

**Referenced By (Incoming):**

- `oaseslive.long_serial_number_xref.long_serial_number` → `part_number`
- `oaseslive.oeim_invoice_snap_serl_master.LONG_SERIAL_NUMBER` → `part_number`
- `oaseslive.rotable_batch_locations.long_serial_number` → `part_number`
- `oaseslive.short_long_serials.LONG_SERIAL_NUMBER` → `part_number`

### oaseslive.maint_accomplishment_costs

**References (Outgoing):**

- `ACCOMPLISHMENT_ID` → `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID`
- `MAINT_COST_ID` → `oaseslive.maint_cost_budget_adsb.BUDGET_ID`

### oaseslive.maint_associated_cost_aircraft

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `ASSOCIATED_COST_ID` → `oaseslive.maint_associated_cost_aircraft.ASSOCIATED_COST_ID`
- `CATEGORY_ID` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

**Referenced By (Incoming):**

- `oaseslive.maint_associated_cost_aircraft.ASSOCIATED_COST_ID` → `ASSOCIATED_COST_ID`
- `oaseslive.maint_associated_costs.ASSOCIATED_COST_ID` → `ASSOCIATED_COST_ID`

### oaseslive.maint_associated_costs

**References (Outgoing):**

- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`
- `ASSOCIATED_COST_ID` → `oaseslive.maint_associated_cost_aircraft.ASSOCIATED_COST_ID`

### oaseslive.maint_card_pref_cost_cats

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`

### oaseslive.maint_cost_budget_adsb

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `WORKCARD_ID` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `ITEM_ID` → `oaseslive.delivery_note_item_header_1.delivery_note_number`
- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `BUDGET_ID` → `oaseslive.maint_cost_budget_adsb.BUDGET_ID`
- `FREQUENCY_ID` → `oaseslive.rfc_frequency_phase_header.rfc_id`
- `PHASE_NUMBER` → `oaseslive.rfc_frequency_phase_header.rfc_id`

**Referenced By (Incoming):**

- `oaseslive.maint_accomplishment_costs.MAINT_COST_ID` → `BUDGET_ID`
- `oaseslive.maint_cost_budget_adsb.BUDGET_ID` → `BUDGET_ID`
- `oaseslive.maint_cost_budget_aircraft.BUDGET_ID` → `BUDGET_ID`
- `oaseslive.maint_cost_budget_cfds.BUDGET_ID` → `BUDGET_ID`
- `oaseslive.maint_cost_budget_costs.BUDGET_ID` → `BUDGET_ID`
- `oaseslive.maint_cost_budget_defects.BUDGET_ID` → `BUDGET_ID`
- `oaseslive.maint_cost_budget_labour_ests.BUDGET_ID` → `BUDGET_ID`
- `oaseslive.maint_cost_budget_materials.BUDGET_ID` → `BUDGET_ID`
- `oaseslive.maint_cost_budget_packages.BUDGET_ID` → `BUDGET_ID`
- `oaseslive.maint_cost_budget_visits.BUDGET_ID` → `BUDGET_ID`
- `oaseslive.maint_cost_budget_workcards.BUDGET_ID` → `BUDGET_ID`
- `oaseslive.maint_hist_associated_costs.MAINT_COST_ID` → `BUDGET_ID`
- `oaseslive.maint_labour_costs.MAINT_COST_ID` → `BUDGET_ID`
- `oaseslive.maint_material_costs.MAINT_COST_ID` → `BUDGET_ID`
- `oaseslive.maint_nrc_costs.MAINT_COST_ID` → `BUDGET_ID`
- `oaseslive.maint_works_order_costs.MAINT_COST_ID` → `BUDGET_ID`
- `oaseslive.maintenance_cost_budgets.BUDGET_ID` → `BUDGET_ID`

### oaseslive.maint_cost_budget_aircraft

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `BUDGET_ID` → `oaseslive.maint_cost_budget_adsb.BUDGET_ID`

### oaseslive.maint_cost_budget_cfds

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `ITEM_ID` → `oaseslive.delivery_note_item_header_1.delivery_note_number`
- `BUDGET_ID` → `oaseslive.maint_cost_budget_adsb.BUDGET_ID`

### oaseslive.maint_cost_budget_costs

**References (Outgoing):**

- `ITEM_ID` → `oaseslive.delivery_note_item_header_1.delivery_note_number`
- `BUDGET_ID` → `oaseslive.maint_cost_budget_adsb.BUDGET_ID`
- `BUDGET_COST_ID` → `oaseslive.maint_cost_budget_costs.BUDGET_COST_ID`
- `COST_TYPE_ID` → `oaseslive.maintenance_cost_types.COST_ID`

**Referenced By (Incoming):**

- `oaseslive.maint_cost_budget_costs.BUDGET_COST_ID` → `BUDGET_COST_ID`
- `oaseslive.maint_cost_budget_defects.BUDGET_COST_ID` → `BUDGET_COST_ID`

### oaseslive.maint_cost_budget_defects

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `BUDGET_ID` → `oaseslive.maint_cost_budget_adsb.BUDGET_ID`
- `BUDGET_COST_ID` → `oaseslive.maint_cost_budget_costs.BUDGET_COST_ID`

### oaseslive.maint_cost_budget_labour_ests

**References (Outgoing):**

- `ITEM_ID` → `oaseslive.delivery_note_item_header_1.delivery_note_number`
- `BUDGET_ID` → `oaseslive.maint_cost_budget_adsb.BUDGET_ID`
- `LABOUR_EST_ID` → `oaseslive.maint_cost_budget_labour_ests.BUDGET_ID`

**Referenced By (Incoming):**

- `oaseslive.maint_cost_budget_labour_ests.LABOUR_EST_ID` → `BUDGET_ID`

### oaseslive.maint_cost_budget_materials

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `MATERIAL_ID` → `oaseslive.amp_material_effectivity.WORKCARD_MATERIAL_ID`
- `ITEM_ID` → `oaseslive.delivery_note_item_header_1.delivery_note_number`
- `BUDGET_ID` → `oaseslive.maint_cost_budget_adsb.BUDGET_ID`

### oaseslive.maint_cost_budget_packages

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `PACKAGE_CODE` → `oaseslive.amp_package_notes.fleet`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `ITEM_ID` → `oaseslive.delivery_note_item_header_1.delivery_note_number`
- `BUDGET_ID` → `oaseslive.maint_cost_budget_adsb.BUDGET_ID`

### oaseslive.maint_cost_budget_visits

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `VISIT_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `ITEM_ID` → `oaseslive.delivery_note_item_header_1.delivery_note_number`
- `BUDGET_ID` → `oaseslive.maint_cost_budget_adsb.BUDGET_ID`

### oaseslive.maint_cost_budget_workcards

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `WORKCARD_ID` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `COST_CODE` → `oaseslive.cost_codes.id`
- `ITEM_ID` → `oaseslive.delivery_note_item_header_1.delivery_note_number`
- `BUDGET_ID` → `oaseslive.maint_cost_budget_adsb.BUDGET_ID`
- `PACKAGE_ITEM_ID` → `oaseslive.package_items.PACKAGE_ITEMS_ID`

### oaseslive.maint_cost_hourly_rate_set

**References (Outgoing):**

- `HOURLY_RATE_SET_ID` → `oaseslive.maint_cost_hourly_rate_set.HOURLY_RATE_SET_ID`
- `CATEGORY_SET_ID` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

**Referenced By (Incoming):**

- `oaseslive.maint_cost_hourly_rate_set.HOURLY_RATE_SET_ID` → `HOURLY_RATE_SET_ID`
- `oaseslive.maint_cost_hourly_rates.HOURLY_RATE_SET_ID` → `HOURLY_RATE_SET_ID`

### oaseslive.maint_cost_hourly_rates

**References (Outgoing):**

- `COST_CODE` → `oaseslive.cost_codes.id`
- `HOURLY_RATE_SET_ID` → `oaseslive.maint_cost_hourly_rate_set.HOURLY_RATE_SET_ID`
- `TIME_CATEGORY_ID` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

### oaseslive.maint_cost_mro_wo_invoices

**References (Outgoing):**

- `INVOICE_ID` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.maint_cost_mro_wo_quotes

**References (Outgoing):**

- `QUOTE_ID` → `oaseslive.cq_quote_cards.quote_id`

### oaseslive.maint_cost_time_categories

**References (Outgoing):**

- `CONTRACT_ID` → `oaseslive.customer_contract_rates.contract_id`
- `TIME_CATEGORY_ID` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`
- `CATEGORY_SET_ID` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

### oaseslive.maint_cost_time_category_set

**References (Outgoing):**

- `CATEGORY_SET_ID` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

**Referenced By (Incoming):**

- `oaseslive.customer_contract_rates.time_category_id` → `CATEGORY_SET_ID`
- `oaseslive.customer_contract_stop_incl.time_category_id` → `CATEGORY_SET_ID`
- `oaseslive.default_labour_rates.time_category_id` → `CATEGORY_SET_ID`
- `oaseslive.email_notification.CATEGORY_ID` → `CATEGORY_SET_ID`
- `oaseslive.email_notification_categories.category_id` → `CATEGORY_SET_ID`
- `oaseslive.maint_associated_cost_aircraft.CATEGORY_ID` → `CATEGORY_SET_ID`
- `oaseslive.maint_cost_hourly_rate_set.CATEGORY_SET_ID` → `CATEGORY_SET_ID`
- `oaseslive.maint_cost_hourly_rates.TIME_CATEGORY_ID` → `CATEGORY_SET_ID`
- `oaseslive.maint_cost_time_categories.TIME_CATEGORY_ID` → `CATEGORY_SET_ID`
- `oaseslive.maint_cost_time_categories.CATEGORY_SET_ID` → `CATEGORY_SET_ID`
- `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID` → `CATEGORY_SET_ID`
- `oaseslive.maintenance_cat_excl_subchap.CATEGORY_ID` → `CATEGORY_SET_ID`
- `oaseslive.maintenance_cat_incl_chapter.CATEGORY_ID` → `CATEGORY_SET_ID`
- `oaseslive.maintenance_cat_incl_parts.CATEGORY_ID` → `CATEGORY_SET_ID`
- `oaseslive.maintenance_cost_cat_fleet.CATEGORY_ID` → `CATEGORY_SET_ID`
- `oaseslive.maintenance_cost_categories.CATEGORY_ID` → `CATEGORY_SET_ID`
- `oaseslive.oeim_invoice_inclusive_hrs.time_category_id` → `CATEGORY_SET_ID`
- `oaseslive.oeim_invoice_snap_con_rates.TIME_CATEGORY_ID` → `CATEGORY_SET_ID`
- `oaseslive.oeim_invoice_snap_time_cats.time_category_id` → `CATEGORY_SET_ID`
- `oaseslive.planners_notes.CATEGORY_ID` → `CATEGORY_SET_ID`
- `oaseslive.planners_notes_categories.category_id` → `CATEGORY_SET_ID`
- `oaseslive.time_categories.time_category_id` → `CATEGORY_SET_ID`

### oaseslive.maint_hist_associated_costs

**References (Outgoing):**

- `MAINT_COST_ID` → `oaseslive.maint_cost_budget_adsb.BUDGET_ID`
- `COST_TYPE_ID` → `oaseslive.maintenance_cost_types.COST_ID`

### oaseslive.maint_historic_defects

**References (Outgoing):**

- `DEFECT_ID` → `oaseslive.defect_extensions.DEFECT_ID`

### oaseslive.maint_labour_costs

**References (Outgoing):**

- `MAINT_COST_ID` → `oaseslive.maint_cost_budget_adsb.BUDGET_ID`

### oaseslive.maint_material_costs

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `MAINT_COST_ID` → `oaseslive.maint_cost_budget_adsb.BUDGET_ID`
- `MATERIAL_COST_ID` → `oaseslive.maint_material_costs.MATERIAL_COST_ID`

**Referenced By (Incoming):**

- `oaseslive.maint_material_costs.MATERIAL_COST_ID` → `MATERIAL_COST_ID`

### oaseslive.maint_nrc_costs

**References (Outgoing):**

- `NRC_NUMBER` → `oaseslive.cq_quote_nrc_access_panels.QUOTE_ID`
- `MAINT_COST_ID` → `oaseslive.maint_cost_budget_adsb.BUDGET_ID`

### oaseslive.maint_pack_pref_cost_cats

**References (Outgoing):**

- `PACKAGE_CODE` → `oaseslive.amp_package_notes.fleet`

### oaseslive.maint_works_order_costs

**References (Outgoing):**

- `MAINT_COST_ID` → `oaseslive.maint_cost_budget_adsb.BUDGET_ID`

### oaseslive.maintenance_cat_excl_subchap

**References (Outgoing):**

- `CATEGORY_ID` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

### oaseslive.maintenance_cat_incl_chapter

**References (Outgoing):**

- `CATEGORY_ID` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

### oaseslive.maintenance_cat_incl_parts

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `CATEGORY_ID` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

### oaseslive.maintenance_cost_budgets

**References (Outgoing):**

- `BUDGET_ID` → `oaseslive.maint_cost_budget_adsb.BUDGET_ID`

### oaseslive.maintenance_cost_cat_fleet

**References (Outgoing):**

- `CATEGORY_ID` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

### oaseslive.maintenance_cost_categories

**References (Outgoing):**

- `CATEGORY_ID` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

### oaseslive.maintenance_cost_entry

**References (Outgoing):**

- `ENTRY_ID` → `oaseslive.batches_by_customs_entry.CUSTOMS_ENTRY_NUMBER`
- `COST_ID` → `oaseslive.cost_codes.id`

### oaseslive.maintenance_cost_invoices

**References (Outgoing):**

- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`
- `INVOICE_ID` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.maintenance_cost_quotes

**References (Outgoing):**

- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `QUOTE_ID` → `oaseslive.cq_quote_cards.quote_id`
- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`

### oaseslive.maintenance_cost_types

**References (Outgoing):**

- `COST_ID` → `oaseslive.cost_codes.id`

**Referenced By (Incoming):**

- `oaseslive.maint_cost_budget_costs.COST_TYPE_ID` → `COST_ID`
- `oaseslive.maint_hist_associated_costs.COST_TYPE_ID` → `COST_ID`

### oaseslive.mandatory_parts

**References (Outgoing):**

- `COST_CODE` → `oaseslive.cost_codes.id`

### oaseslive.manufacturers_work_documents

**References (Outgoing):**

- `DOCUMENT_ID` → `oaseslive.aircraft_documents.AIRCRAFT_DOCUMENT_ID`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`

### oaseslive.marketing_codes

**References (Outgoing):**

- `MARKETING_CODE` → `oaseslive.marketing_codes.MARKETING_CODE`

**Referenced By (Incoming):**

- `oaseslive.marketing_codes.MARKETING_CODE` → `MARKETING_CODE`
- `oaseslive.part_number_marketing_codes.MARKETING_CODE` → `MARKETING_CODE`

### oaseslive.markups

**References (Outgoing):**

- `MARKUP_CODE` → `oaseslive.freight_cost_markups.FREIGHT_COST_MARKUP_ID`

### oaseslive.material_pool_agreement

**References (Outgoing):**

- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`
- `AGREEMENT_ID` → `oaseslive.material_pool_agreement.AGREEMENT_ID`

**Referenced By (Incoming):**

- `oaseslive.material_pool_agreement.AGREEMENT_ID` → `AGREEMENT_ID`
- `oaseslive.material_pool_agreement_ac.AGREEMENT_ID` → `AGREEMENT_ID`
- `oaseslive.material_pool_agreement_pn.AGREEMENT_ID` → `AGREEMENT_ID`

### oaseslive.material_pool_agreement_ac

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `AGREEMENT_ID` → `oaseslive.material_pool_agreement.AGREEMENT_ID`

### oaseslive.material_pool_agreement_pn

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `AGREEMENT_ID` → `oaseslive.material_pool_agreement.AGREEMENT_ID`

### oaseslive.mavis_system_header

**References (Outgoing):**

- `KEY_ID` → `oaseslive.osys_key_to_reportid.OSYSKEY`

### oaseslive.maximum_preload_pick_quantity

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.measurement_alerts_aircraft

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `life_code` → `oaseslive.aircraft_life.AIRCRAFT_CODE`
- `email_notification_cat_id` → `oaseslive.email_notification_categories.category_id`
- `life_code_level_id` → `oaseslive.life_code_levels.life_code_level_id`

### oaseslive.measurement_alerts_fleet

**References (Outgoing):**

- `life_code` → `oaseslive.aircraft_life.AIRCRAFT_CODE`
- `email_notification_cat_id` → `oaseslive.email_notification_categories.category_id`
- `life_code_level_id` → `oaseslive.life_code_levels.life_code_level_id`

### oaseslive.mel_items

**References (Outgoing):**

- `revision_id` → `oaseslive.amp_revisions.revision_id`

### oaseslive.mel_references

**References (Outgoing):**

- `revision_id` → `oaseslive.amp_revisions.revision_id`

### oaseslive.mel_revision_history

**References (Outgoing):**

- `HISTORY_ID` → `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `USER_ID` → `oaseslive.dataset_locks_by_user.USER_ID`

**Referenced By (Incoming):**

- `oaseslive.fleet_header_2.mel_revision_number` → `HISTORY_ID`
- `oaseslive.nrc_defect_details.mel_revision_number` → `HISTORY_ID`
- `oaseslive.tech_log_3.mel_revision_number` → `HISTORY_ID`

### oaseslive.mel_revisions

**References (Outgoing):**

- `revision_id` → `oaseslive.amp_revisions.revision_id`
- `user_id` → `oaseslive.dataset_locks_by_user.USER_ID`

### oaseslive.monthly_loans_in

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.monthly_loans_out

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `DELIVERY_NOTE_NUMBER` → `oaseslive.delivery_note_extended_remarks.DELIVERY_NOTE_NUMBER`

### oaseslive.movement_codes

**References (Outgoing):**

- `movement_code` → `oaseslive.component_movement_hist_life.part_number`

### oaseslive.n_s_extended_part_descriptions

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.netline_import_index

**References (Outgoing):**

- `REPORT_ID` → `oaseslive.amp_report_documents.FLEET`

### oaseslive.no_narrative_default

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.non_stock_parts

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `stock_check_code` → `oaseslive.random_stock_check_bins.WAREHOUSE_CODE`

**Referenced By (Incoming):**

- `oaseslive.preorder_lines.NON_STOCK_PART_NUMBER` → `part_number`
- `oaseslive.shipment_demands.non_stock_part_number` → `part_number`

### oaseslive.non_stock_parts_bkp_oases382

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `STOCK_CHECK_CODE` → `oaseslive.random_stock_check_bins.WAREHOUSE_CODE`

### oaseslive.nrc_access_panels

**References (Outgoing):**

- `access_panel_code` → `oaseslive.amp_access_panel_desc_hdr.fleet`
- `nrc_number` → `oaseslive.cq_quote_nrc_access_panels.QUOTE_ID`

### oaseslive.nrc_defect_details

**References (Outgoing):**

- `corrosion_code` → `oaseslive.corrosion_categories.corrosion_code`
- `defect_id` → `oaseslive.defect_extensions.DEFECT_ID`
- `mel_revision_number` → `oaseslive.mel_revision_history.HISTORY_ID`

### oaseslive.nrc_defect_notes

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `DEFECT_NUMBER` → `oaseslive.defect_extensions.DEFECT_ID`

### oaseslive.nrc_documents

**References (Outgoing):**

- `document_id` → `oaseslive.aircraft_documents.AIRCRAFT_DOCUMENT_ID`
- `nrc_number` → `oaseslive.cq_quote_nrc_access_panels.QUOTE_ID`
- `document_image_id` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`
- `sequence_number` → `oaseslive.nrc_high_sequence_control.KEY_ID`

### oaseslive.nrc_high_sequence_control

**References (Outgoing):**

- `KEY_ID` → `oaseslive.osys_key_to_reportid.OSYSKEY`

**Referenced By (Incoming):**

- `oaseslive.amp_access_panels_by_workcard.sequence_number` → `KEY_ID`
- `oaseslive.amp_documents_by_workcard.sequence_number` → `KEY_ID`
- `oaseslive.amp_documents_by_workcard_bk.SEQUENCE_NUMBER` → `KEY_ID`
- `oaseslive.amp_materials_required_by_wc.sequence_number` → `KEY_ID`
- `oaseslive.amp_packages_by_workcard.sequence_number` → `KEY_ID`
- `oaseslive.amp_visits.sequence_number` → `KEY_ID`
- `oaseslive.amp_wc_aircraft_exclusions.sequence_number` → `KEY_ID`
- `oaseslive.nrc_documents.sequence_number` → `KEY_ID`
- `oaseslive.nrc_requirements_actions.sequence_id` → `KEY_ID`
- `oaseslive.repetitive_defect_tech_logs.SEQUENCE_NUMBER` → `KEY_ID`
- `oaseslive.security_audit_log_meta_data.SEQUENCE_NUMBER` → `KEY_ID`
- `oaseslive.sfdc_deleted_bookings.SEQUENCE_NUMBER` → `KEY_ID`
- `oaseslive.tech_log_rectification_text.SEQUENCE_NUMBER` → `KEY_ID`

### oaseslive.nrc_materials

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `nrc_number` → `oaseslive.cq_quote_nrc_access_panels.QUOTE_ID`

### oaseslive.nrc_print_history

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `DEFECT_NUMBER` → `oaseslive.defect_extensions.DEFECT_ID`
- `PRINT_HISTORY_ID` → `oaseslive.nrc_print_history.PRINT_HISTORY_ID`

**Referenced By (Incoming):**

- `oaseslive.nrc_print_history.PRINT_HISTORY_ID` → `PRINT_HISTORY_ID`

### oaseslive.nrc_properties

**References (Outgoing):**

- `NRC_NUMBER` → `oaseslive.cq_quote_nrc_access_panels.QUOTE_ID`

### oaseslive.nrc_rectification_notes

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `DEFECT_NUMBER` → `oaseslive.defect_extensions.DEFECT_ID`

### oaseslive.nrc_requirements_actions

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `defect_number` → `oaseslive.defect_extensions.DEFECT_ID`
- `sequence_id` → `oaseslive.nrc_high_sequence_control.KEY_ID`

**Referenced By (Incoming):**

- `oaseslive.condition_pick_table.REQUIREMENT_NUMBER` → `aircraft_short_reg`
- `oaseslive.consumable_history.requirement_number` → `aircraft_short_reg`
- `oaseslive.credit_works_order_cards.requirement_number` → `aircraft_short_reg`
- `oaseslive.delivery_note_item_header_1.requirement_number` → `aircraft_short_reg`
- `oaseslive.dmg_rpr_repair_req_details.REQUIREMENT_NUMBER` → `aircraft_short_reg`
- `oaseslive.dues_register.requirement_number` → `aircraft_short_reg`
- `oaseslive.oeim_credit_warranty.requirement_number` → `aircraft_short_reg`
- `oaseslive.oeim_invoice_materials.requirement_number` → `aircraft_short_reg`
- `oaseslive.oeim_invoice_warranty.requirement_number` → `aircraft_short_reg`
- `oaseslive.oeim_invoice_warranty_refunds.requirement_number` → `aircraft_short_reg`
- `oaseslive.order_line_requirement_xref.REQUIREMENT_NUMBER` → `aircraft_short_reg`
- `oaseslive.order_requirement_allocation.requirement_number` → `aircraft_short_reg`
- `oaseslive.part_xref_to_pick_history.REQUIREMENT_NUMBER` → `aircraft_short_reg`
- `oaseslive.pick_hist_7890_bkp.REQUIREMENT_NUMBER` → `aircraft_short_reg`
- `oaseslive.pick_history.REQUIREMENT_NUMBER` → `aircraft_short_reg`
- `oaseslive.preorder_line_requirement_xref.REQUIREMENT_NUMBER` → `aircraft_short_reg`
- `oaseslive.requirement_planners_notes.REQUIREMENT_NUMBER` → `aircraft_short_reg`
- `oaseslive.requirement_recharge_details.REQUIREMENT_NUMBER` → `aircraft_short_reg`
- `oaseslive.requirement_to_rfq_xref.requirement_number` → `aircraft_short_reg`
- `oaseslive.requirements.requirement_number` → `aircraft_short_reg`
- `oaseslive.rfq_requirement_xref.REQUIREMENT_NUMBER` → `aircraft_short_reg`
- `oaseslive.rotable_history.requirement_number` → `aircraft_short_reg`
- `oaseslive.sales_order_lines.requirement_number` → `aircraft_short_reg`
- `oaseslive.shelf_life_expiry_req_codes.REQUIREMENT_CODE` → `aircraft_short_reg`
- `oaseslive.shipment_requirement_demands.requirement_number` → `aircraft_short_reg`

### oaseslive.nrc_status_history

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `STATUS_CODE` → `oaseslive.amp_revision_status.REVISION_STATUS_ID`
- `DEFECT_NUMBER` → `oaseslive.defect_extensions.DEFECT_ID`
- `STATUS_HISTORY_ID` → `oaseslive.nrc_status_history.STATUS_HISTORY_ID`

**Referenced By (Incoming):**

- `oaseslive.nrc_status_history.STATUS_HISTORY_ID` → `STATUS_HISTORY_ID`

### oaseslive.nrc_tools

**References (Outgoing):**

- `batch_number` → `oaseslive.batch_file_header.KEY`
- `nrc_number` → `oaseslive.cq_quote_nrc_access_panels.QUOTE_ID`

### oaseslive.nrc_workcard_narrative

**References (Outgoing):**

- `NRC_NUMBER` → `oaseslive.cq_quote_nrc_access_panels.QUOTE_ID`

### oaseslive.nrc_xref_to_scheduled_workcard

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `NRC_NUMBER` → `oaseslive.cq_quote_nrc_access_panels.QUOTE_ID`
- `DEFECT_NUMBER` → `oaseslive.defect_extensions.DEFECT_ID`

### oaseslive.oases_message_log

**References (Outgoing):**

- `LOG_NUMBER` → `oaseslive.amp_data_migration_log.LOG_NUMBER`

### oaseslive.oases_reports

**References (Outgoing):**

- `REPORT_ID` → `oaseslive.amp_report_documents.FLEET`

### oaseslive.oeim_booking_base_data

**Referenced By (Incoming):**

- `oaseslive.oeim_invoice_snap_sfdc_book.BOOKING_ID` → `BOOKING_ROUNDING_UP_MINS`
- `oaseslive.sfdc_activity.BOOKING_ID` → `BOOKING_ROUNDING_UP_MINS`
- `oaseslive.sfdc_bookings.BOOKING_ID` → `BOOKING_ROUNDING_UP_MINS`

### oaseslive.oeim_credit_warranty

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `card_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `batch_number` → `oaseslive.batch_file_header.KEY`
- `order_number` → `oaseslive.batch_orders.BATCH_NUMBER`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `requirement_number` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`

### oaseslive.oeim_invoice

**References (Outgoing):**

- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.oeim_invoice_cards

**References (Outgoing):**

- `card_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `package_code` → `oaseslive.amp_package_notes.fleet`
- `invoice_number` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.oeim_invoice_fixed_charges

**References (Outgoing):**

- `cost_code` → `oaseslive.cost_codes.id`
- `invoice_number` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.oeim_invoice_inclusive_hrs

**References (Outgoing):**

- `card_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `invoice_number` → `oaseslive.invoice_categories.INVOICE_CATEGORY`
- `time_category_id` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

### oaseslive.oeim_invoice_materials

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `card_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `package_code` → `oaseslive.amp_package_notes.fleet`
- `batch_number` → `oaseslive.batch_file_header.KEY`
- `order_number` → `oaseslive.batch_orders.BATCH_NUMBER`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `invoice_number` → `oaseslive.invoice_categories.INVOICE_CATEGORY`
- `requirement_number` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`

### oaseslive.oeim_invoice_packages

**References (Outgoing):**

- `package_code` → `oaseslive.amp_package_notes.fleet`
- `cost_code` → `oaseslive.cost_codes.id`
- `invoice_number` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.oeim_invoice_snap_con_rates

**References (Outgoing):**

- `COST_CODE` → `oaseslive.cost_codes.id`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`
- `TIME_CATEGORY_ID` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

### oaseslive.oeim_invoice_snap_cost_codes

**References (Outgoing):**

- `COST_CODE` → `oaseslive.cost_codes.id`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.oeim_invoice_snap_currencies

**References (Outgoing):**

- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.oeim_invoice_snap_departments

**References (Outgoing):**

- `DEPARTMENT_ID` → `oaseslive.departments.DEPARTMENT_ID`
- `EXPORT_CODE` → `oaseslive.export_codes.EXPORT_ID`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.oeim_invoice_snap_employees

**References (Outgoing):**

- `EMPLOYEE_NUMBER` → `oaseslive.defect_stage_employees.defect_id`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.oeim_invoice_snap_part_master

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.oeim_invoice_snap_pay_types

**References (Outgoing):**

- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`
- `PAYMENT_CODE` → `oaseslive.payment_types.payment_code`

### oaseslive.oeim_invoice_snap_pm_bkup

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.oeim_invoice_snap_public_hol

**References (Outgoing):**

- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.oeim_invoice_snap_serl_master

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`
- `LONG_SERIAL_NUMBER` → `oaseslive.long_serial_number_xref.part_number`

### oaseslive.oeim_invoice_snap_sfdc_book

**References (Outgoing):**

- `TASK_NUMBER` → `oaseslive.amp_datmig_comp_task_lookup.FLEET`
- `DEFECT_CODE` → `oaseslive.defect_extensions.DEFECT_ID`
- `EMPLOYEE_NUMBER` → `oaseslive.defect_stage_employees.defect_id`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`
- `BOOKING_ID` → `oaseslive.oeim_booking_base_data.BOOKING_ROUNDING_UP_MINS`

### oaseslive.oeim_invoice_snap_time_cats

**References (Outgoing):**

- `invoice_number` → `oaseslive.invoice_categories.INVOICE_CATEGORY`
- `time_category_id` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

### oaseslive.oeim_invoice_snap_time_crits

**References (Outgoing):**

- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.oeim_invoice_snap_users

**References (Outgoing):**

- `OASES_ID` → `oaseslive.cfd_categorires_bkpoases405.CFD_CATEGORY`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.oeim_invoice_snap_vat_codes

**References (Outgoing):**

- `VAT_CODE` → `oaseslive.amp_workcard_activations.workcard_activation_id`
- `EXPORT_ID` → `oaseslive.export_codes.EXPORT_ID`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.oeim_invoice_warranty

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `card_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `package_code` → `oaseslive.amp_package_notes.fleet`
- `batch_number` → `oaseslive.batch_file_header.KEY`
- `order_number` → `oaseslive.batch_orders.BATCH_NUMBER`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `invoice_number` → `oaseslive.invoice_categories.INVOICE_CATEGORY`
- `requirement_number` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`

### oaseslive.oeim_invoice_warranty_refunds

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `card_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `batch_number` → `oaseslive.batch_file_header.KEY`
- `order_number` → `oaseslive.batch_orders.BATCH_NUMBER`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `invoice_number` → `oaseslive.invoice_categories.INVOICE_CATEGORY`
- `requirement_number` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`

### oaseslive.oeim_invoice_works_orders

**References (Outgoing):**

- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.oeim_quote_dismissed

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `PACKAGE_CODE` → `oaseslive.amp_package_notes.fleet`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.oeim_transaction_log_details

**References (Outgoing):**

- `DETAIL_NUMBER` → `oaseslive.aircraft_lease_details.aircraft_code`
- `LOG_NUMBER` → `oaseslive.amp_data_migration_log.LOG_NUMBER`

### oaseslive.oeim_transaction_log_header

**References (Outgoing):**

- `LOG_NUMBER` → `oaseslive.amp_data_migration_log.LOG_NUMBER`

### oaseslive.ord_po_unit_conv_delta1827

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

### oaseslive.order_change_history

**References (Outgoing):**

- `HISTORY_ID` → `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `PREORDER_ID` → `oaseslive.preorder_line_requirement_xref.PREORDER_ID`

### oaseslive.order_customs_info

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

### oaseslive.order_delivery_note_remarks

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

### oaseslive.order_email_chasing

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

### oaseslive.order_goods_received

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `order_number` → `oaseslive.batch_orders.BATCH_NUMBER`
- `goods_received_number` → `oaseslive.goods_received_sheet_document.BATCH_NUMBER`

### oaseslive.order_goods_received_invoices

**References (Outgoing):**

- `VAT_CODE` → `oaseslive.amp_workcard_activations.workcard_activation_id`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.order_header_1

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `order_number` → `oaseslive.batch_orders.BATCH_NUMBER`
- `company_code` → `oaseslive.company_codes.COMPANY_CODE`
- `currency_code` → `oaseslive.currency_codes.currency_code`
- `release_code` → `oaseslive.release_codes.RELEASE_CODE`

### oaseslive.order_header_2

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `WORKS_ORDER_NUMBER` → `oaseslive.credit_works_order_cards.credit_note_no`

### oaseslive.order_header_3

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `DELIVERY_NOTE_NUMBER` → `oaseslive.delivery_note_extended_remarks.DELIVERY_NOTE_NUMBER`

### oaseslive.order_header_4

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `EMPLOYEE_NUMBER` → `oaseslive.defect_stage_employees.defect_id`

### oaseslive.order_history

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `CONDITION_CODE` → `oaseslive.condition_codes.condition_code`
- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.order_line_additional_info

**References (Outgoing):**

- `AIRWAY_BILL_NUMBER` → `oaseslive.airway_bill_references.AWB_ID`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `CONDITION_CODE` → `oaseslive.condition_codes.condition_code`
- `RELEASE_CODE` → `oaseslive.release_codes.RELEASE_CODE`

**Referenced By (Incoming):**

- `oaseslive.rp_employee_calendar_addition.addition_id` → `ORDER_NUMBER`

### oaseslive.order_line_additional_info_2

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

### oaseslive.order_line_notes

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

### oaseslive.order_line_quotes_data

**References (Outgoing):**

- `VAT_CODE` → `oaseslive.amp_workcard_activations.workcard_activation_id`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`

### oaseslive.order_line_requirement_xref

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `REQUIREMENT_NUMBER` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`

### oaseslive.order_line_weight_dimension

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `DIMENSION_ID` → `oaseslive.order_line_weight_dimension.DIMENSION_ID`

**Referenced By (Incoming):**

- `oaseslive.order_line_weight_dimension.DIMENSION_ID` → `DIMENSION_ID`

### oaseslive.order_lines

**References (Outgoing):**

- `vat_code` → `oaseslive.amp_workcard_activations.workcard_activation_id`
- `order_number` → `oaseslive.batch_orders.BATCH_NUMBER`
- `bin_number` → `oaseslive.bins.bin_number`
- `movement_code` → `oaseslive.component_movement_hist_life.part_number`
- `strip_report_number` → `oaseslive.strip_report_findings_text.STRIP_REPORT_NUMBER`

### oaseslive.order_numbers_by_supplier

**References (Outgoing):**

- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

### oaseslive.order_print_date

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

### oaseslive.order_purchase_unit_conversion

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

### oaseslive.order_requirement_allocation

**References (Outgoing):**

- `order_number` → `oaseslive.batch_orders.BATCH_NUMBER`
- `requirement_number` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`

**Referenced By (Incoming):**

- `oaseslive.rp_employee_allocation.ALLOCATION_ID` → `order_number`

### oaseslive.order_standard_text_blocks

**References (Outgoing):**

- `BLOCK_NUMBER` → `oaseslive.block_countries.block_code`

### oaseslive.order_supplier_approval

**References (Outgoing):**

- `SUPPLIER_APPROVAL_NUMBER` → `oaseslive.account_supplier_approvals.account_code`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

### oaseslive.order_text

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

### oaseslive.order_workshop_works_orders

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

### oaseslive.orders_by_due_date

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

### oaseslive.orders_to_part_number_xref

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

### oaseslive.ordr_goods_bkp

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `GOODS_RECEIVED_NUMBER` → `oaseslive.goods_received_sheet_document.BATCH_NUMBER`

### oaseslive.original_purchase_values

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `currency_code` → `oaseslive.currency_codes.currency_code`

### oaseslive.osys_defect_act_to_defect_id

**References (Outgoing):**

- `DEFECT_ID` → `oaseslive.defect_extensions.DEFECT_ID`

### oaseslive.osys_defect_to_defect_id

**References (Outgoing):**

- `DEFECT_NUMBER` → `oaseslive.defect_extensions.DEFECT_ID`
- `DEFECT_ID` → `oaseslive.defect_extensions.DEFECT_ID`

### oaseslive.osys_defect_to_tech_log_line

**References (Outgoing):**

- `DEFECT_NUMBER` → `oaseslive.defect_extensions.DEFECT_ID`

### oaseslive.osys_key_to_reportid

**References (Outgoing):**

- `REPORT_ID` → `oaseslive.amp_report_documents.FLEET`

**Referenced By (Incoming):**

- `oaseslive.account_system_header.KEY_ID` → `OSYSKEY`
- `oaseslive.invoice_system_header.KEY_ID` → `OSYSKEY`
- `oaseslive.lasers_system_header.KEY_ID` → `OSYSKEY`
- `oaseslive.mavis_system_header.KEY_ID` → `OSYSKEY`
- `oaseslive.nrc_high_sequence_control.KEY_ID` → `OSYSKEY`
- `oaseslive.rd_xref_to_tech_logs.KEY_ID` → `OSYSKEY`
- `oaseslive.sales_order_parameters.KEY_ID` → `OSYSKEY`
- `oaseslive.system_header_icarus.KEY_ID` → `OSYSKEY`
- `oaseslive.test_table.KEY_ID` → `OSYSKEY`

### oaseslive.outstation_codes

**References (Outgoing):**

- `OUTSTATION_CODE` → `oaseslive.outstation_codes.OUTSTATION_CODE`

**Referenced By (Incoming):**

- `oaseslive.outstation_codes.OUTSTATION_CODE` → `OUTSTATION_CODE`

### oaseslive.package

**References (Outgoing):**

- `PACKAGE_ID` → `oaseslive.amp_package_notes.fleet`
- `SHIPMENT_ID` → `oaseslive.shipment.SHIPMENT_ID`

### oaseslive.package_items

**References (Outgoing):**

- `PACKAGE_ID` → `oaseslive.amp_package_notes.fleet`
- `ITEM_ID` → `oaseslive.delivery_note_item_header_1.delivery_note_number`
- `PACKAGE_ITEMS_ID` → `oaseslive.package_items.PACKAGE_ITEMS_ID`

**Referenced By (Incoming):**

- `oaseslive.maint_cost_budget_workcards.PACKAGE_ITEM_ID` → `PACKAGE_ITEMS_ID`
- `oaseslive.package_items.PACKAGE_ITEMS_ID` → `PACKAGE_ITEMS_ID`

### oaseslive.paragraph_cancels

**References (Outgoing):**

- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `PARAGRAPH_ID` → `oaseslive.paragraph_cancels.RFC_ID`

**Referenced By (Incoming):**

- `oaseslive.accomp_bkup.PARAGRAPH_ID` → `RFC_ID`
- `oaseslive.accomp_hist_delta_1763.PARAGRAPH_ID` → `RFC_ID`
- `oaseslive.accomp_hist_lost_sched.PARAGRAPH_ID` → `RFC_ID`
- `oaseslive.accomplishment_history.PARAGRAPH_ID` → `RFC_ID`
- `oaseslive.dmg_rpr_inspections.PARAGRAPH_ID` → `RFC_ID`
- `oaseslive.dmg_rpr_interim_repairs.PARAGRAPH_ID` → `RFC_ID`
- `oaseslive.dmg_rpr_permanent_repairs.PARAGRAPH_ID` → `RFC_ID`
- `oaseslive.dmg_rpr_time_limited_repairs.PARAGRAPH_ID` → `RFC_ID`
- `oaseslive.paragraph_cancels.PARAGRAPH_ID` → `RFC_ID`
- `oaseslive.rfc_aircraft.paragraph_id` → `RFC_ID`
- `oaseslive.rfc_components.paragraph_id` → `RFC_ID`
- `oaseslive.rfc_frequency_phase_header.paragraph_id` → `RFC_ID`
- `oaseslive.rfc_frequency_phase_limits.paragraph_id` → `RFC_ID`
- `oaseslive.rfc_frequency_phases.paragraph_id` → `RFC_ID`
- `oaseslive.rfc_paragraphs.paragraph_id` → `RFC_ID`
- `oaseslive.temp_rfc_paragraphs.PARAGRAPH_ID` → `RFC_ID`

### oaseslive.part_applicability_codes

**References (Outgoing):**

- `APPLICABILITY_CODE` → `oaseslive.amp_workcard_lcl_applicability.LIFE_CODE_LEVEL_ID`

### oaseslive.part_change_warning_chapters

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.part_change_warnings

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.part_customs_tariff_territory

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `CUSTOMS_TARIFF_CODE` → `oaseslive.customs_tariff_codes.customs_tariff_code`

### oaseslive.part_master

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `stock_check_code` → `oaseslive.random_stock_check_bins.WAREHOUSE_CODE`

### oaseslive.part_master_bkp_oases382

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `STOCK_CHECK_CODE` → `oaseslive.random_stock_check_bins.WAREHOUSE_CODE`

### oaseslive.part_number_amendment_history

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `USER_ID` → `oaseslive.dataset_locks_by_user.USER_ID`

### oaseslive.part_number_chapters

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.part_number_chapters_dj-82

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.part_number_essentiality_codes

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `ESSENTIALITY_CODE` → `oaseslive.part_number_essentiality_codes.PART_NUMBER`

**Referenced By (Incoming):**

- `oaseslive.part_number_essentiality_codes.ESSENTIALITY_CODE` → `PART_NUMBER`

### oaseslive.part_number_marketing_codes

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `MARKETING_CODE` → `oaseslive.marketing_codes.MARKETING_CODE`

### oaseslive.part_number_order_retention

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.part_number_owner_float_levels

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.part_number_properties

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.part_number_properties_serials

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.part_number_shelf_life_details

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `COMPONENT_LIFE_LIMIT_ID` → `oaseslive.component_life_limits.component_life_limit_id`

### oaseslive.part_number_technical_notes

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.part_number_vat_codes

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `VAT_CODE` → `oaseslive.amp_workcard_activations.workcard_activation_id`

### oaseslive.part_serial_documents

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `DOCUMENT_IMAGE_ID` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`
- `PART_SERIAL_DOCUMENT_ID` → `oaseslive.part_serial_documents.PART_SERIAL_DOCUMENT_ID`

**Referenced By (Incoming):**

- `oaseslive.part_serial_documents.PART_SERIAL_DOCUMENT_ID` → `PART_SERIAL_DOCUMENT_ID`

### oaseslive.part_serial_master_list

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.part_xref_to_pick_history

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `PICK_NUMBER` → `oaseslive.condition_pick_table.PART_NUMBER`
- `REQUIREMENT_NUMBER` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`

### oaseslive.parts_customs_tariff_codes

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `CUSTOMS_TARIFF_CODE` → `oaseslive.customs_tariff_codes.customs_tariff_code`

### oaseslive.parts_freight_tiered_markups

**References (Outgoing):**

- `FREIGHT_COST_MARKUP_ID` → `oaseslive.freight_cost_markups.FREIGHT_COST_MARKUP_ID`

### oaseslive.parts_received_without_cost

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

### oaseslive.parts_requiring_export_licence

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.payment_types

**References (Outgoing):**

- `payment_code` → `oaseslive.payment_types.payment_code`

**Referenced By (Incoming):**

- `oaseslive.oeim_invoice_snap_pay_types.PAYMENT_CODE` → `payment_code`
- `oaseslive.payment_types.payment_code` → `payment_code`

### oaseslive.pdc_import_index

**References (Outgoing):**

- `report_id` → `oaseslive.amp_report_documents.FLEET`

### oaseslive.pick_hist_7890_bkp

**References (Outgoing):**

- `ALTERNATE_PART_NUMBER` → `oaseslive.alternate_parts.PART_NUMBER`
- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `PICK_NUMBER` → `oaseslive.condition_pick_table.PART_NUMBER`
- `REQUIREMENT_NUMBER` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`

### oaseslive.pick_history

**References (Outgoing):**

- `ALTERNATE_PART_NUMBER` → `oaseslive.alternate_parts.PART_NUMBER`
- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `PICK_NUMBER` → `oaseslive.condition_pick_table.PART_NUMBER`
- `REQUIREMENT_NUMBER` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`

### oaseslive.pirep_index_data

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.planners_notes

**References (Outgoing):**

- `STATUS_ID` → `oaseslive.amp_revision_status.REVISION_STATUS_ID`
- `CATEGORY_ID` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`
- `NOTES_XREF_ID` → `oaseslive.planners_notes_xref.CATEGORY_XREF_ID`

**Referenced By (Incoming):**

- `oaseslive.requirements.planner_id` → `NOTES_XREF_ID`

### oaseslive.planners_notes_categories

**References (Outgoing):**

- `category_id` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

### oaseslive.planners_notes_statuses

**References (Outgoing):**

- `STATUS_ID` → `oaseslive.amp_revision_status.REVISION_STATUS_ID`

### oaseslive.planners_notes_xref

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `ALERT_NUMBER` → `oaseslive.alert_colors.ALERT_TYPE_ID`
- `VISIT_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `PACKAGE_CODE` → `oaseslive.amp_package_notes.fleet`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `WORKCARD_INTERVAL_ID` → `oaseslive.amp_workcard_intervals_limits.workcard_interval_id`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`

**Referenced By (Incoming):**

- `oaseslive.planners_notes.NOTES_XREF_ID` → `CATEGORY_XREF_ID`

### oaseslive.prefered_bins

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.preferred_suppliers_by_part

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`

### oaseslive.preorder_line_requirement_xref

**References (Outgoing):**

- `REQUIREMENT_NUMBER` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`
- `PREORDER_ID` → `oaseslive.preorder_line_requirement_xref.PREORDER_ID`

**Referenced By (Incoming):**

- `oaseslive.order_change_history.PREORDER_ID` → `PREORDER_ID`
- `oaseslive.preorder_line_requirement_xref.PREORDER_ID` → `PREORDER_ID`
- `oaseslive.preorder_line_stock_info.PREORDER_ID` → `PREORDER_ID`
- `oaseslive.preorder_lines.PREORDER_ID` → `PREORDER_ID`
- `oaseslive.preorders.PREORDER_ID` → `PREORDER_ID`
- `oaseslive.sap_order_header.PREORDER_ID` → `PREORDER_ID`
- `oaseslive.sap_order_line.PREORDER_ID` → `PREORDER_ID`

### oaseslive.preorder_line_stock_info

**References (Outgoing):**

- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `BIN_NUMBER` → `oaseslive.bins.bin_number`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `MOVEMENT_CODE` → `oaseslive.component_movement_hist_life.part_number`
- `PREORDER_ID` → `oaseslive.preorder_line_requirement_xref.PREORDER_ID`

### oaseslive.preorder_lines

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `VAT_CODE` → `oaseslive.amp_workcard_activations.workcard_activation_id`
- `CONDITION_CODE` → `oaseslive.condition_codes.condition_code`
- `NON_STOCK_PART_NUMBER` → `oaseslive.non_stock_parts.part_number`
- `PREORDER_ID` → `oaseslive.preorder_line_requirement_xref.PREORDER_ID`
- `RELEASE_CODE` → `oaseslive.release_codes.RELEASE_CODE`

### oaseslive.preorders

**References (Outgoing):**

- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `COMPANY_CODE` → `oaseslive.company_codes.COMPANY_CODE`
- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`
- `EMPLOYEE_NUMBER` → `oaseslive.defect_stage_employees.defect_id`
- `PREORDER_ID` → `oaseslive.preorder_line_requirement_xref.PREORDER_ID`

### oaseslive.price_codes

**References (Outgoing):**

- `PRICE_CODE` → `oaseslive.price_codes.PRICE_CODE`

**Referenced By (Incoming):**

- `oaseslive.price_codes.PRICE_CODE` → `PRICE_CODE`

### oaseslive.price_types

**References (Outgoing):**

- `price_type_code` → `oaseslive.price_types.price_type_code`

**Referenced By (Incoming):**

- `oaseslive.ie96_historic.PRICE_TYPE_CODE` → `price_type_code`
- `oaseslive.price_types.price_type_code` → `price_type_code`
- `oaseslive.sales_prices.price_type_code` → `price_type_code`

### oaseslive.public_holidays

**Referenced By (Incoming):**

- `oaseslive.rp_block_resource_days.DAY_ID` → `HOLIDAY_DATE`
- `oaseslive.rp_block_resource_days.DAY_NUMBER` → `HOLIDAY_DATE`

### oaseslive.purchase_demand_by_part

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.quote_email_chasing

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

### oaseslive.quotes_by_part

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`

### oaseslive.quotes_for_part_by_account

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`

### oaseslive.random_stock_check_bins

**References (Outgoing):**

- `WAREHOUSE_CODE` → `oaseslive.account_available_warehouses.ACCOUNT_CODE`
- `BIN_NUMBER` → `oaseslive.bins.bin_number`

**Referenced By (Incoming):**

- `oaseslive.non_stock_parts.stock_check_code` → `WAREHOUSE_CODE`
- `oaseslive.non_stock_parts_bkp_oases382.STOCK_CHECK_CODE` → `WAREHOUSE_CODE`
- `oaseslive.part_master.stock_check_code` → `WAREHOUSE_CODE`
- `oaseslive.part_master_bkp_oases382.STOCK_CHECK_CODE` → `WAREHOUSE_CODE`

### oaseslive.random_stock_check_date

**References (Outgoing):**

- `WAREHOUSE_CODE` → `oaseslive.account_available_warehouses.ACCOUNT_CODE`

### oaseslive.random_stock_check_log

**References (Outgoing):**

- `WAREHOUSE_CODE` → `oaseslive.account_available_warehouses.ACCOUNT_CODE`

### oaseslive.random_stock_check_parts

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `WAREHOUSE_CODE` → `oaseslive.account_available_warehouses.ACCOUNT_CODE`

### oaseslive.rd_xref_to_tech_logs

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `ALERT_NUMBER` → `oaseslive.alert_colors.ALERT_TYPE_ID`
- `STATUS_CODE` → `oaseslive.amp_revision_status.REVISION_STATUS_ID`
- `KEY_ID` → `oaseslive.osys_key_to_reportid.OSYSKEY`

### oaseslive.rdi_history

**References (Outgoing):**

- `ALERT_NUMBER` → `oaseslive.alert_colors.ALERT_TYPE_ID`
- `USER_ID` → `oaseslive.dataset_locks_by_user.USER_ID`

**Referenced By (Incoming):**

- `oaseslive.rdi_to_nrc.RDI_NUMBER` → `ALERT_NUMBER`

### oaseslive.rdi_to_nrc

**References (Outgoing):**

- `NRC_NUMBER` → `oaseslive.cq_quote_nrc_access_panels.QUOTE_ID`
- `RDI_NUMBER` → `oaseslive.rdi_history.ALERT_NUMBER`

### oaseslive.release_codes

**References (Outgoing):**

- `RELEASE_CODE` → `oaseslive.release_codes.RELEASE_CODE`

**Referenced By (Incoming):**

- `oaseslive.order_header_1.release_code` → `RELEASE_CODE`
- `oaseslive.order_line_additional_info.RELEASE_CODE` → `RELEASE_CODE`
- `oaseslive.preorder_lines.RELEASE_CODE` → `RELEASE_CODE`
- `oaseslive.release_codes.RELEASE_CODE` → `RELEASE_CODE`
- `oaseslive.requests_for_quotes_lines.RELEASE_CODE` → `RELEASE_CODE`

### oaseslive.release_to_service_statement

**Referenced By (Incoming):**

- `oaseslive.account_location_header_6.state_code` → `RELEASE_STATEMENT`

### oaseslive.reliability_report_logo_desc

**References (Outgoing):**

- `DOCUMENT_IMAGE_ID` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`
- `LOGO_DESC_ID` → `oaseslive.reliability_report_logo_desc.LOGO_DESC_ID`

**Referenced By (Incoming):**

- `oaseslive.reliability_report_logo_desc.LOGO_DESC_ID` → `LOGO_DESC_ID`

### oaseslive.removals

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.repair_approval_data

**References (Outgoing):**

- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `MOVEMENT_CODE` → `oaseslive.component_movement_hist_life.part_number`

### oaseslive.repetitive_defect_header_1

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `ALERT_NUMBER` → `oaseslive.alert_colors.ALERT_TYPE_ID`

### oaseslive.repetitive_defect_header_2

**References (Outgoing):**

- `ALERT_NUMBER` → `oaseslive.alert_colors.ALERT_TYPE_ID`

### oaseslive.repetitive_defect_narrative

**References (Outgoing):**

- `ALERT_NUMBER` → `oaseslive.alert_colors.ALERT_TYPE_ID`
- `USER_ID` → `oaseslive.dataset_locks_by_user.USER_ID`

### oaseslive.repetitive_defect_tech_logs

**References (Outgoing):**

- `ALERT_NUMBER` → `oaseslive.alert_colors.ALERT_TYPE_ID`
- `SEQUENCE_NUMBER` → `oaseslive.nrc_high_sequence_control.KEY_ID`

### oaseslive.req_priority_desc_oases_1228

**References (Outgoing):**

- `PRIORITY_ID` → `oaseslive.req_priority_desc_oases_1228.PRIORITY_ID`

**Referenced By (Incoming):**

- `oaseslive.req_priority_desc_oases_1228.PRIORITY_ID` → `PRIORITY_ID`
- `oaseslive.requirement_priority_codes.priority_code` → `PRIORITY_ID`
- `oaseslive.requirement_priority_desc.PRIORITY_ID` → `PRIORITY_ID`
- `oaseslive.requirement_priority_leadtimes.PRIORITY_CODE` → `PRIORITY_ID`
- `oaseslive.requirement_priority_sla.PRIORITY_CODE` → `PRIORITY_ID`

### oaseslive.requests_for_quotes

**References (Outgoing):**

- `RFQ_NUMBER` → `oaseslive.requirement_to_rfq_xref.requirement_number`

### oaseslive.requests_for_quotes_lines

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `MOVEMENT_CODE` → `oaseslive.component_movement_hist_life.part_number`
- `RELEASE_CODE` → `oaseslive.release_codes.RELEASE_CODE`
- `RFQ_NUMBER` → `oaseslive.requirement_to_rfq_xref.requirement_number`

### oaseslive.requests_for_quotes_notes

**References (Outgoing):**

- `RFQ_NUMBER` → `oaseslive.requirement_to_rfq_xref.requirement_number`

### oaseslive.requirement_planners_notes

**References (Outgoing):**

- `REQUIREMENT_NUMBER` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`

### oaseslive.requirement_priority_codes

**References (Outgoing):**

- `priority_code` → `oaseslive.req_priority_desc_oases_1228.PRIORITY_ID`

### oaseslive.requirement_priority_desc

**References (Outgoing):**

- `PRIORITY_ID` → `oaseslive.req_priority_desc_oases_1228.PRIORITY_ID`

### oaseslive.requirement_priority_leadtimes

**References (Outgoing):**

- `PRIORITY_CODE` → `oaseslive.req_priority_desc_oases_1228.PRIORITY_ID`

### oaseslive.requirement_priority_sla

**References (Outgoing):**

- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `PRIORITY_CODE` → `oaseslive.req_priority_desc_oases_1228.PRIORITY_ID`

### oaseslive.requirement_recharge_details

**References (Outgoing):**

- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `COST_CODE` → `oaseslive.cost_codes.id`
- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`
- `REQUIREMENT_NUMBER` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`
- `STRIP_REPORT_NUMBER` → `oaseslive.strip_report_findings_text.STRIP_REPORT_NUMBER`

### oaseslive.requirement_source_codes

**References (Outgoing):**

- `SOURCE_CODE` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`

### oaseslive.requirement_to_rfq_xref

**References (Outgoing):**

- `requirement_number` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`
- `rfq_number` → `oaseslive.requirement_to_rfq_xref.requirement_number`

**Referenced By (Incoming):**

- `oaseslive.requests_for_quotes.RFQ_NUMBER` → `requirement_number`
- `oaseslive.requests_for_quotes_lines.RFQ_NUMBER` → `requirement_number`
- `oaseslive.requests_for_quotes_notes.RFQ_NUMBER` → `requirement_number`
- `oaseslive.requirement_to_rfq_xref.rfq_number` → `requirement_number`
- `oaseslive.rfq_by_part_number.RFQ_NUMBER` → `requirement_number`
- `oaseslive.rfq_history.rfq_number` → `requirement_number`
- `oaseslive.rfq_quote_received.RFQ_NUMBER` → `requirement_number`
- `oaseslive.rfq_quote_received_notes.rfq_number` → `requirement_number`
- `oaseslive.rfq_requirement_xref.RFQ_NUMBER` → `requirement_number`
- `oaseslive.rfq_supplier_details.rfq_number` → `requirement_number`
- `oaseslive.rfq_supplier_notes.RFQ_NUMBER` → `requirement_number`
- `oaseslive.rfq_to_order_xref.rfq_number` → `requirement_number`
- `oaseslive.sales_request_quote_detail.rfq_number` → `requirement_number`

### oaseslive.requirements

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `alert_number` → `oaseslive.alert_colors.ALERT_TYPE_ID`
- `cfd_number` → `oaseslive.cfd_categories.cfd_category`
- `sales_order_number` → `oaseslive.customer_sales_order_xref.CUSTOMER_SALES_ORDER_NUMBER`
- `defect_number` → `oaseslive.defect_extensions.DEFECT_ID`
- `defect_id` → `oaseslive.defect_extensions.DEFECT_ID`
- `requirement_number` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`
- `planner_id` → `oaseslive.planners_notes.NOTES_XREF_ID`

### oaseslive.rfc_accomplishment

**References (Outgoing):**

- `accomplishment_code` → `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID`

### oaseslive.rfc_aircraft

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `na_id` → `oaseslive.alternate_parts.PART_NUMBER`
- `rfc_id` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `paragraph_id` → `oaseslive.paragraph_cancels.RFC_ID`
- `frequency_id` → `oaseslive.rfc_frequency_phase_header.rfc_id`

### oaseslive.rfc_change_origin

**References (Outgoing):**

- `change_origin_code` → `oaseslive.rfc_change_origin.change_origin_code`

**Referenced By (Incoming):**

- `oaseslive.rfc_change_origin.change_origin_code` → `change_origin_code`
- `oaseslive.rfc_download_origin_codes.CHANGE_ORIGIN_CODE` → `change_origin_code`
- `oaseslive.rfc_header.change_origin_code` → `change_origin_code`
- `oaseslive.rfc_status.change_origin_code` → `change_origin_code`

### oaseslive.rfc_components

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `na_id` → `oaseslive.alternate_parts.PART_NUMBER`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `rfc_id` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `paragraph_id` → `oaseslive.paragraph_cancels.RFC_ID`
- `frequency_id` → `oaseslive.rfc_frequency_phase_header.rfc_id`

### oaseslive.rfc_documents

**References (Outgoing):**

- `DOCUMENT_IMAGE_ID` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`
- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `RFC_DOCUMENT_ID` → `oaseslive.rfc_documents.RFC_DOCUMENT_ID`

**Referenced By (Incoming):**

- `oaseslive.rfc_documents.RFC_DOCUMENT_ID` → `RFC_DOCUMENT_ID`

### oaseslive.rfc_download_effectivity

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `TAXONOMY_ID` → `oaseslive.rfc_download_taxonomy.TAXONOMY_ID`

### oaseslive.rfc_download_origin_codes

**References (Outgoing):**

- `ACCOMPLISHMENT_CODE` → `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID`
- `CHANGE_ORIGIN_CODE` → `oaseslive.rfc_change_origin.change_origin_code`
- `AUTHORITY_CODE` → `oaseslive.rfc_regulating_authority.authority_code`

### oaseslive.rfc_download_taxonomy

**References (Outgoing):**

- `TAXONOMY_ID` → `oaseslive.rfc_download_taxonomy.TAXONOMY_ID`
- `AUTHORITY_CODE` → `oaseslive.rfc_regulating_authority.authority_code`

**Referenced By (Incoming):**

- `oaseslive.rfc_download_effectivity.TAXONOMY_ID` → `TAXONOMY_ID`
- `oaseslive.rfc_download_taxonomy.TAXONOMY_ID` → `TAXONOMY_ID`

### oaseslive.rfc_effectivity_ata

**References (Outgoing):**

- `rfc_id` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`

### oaseslive.rfc_effectivity_fleet

**References (Outgoing):**

- `rfc_id` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`

### oaseslive.rfc_effectivity_part

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `rfc_id` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`

### oaseslive.rfc_evaluation_history

**References (Outgoing):**

- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `EVALUATION_HISTORY_ID` → `oaseslive.rfc_evaluation_history.EVALUATION_HISTORY_ID`

**Referenced By (Incoming):**

- `oaseslive.rfc_evaluation_history.EVALUATION_HISTORY_ID` → `EVALUATION_HISTORY_ID`

### oaseslive.rfc_evaluation_stages

**References (Outgoing):**

- `stage_code` → `oaseslive.amp_component_intervals_stages.component_interval_id`

### oaseslive.rfc_frequency_phase_header

**References (Outgoing):**

- `rfc_id` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `paragraph_id` → `oaseslive.paragraph_cancels.RFC_ID`
- `frequency_id` → `oaseslive.rfc_frequency_phase_header.rfc_id`

**Referenced By (Incoming):**

- `oaseslive.amp_workcard_h3_7487bkp.PHASE_CODE` → `rfc_id`
- `oaseslive.amp_workcard_header_3.phase_code` → `rfc_id`
- `oaseslive.dmg_rpr_inspections.FREQUENCY_ID` → `rfc_id`
- `oaseslive.dmg_rpr_interim_repairs.FREQUENCY_ID` → `rfc_id`
- `oaseslive.dmg_rpr_permanent_repairs.FREQUENCY_ID` → `rfc_id`
- `oaseslive.dmg_rpr_time_limited_repairs.FREQUENCY_ID` → `rfc_id`
- `oaseslive.maint_cost_budget_adsb.FREQUENCY_ID` → `rfc_id`
- `oaseslive.maint_cost_budget_adsb.PHASE_NUMBER` → `rfc_id`
- `oaseslive.rfc_aircraft.frequency_id` → `rfc_id`
- `oaseslive.rfc_components.frequency_id` → `rfc_id`
- `oaseslive.rfc_frequency_phase_header.frequency_id` → `rfc_id`
- `oaseslive.rfc_frequency_phase_limits.frequency_id` → `rfc_id`
- `oaseslive.rfc_frequency_phases.frequency_id` → `rfc_id`

### oaseslive.rfc_frequency_phase_limits

**References (Outgoing):**

- `rfc_id` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `life_code_level_id` → `oaseslive.life_code_levels.life_code_level_id`
- `paragraph_id` → `oaseslive.paragraph_cancels.RFC_ID`
- `frequency_id` → `oaseslive.rfc_frequency_phase_header.rfc_id`

### oaseslive.rfc_frequency_phases

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `rfc_id` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `paragraph_id` → `oaseslive.paragraph_cancels.RFC_ID`
- `frequency_id` → `oaseslive.rfc_frequency_phase_header.rfc_id`

### oaseslive.rfc_header

**References (Outgoing):**

- `accomplishment_code` → `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID`
- `section_id` → `oaseslive.amp_workcard_sections.section_id`
- `rfc_id` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `change_origin_code` → `oaseslive.rfc_change_origin.change_origin_code`
- `authority_code` → `oaseslive.rfc_regulating_authority.authority_code`

### oaseslive.rfc_header_publications

**References (Outgoing):**

- `PUBLICATION_CODE` → `oaseslive.amp_workcard_publications.PUBLICATION_ID`
- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`

### oaseslive.rfc_na_notes

**References (Outgoing):**

- `na_id` → `oaseslive.alternate_parts.PART_NUMBER`
- `na_code` → `oaseslive.alternate_parts.PART_NUMBER`

### oaseslive.rfc_paragraphs

**References (Outgoing):**

- `rfc_id` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `paragraph_id` → `oaseslive.paragraph_cancels.RFC_ID`

### oaseslive.rfc_policies

**References (Outgoing):**

- `policy_id` → `oaseslive.security_policy.POLICY_ID`

### oaseslive.rfc_print_history_log

**References (Outgoing):**

- `LOG_ID` → `oaseslive.amp_data_migration_log.LOG_NUMBER`
- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`

### oaseslive.rfc_publications

**References (Outgoing):**

- `PUBLICATION_CODE` → `oaseslive.amp_workcard_publications.PUBLICATION_ID`

### oaseslive.rfc_regulating_authority

**References (Outgoing):**

- `authority_code` → `oaseslive.rfc_regulating_authority.authority_code`

**Referenced By (Incoming):**

- `oaseslive.consumable_history.authority_code` → `authority_code`
- `oaseslive.rfc_download_origin_codes.AUTHORITY_CODE` → `authority_code`
- `oaseslive.rfc_download_taxonomy.AUTHORITY_CODE` → `authority_code`
- `oaseslive.rfc_header.authority_code` → `authority_code`
- `oaseslive.rfc_regulating_authority.authority_code` → `authority_code`

### oaseslive.rfc_relationships

**References (Outgoing):**

- `rfc_id` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`

### oaseslive.rfc_statement_sections

**References (Outgoing):**

- `SECTION_ID` → `oaseslive.amp_workcard_sections.section_id`
- `SECTION_CODE` → `oaseslive.amp_workcard_sections.section_id`

### oaseslive.rfc_status

**References (Outgoing):**

- `permission_id` → `oaseslive.add_extension_permissions.USER_ID`
- `stage_code` → `oaseslive.amp_component_intervals_stages.component_interval_id`
- `change_origin_code` → `oaseslive.rfc_change_origin.change_origin_code`

### oaseslive.rfc_transaction_log

**References (Outgoing):**

- `LOG_ID` → `oaseslive.amp_data_migration_log.LOG_NUMBER`
- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`

### oaseslive.rfq_by_part_number

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `RFQ_NUMBER` → `oaseslive.requirement_to_rfq_xref.requirement_number`

### oaseslive.rfq_history

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `condition_code` → `oaseslive.condition_codes.condition_code`
- `currency_code` → `oaseslive.currency_codes.currency_code`
- `rfq_number` → `oaseslive.requirement_to_rfq_xref.requirement_number`

### oaseslive.rfq_quote_received

**References (Outgoing):**

- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`
- `RFQ_NUMBER` → `oaseslive.requirement_to_rfq_xref.requirement_number`

### oaseslive.rfq_quote_received_notes

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `rfq_number` → `oaseslive.requirement_to_rfq_xref.requirement_number`

### oaseslive.rfq_requirement_xref

**References (Outgoing):**

- `REQUIREMENT_NUMBER` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`
- `RFQ_NUMBER` → `oaseslive.requirement_to_rfq_xref.requirement_number`

### oaseslive.rfq_supplier_details

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `rfq_number` → `oaseslive.requirement_to_rfq_xref.requirement_number`

### oaseslive.rfq_supplier_notes

**References (Outgoing):**

- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `RFQ_NUMBER` → `oaseslive.requirement_to_rfq_xref.requirement_number`

### oaseslive.rfq_to_order_xref

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `order_number` → `oaseslive.batch_orders.BATCH_NUMBER`
- `rfq_number` → `oaseslive.requirement_to_rfq_xref.requirement_number`

### oaseslive.rotable_batch_locations

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `batch_number` → `oaseslive.batch_file_header.KEY`
- `bin_number` → `oaseslive.bins.bin_number`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `movement_code` → `oaseslive.component_movement_hist_life.part_number`
- `long_serial_number` → `oaseslive.long_serial_number_xref.part_number`

### oaseslive.rotable_float_values

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.rotable_history

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `batch_number` → `oaseslive.batch_file_header.KEY`
- `order_number` → `oaseslive.batch_orders.BATCH_NUMBER`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `movement_code` → `oaseslive.component_movement_hist_life.part_number`
- `delivery_note_number` → `oaseslive.delivery_note_extended_remarks.DELIVERY_NOTE_NUMBER`
- `requirement_number` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`

**Referenced By (Incoming):**

- `oaseslive.shipment_demands.rotable_history_id` → `id`

### oaseslive.rotables_below_re_order

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.rp_base_plan_header

**References (Outgoing):**

- `BASE_PLAN_ID` → `oaseslive.rp_base_plan_header.BASE_PLAN_ID`

**Referenced By (Incoming):**

- `oaseslive.rp_base_plan_header.BASE_PLAN_ID` → `BASE_PLAN_ID`
- `oaseslive.rp_wo_base_estimated_defects.BASE_PLAN_ID` → `BASE_PLAN_ID`
- `oaseslive.rp_wo_base_milestones.BASE_PLAN_ID` → `BASE_PLAN_ID`
- `oaseslive.rp_wo_base_nrc_plan.BASE_PLAN_ID` → `BASE_PLAN_ID`
- `oaseslive.rp_wo_base_workcard_plan.BASE_PLAN_ID` → `BASE_PLAN_ID`

### oaseslive.rp_basic_shift

**References (Outgoing):**

- `basic_shift_id` → `oaseslive.rp_basic_shift.basic_shift_id`

**Referenced By (Incoming):**

- `oaseslive.rp_basic_shift.basic_shift_id` → `basic_shift_id`
- `oaseslive.rp_block_resource.SHIFT_ID` → `basic_shift_id`
- `oaseslive.rp_employee_allocation_header.BASIC_SHIFT_ID` → `basic_shift_id`
- `oaseslive.rp_employee_calendar_addition.shift_id` → `basic_shift_id`
- `oaseslive.rp_wo_base_estimated_defects.BASIC_SHIFT_ID` → `basic_shift_id`
- `oaseslive.rp_wo_base_nrc_plan.BASIC_SHIFT_ID` → `basic_shift_id`
- `oaseslive.rp_wo_base_workcard_plan.BASIC_SHIFT_ID` → `basic_shift_id`
- `oaseslive.rp_wo_estimated_defects.basic_shift_id` → `basic_shift_id`
- `oaseslive.rp_wo_nrc_plan.basic_shift_id` → `basic_shift_id`
- `oaseslive.rp_wo_workcard_plan.basic_shift_id` → `basic_shift_id`

### oaseslive.rp_block_resource

**References (Outgoing):**

- `WAREHOUSE_CODE` → `oaseslive.account_available_warehouses.ACCOUNT_CODE`
- `BLOCK_ID` → `oaseslive.block_countries.block_code`
- `SHIFT_ID` → `oaseslive.rp_basic_shift.basic_shift_id`
- `SCOPE_TYPE_ID` → `oaseslive.scope_type_rating.scope_type_id`

### oaseslive.rp_block_resource_days

**References (Outgoing):**

- `BLOCK_ID` → `oaseslive.block_countries.block_code`
- `DAY_ID` → `oaseslive.public_holidays.HOLIDAY_DATE`
- `DAY_NUMBER` → `oaseslive.public_holidays.HOLIDAY_DATE`

### oaseslive.rp_calendar_addition_type

**References (Outgoing):**

- `type_id` → `oaseslive.aircraft_types.aircraft_type`

### oaseslive.rp_dependencies

**References (Outgoing):**

- `TYPE_ID` → `oaseslive.aircraft_types.aircraft_type`
- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `REVISION_ID` → `oaseslive.amp_revisions.revision_id`
- `MILESTONE_ID` → `oaseslive.rp_milestone_history.HISTORY_ID`

### oaseslive.rp_employee_allocation

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `NRC_NUMBER` → `oaseslive.cq_quote_nrc_access_panels.QUOTE_ID`
- `ALLOCATION_ID` → `oaseslive.order_requirement_allocation.order_number`
- `ALLOCATION_HEADER_ID` → `oaseslive.rp_employee_allocation_header.ALLOCATION_HEADER_ID`

### oaseslive.rp_employee_allocation_header

**References (Outgoing):**

- `EMPLOYEE_NUMBER` → `oaseslive.defect_stage_employees.defect_id`
- `BASIC_SHIFT_ID` → `oaseslive.rp_basic_shift.basic_shift_id`
- `ALLOCATION_HEADER_ID` → `oaseslive.rp_employee_allocation_header.ALLOCATION_HEADER_ID`

**Referenced By (Incoming):**

- `oaseslive.rp_employee_allocation.ALLOCATION_HEADER_ID` → `ALLOCATION_HEADER_ID`
- `oaseslive.rp_employee_allocation_header.ALLOCATION_HEADER_ID` → `ALLOCATION_HEADER_ID`

### oaseslive.rp_employee_calendar_addition

**References (Outgoing):**

- `warehouse_code` → `oaseslive.account_available_warehouses.ACCOUNT_CODE`
- `type_id` → `oaseslive.aircraft_types.aircraft_type`
- `employee_number` → `oaseslive.defect_stage_employees.defect_id`
- `addition_id` → `oaseslive.order_line_additional_info.ORDER_NUMBER`
- `shift_id` → `oaseslive.rp_basic_shift.basic_shift_id`

### oaseslive.rp_employee_calendar_pattern

**References (Outgoing):**

- `warehouse_code` → `oaseslive.account_available_warehouses.ACCOUNT_CODE`
- `employee_number` → `oaseslive.defect_stage_employees.defect_id`
- `shift_pattern_id` → `oaseslive.rp_shift_pattern.shift_pattern_id`

### oaseslive.rp_milestone_history

**References (Outgoing):**

- `HISTORY_ID` → `oaseslive.accomplishment_history.ACCOMPLISHMENT_ID`
- `MILESTONE_ID` → `oaseslive.rp_milestone_history.HISTORY_ID`

**Referenced By (Incoming):**

- `oaseslive.rp_dependencies.MILESTONE_ID` → `HISTORY_ID`
- `oaseslive.rp_milestone_history.MILESTONE_ID` → `HISTORY_ID`
- `oaseslive.rp_milestones.MILESTONE_ID` → `HISTORY_ID`
- `oaseslive.rp_milestones.MILESTONE_CODE` → `HISTORY_ID`
- `oaseslive.rp_wo_base_milestones.MILESTONE_ID` → `HISTORY_ID`
- `oaseslive.rp_wo_milestones.MILESTONE_ID` → `HISTORY_ID`

### oaseslive.rp_milestones

**References (Outgoing):**

- `MILESTONE_ID` → `oaseslive.rp_milestone_history.HISTORY_ID`
- `MILESTONE_CODE` → `oaseslive.rp_milestone_history.HISTORY_ID`

### oaseslive.rp_shift_pattern

**References (Outgoing):**

- `shift_pattern_id` → `oaseslive.rp_shift_pattern.shift_pattern_id`

**Referenced By (Incoming):**

- `oaseslive.rp_employee_calendar_pattern.shift_pattern_id` → `shift_pattern_id`
- `oaseslive.rp_shift_pattern.shift_pattern_id` → `shift_pattern_id`
- `oaseslive.rp_shift_pattern_header.shift_pattern_id` → `shift_pattern_id`

### oaseslive.rp_shift_pattern_header

**References (Outgoing):**

- `shift_pattern_id` → `oaseslive.rp_shift_pattern.shift_pattern_id`

### oaseslive.rp_weekends

**References (Outgoing):**

- `WEEKENDS_ID` → `oaseslive.rp_weekends.WEEKENDS_ID`

**Referenced By (Incoming):**

- `oaseslive.rp_weekends.WEEKENDS_ID` → `WEEKENDS_ID`

### oaseslive.rp_wo_base_estimated_defects

**References (Outgoing):**

- `BASE_PLAN_ID` → `oaseslive.rp_base_plan_header.BASE_PLAN_ID`
- `BASIC_SHIFT_ID` → `oaseslive.rp_basic_shift.basic_shift_id`

### oaseslive.rp_wo_base_milestones

**References (Outgoing):**

- `BASE_PLAN_ID` → `oaseslive.rp_base_plan_header.BASE_PLAN_ID`
- `MILESTONE_ID` → `oaseslive.rp_milestone_history.HISTORY_ID`

### oaseslive.rp_wo_base_nrc_plan

**References (Outgoing):**

- `NRC_NUMBER` → `oaseslive.cq_quote_nrc_access_panels.QUOTE_ID`
- `BASE_PLAN_ID` → `oaseslive.rp_base_plan_header.BASE_PLAN_ID`
- `BASIC_SHIFT_ID` → `oaseslive.rp_basic_shift.basic_shift_id`

### oaseslive.rp_wo_base_workcard_plan

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `BASE_PLAN_ID` → `oaseslive.rp_base_plan_header.BASE_PLAN_ID`
- `BASIC_SHIFT_ID` → `oaseslive.rp_basic_shift.basic_shift_id`

### oaseslive.rp_wo_estimated_defects

**References (Outgoing):**

- `basic_shift_id` → `oaseslive.rp_basic_shift.basic_shift_id`

### oaseslive.rp_wo_milestones

**References (Outgoing):**

- `MILESTONE_ID` → `oaseslive.rp_milestone_history.HISTORY_ID`

### oaseslive.rp_wo_nrc_plan

**References (Outgoing):**

- `nrc_number` → `oaseslive.cq_quote_nrc_access_panels.QUOTE_ID`
- `basic_shift_id` → `oaseslive.rp_basic_shift.basic_shift_id`

### oaseslive.rp_wo_workcard_plan

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `basic_shift_id` → `oaseslive.rp_basic_shift.basic_shift_id`

### oaseslive.sabre_flight_map

**References (Outgoing):**

- `REPORT_ID` → `oaseslive.amp_report_documents.FLEET`

### oaseslive.sabre_trace

**References (Outgoing):**

- `TRACE_ID` → `oaseslive.easa_trace.TRACE_ID`

### oaseslive.sage_order_line_details

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

### oaseslive.sales_history

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `oaseslive.batch_file_header.KEY`
- `order_number` → `oaseslive.batch_orders.BATCH_NUMBER`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `condition_code` → `oaseslive.condition_codes.condition_code`
- `currency_code` → `oaseslive.currency_codes.currency_code`
- `invoice_number` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.sales_invoice_genled_xref

**References (Outgoing):**

- `END_USE_CODE` → `oaseslive.end_use_codes.END_USE_CODE`

### oaseslive.sales_invoices_xref

**References (Outgoing):**

- `SALES_ORDER_NUMBER` → `oaseslive.customer_sales_order_xref.CUSTOMER_SALES_ORDER_NUMBER`
- `INVOICE_NUMBER` → `oaseslive.invoice_categories.INVOICE_CATEGORY`

### oaseslive.sales_notes_for_part

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### oaseslive.sales_order_dispatches

**References (Outgoing):**

- `batch_number` → `oaseslive.batch_file_header.KEY`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `sales_order_number` → `oaseslive.customer_sales_order_xref.CUSTOMER_SALES_ORDER_NUMBER`
- `delivery_note_number` → `oaseslive.delivery_note_extended_remarks.DELIVERY_NOTE_NUMBER`
- `sales_order_dispatch_number` → `oaseslive.sales_order_dispatches.sales_order_number`

**Referenced By (Incoming):**

- `oaseslive.sales_order_dispatches.sales_order_dispatch_number` → `sales_order_number`
- `oaseslive.sales_order_payments.SALES_ORDER_DISPATCH_NUMBER` → `sales_order_number`

### oaseslive.sales_order_history

**References (Outgoing):**

- `SALES_REQUEST_NUMBER` → `oaseslive.sales_request_quote_detail.sales_request_number`

### oaseslive.sales_order_lines

**References (Outgoing):**

- `sales_order_number` → `oaseslive.customer_sales_order_xref.CUSTOMER_SALES_ORDER_NUMBER`
- `requirement_number` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`
- `sales_request_number` → `oaseslive.sales_request_quote_detail.sales_request_number`

### oaseslive.sales_order_notes

**References (Outgoing):**

- `SALES_ORDER_NUMBER` → `oaseslive.customer_sales_order_xref.CUSTOMER_SALES_ORDER_NUMBER`

### oaseslive.sales_order_parameters

**References (Outgoing):**

- `KEY_ID` → `oaseslive.osys_key_to_reportid.OSYSKEY`

### oaseslive.sales_order_payments

**References (Outgoing):**

- `SALES_ORDER_NUMBER` → `oaseslive.customer_sales_order_xref.CUSTOMER_SALES_ORDER_NUMBER`
- `USER_ID` → `oaseslive.dataset_locks_by_user.USER_ID`
- `SALES_ORDER_DISPATCH_NUMBER` → `oaseslive.sales_order_dispatches.sales_order_number`

### oaseslive.sales_orders

**References (Outgoing):**

- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `COMPANY_CODE` → `oaseslive.company_codes.COMPANY_CODE`
- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`
- `SALES_ORDER_NUMBER` → `oaseslive.customer_sales_order_xref.CUSTOMER_SALES_ORDER_NUMBER`

### oaseslive.sales_orders_by_part

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `SALES_ORDER_NUMBER` → `oaseslive.customer_sales_order_xref.CUSTOMER_SALES_ORDER_NUMBER`

### oaseslive.sales_prices

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `condition_code` → `oaseslive.condition_codes.condition_code`
- `currency_code` → `oaseslive.currency_codes.currency_code`
- `price_type_code` → `oaseslive.price_types.price_type_code`

### oaseslive.sales_quotes_out_history

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `CONDITION_CODE` → `oaseslive.condition_codes.condition_code`
- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`
- `SALES_REQUEST_NUMBER` → `oaseslive.sales_request_quote_detail.sales_request_number`

### oaseslive.sales_request_quote_detail

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `sales_order_number` → `oaseslive.customer_sales_order_xref.CUSTOMER_SALES_ORDER_NUMBER`
- `rfq_number` → `oaseslive.requirement_to_rfq_xref.requirement_number`
- `sales_request_number` → `oaseslive.sales_request_quote_detail.sales_request_number`

**Referenced By (Incoming):**

- `oaseslive.sales_order_history.SALES_REQUEST_NUMBER` → `sales_request_number`
- `oaseslive.sales_order_lines.sales_request_number` → `sales_request_number`
- `oaseslive.sales_quotes_out_history.SALES_REQUEST_NUMBER` → `sales_request_number`
- `oaseslive.sales_request_quote_detail.sales_request_number` → `sales_request_number`
- `oaseslive.sales_request_quote_header.SALES_REQUEST_NUMBER` → `sales_request_number`
- `oaseslive.sales_request_quote_notes.SALES_REQUEST_NUMBER` → `sales_request_number`
- `oaseslive.sales_requested_unknown_parts.SALES_REQUEST_NUMBER` → `sales_request_number`
- `oaseslive.sales_requests_by_part.SALES_REQUEST_NUMBER` → `sales_request_number`
- `oaseslive.sales_requests_by_unknown_part.SALES_REQUEST_NUMBER` → `sales_request_number`

### oaseslive.sales_request_quote_header

**References (Outgoing):**

- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `COMPANY_CODE` → `oaseslive.company_codes.COMPANY_CODE`
- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`
- `USER_ID` → `oaseslive.dataset_locks_by_user.USER_ID`
- `SALES_REQUEST_NUMBER` → `oaseslive.sales_request_quote_detail.sales_request_number`

### oaseslive.sales_request_quote_notes

**References (Outgoing):**

- `SALES_REQUEST_NUMBER` → `oaseslive.sales_request_quote_detail.sales_request_number`

### oaseslive.sales_requested_unknown_parts

**References (Outgoing):**

- `SALES_REQUEST_NUMBER` → `oaseslive.sales_request_quote_detail.sales_request_number`

**Referenced By (Incoming):**

- `oaseslive.sales_requests_by_unknown_part.UNKNOWN_PART_NUMBER` → `SALES_REQUEST_NUMBER`

### oaseslive.sales_requests_by_part

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `SALES_REQUEST_NUMBER` → `oaseslive.sales_request_quote_detail.sales_request_number`

### oaseslive.sales_requests_by_unknown_part

**References (Outgoing):**

- `SALES_REQUEST_NUMBER` → `oaseslive.sales_request_quote_detail.sales_request_number`
- `UNKNOWN_PART_NUMBER` → `oaseslive.sales_requested_unknown_parts.SALES_REQUEST_NUMBER`

### oaseslive.sample_fleets

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `fleet_code` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`

### oaseslive.sample_fleets_jn

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `FLEET_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`

### oaseslive.sap_order_header

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `PREORDER_ID` → `oaseslive.preorder_line_requirement_xref.PREORDER_ID`

### oaseslive.sap_order_line

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `PREORDER_ID` → `oaseslive.preorder_line_requirement_xref.PREORDER_ID`

### oaseslive.schedule_forecast_xref

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `WORKCARD_ID` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `VISIT_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `PACKAGE_CODE` → `oaseslive.amp_package_notes.fleet`
- `WORKCARD_INTERVAL_ID` → `oaseslive.amp_workcard_intervals_limits.workcard_interval_id`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`

### oaseslive.schedule_source

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`

### oaseslive.scope_type_rating

**References (Outgoing):**

- `scope_type_id` → `oaseslive.scope_type_rating.scope_type_id`

**Referenced By (Incoming):**

- `oaseslive.employees_licences.scope_type_id` → `scope_type_id`
- `oaseslive.rp_block_resource.SCOPE_TYPE_ID` → `scope_type_id`
- `oaseslive.scope_type_rating.scope_type_id` → `scope_type_id`

### oaseslive.sectors

**References (Outgoing):**

- `sector_id` → `oaseslive.flown_sectors.aircraft_code`

### oaseslive.security_audit_log_header

**References (Outgoing):**

- `PERMISSION_ID` → `oaseslive.add_extension_permissions.USER_ID`
- `AUDIT_LOG_ID` → `oaseslive.security_audit_log_header.AUDIT_LOG_ID`

**Referenced By (Incoming):**

- `oaseslive.security_audit_log_header.AUDIT_LOG_ID` → `AUDIT_LOG_ID`
- `oaseslive.security_audit_log_meta_data.AUDIT_LOG_ID` → `AUDIT_LOG_ID`

### oaseslive.security_audit_log_meta_data

**References (Outgoing):**

- `SEQUENCE_NUMBER` → `oaseslive.nrc_high_sequence_control.KEY_ID`
- `AUDIT_LOG_ID` → `oaseslive.security_audit_log_header.AUDIT_LOG_ID`

### oaseslive.security_group_perm_attribute

**References (Outgoing):**

- `PERMISSION_ID` → `oaseslive.add_extension_permissions.USER_ID`
- `GROUP_ID` → `oaseslive.forecast_filter_groups.GROUP_ID`
- `ATTRIBUTE_ID` → `oaseslive.security_group_perm_attribute.GROUP_ID`

**Referenced By (Incoming):**

- `oaseslive.security_group_perm_attribute.ATTRIBUTE_ID` → `GROUP_ID`
- `oaseslive.security_permission_def_attrib.ATTRIBUTE_ID` → `GROUP_ID`
- `oaseslive.security_policy_perm_attribute.ATTRIBUTE_ID` → `GROUP_ID`
- `oaseslive.security_user_perm_attribute.ATTRIBUTE_ID` → `GROUP_ID`

### oaseslive.security_group_permissions

**References (Outgoing):**

- `PERMISSION_ID` → `oaseslive.add_extension_permissions.USER_ID`
- `GROUP_ID` → `oaseslive.forecast_filter_groups.GROUP_ID`

### oaseslive.security_group_policies

**References (Outgoing):**

- `GROUP_ID` → `oaseslive.forecast_filter_groups.GROUP_ID`
- `POLICY_ID` → `oaseslive.security_policy.POLICY_ID`

### oaseslive.security_groups

**References (Outgoing):**

- `GROUP_ID` → `oaseslive.forecast_filter_groups.GROUP_ID`

### oaseslive.security_permission_def_attrib

**References (Outgoing):**

- `PERMISSION_ID` → `oaseslive.add_extension_permissions.USER_ID`
- `ATTRIBUTE_ID` → `oaseslive.security_group_perm_attribute.GROUP_ID`

### oaseslive.security_policy

**References (Outgoing):**

- `POLICY_ID` → `oaseslive.security_policy.POLICY_ID`

**Referenced By (Incoming):**

- `oaseslive.cq_quote_status.policy_id` → `POLICY_ID`
- `oaseslive.rfc_policies.policy_id` → `POLICY_ID`
- `oaseslive.security_group_policies.POLICY_ID` → `POLICY_ID`
- `oaseslive.security_policy.POLICY_ID` → `POLICY_ID`
- `oaseslive.security_policy_perm_attribute.POLICY_ID` → `POLICY_ID`
- `oaseslive.security_policy_permissions.POLICY_ID` → `POLICY_ID`
- `oaseslive.security_user_policies.POLICY_ID` → `POLICY_ID`

### oaseslive.security_policy_perm_attribute

**References (Outgoing):**

- `PERMISSION_ID` → `oaseslive.add_extension_permissions.USER_ID`
- `ATTRIBUTE_ID` → `oaseslive.security_group_perm_attribute.GROUP_ID`
- `POLICY_ID` → `oaseslive.security_policy.POLICY_ID`

### oaseslive.security_policy_permissions

**References (Outgoing):**

- `PERMISSION_ID` → `oaseslive.add_extension_permissions.USER_ID`
- `POLICY_ID` → `oaseslive.security_policy.POLICY_ID`

### oaseslive.security_user_effectivity

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `sub_fleet_id` → `oaseslive.sub_fleets.sub_fleet_id`

### oaseslive.security_user_groups

**References (Outgoing):**

- `GROUP_ID` → `oaseslive.forecast_filter_groups.GROUP_ID`

### oaseslive.security_user_notifications

**References (Outgoing):**

- `NOTIFICATION_ID` → `oaseslive.email_notification.ID`
- `USER_NOTIFICATION_ID` → `oaseslive.security_user_notifications.USER_NOTIFICATION_ID`

**Referenced By (Incoming):**

- `oaseslive.security_user_notifications.USER_NOTIFICATION_ID` → `USER_NOTIFICATION_ID`

### oaseslive.security_user_perm_attribute

**References (Outgoing):**

- `PERMISSION_ID` → `oaseslive.add_extension_permissions.USER_ID`
- `ATTRIBUTE_ID` → `oaseslive.security_group_perm_attribute.GROUP_ID`

### oaseslive.security_user_permissions

**References (Outgoing):**

- `PERMISSION_ID` → `oaseslive.add_extension_permissions.USER_ID`

### oaseslive.security_user_permissions_bkp

**References (Outgoing):**

- `PERMISSION_ID` → `oaseslive.add_extension_permissions.USER_ID`

### oaseslive.security_user_policies

**References (Outgoing):**

- `POLICY_ID` → `oaseslive.security_policy.POLICY_ID`

### oaseslive.serial_numbers_by_part

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.sfdc_activity

**References (Outgoing):**

- `ACTIVITY_ID` → `oaseslive.b737ng_activity_import_table.SCHEDULE_REFERENCE`
- `DEFECT_STAGE_ID` → `oaseslive.defect_stage_employees.defect_id`
- `LICENCE_ID` → `oaseslive.email_licence.LICENSE_ID`
- `BOOKING_ID` → `oaseslive.oeim_booking_base_data.BOOKING_ROUNDING_UP_MINS`

### oaseslive.sfdc_bookings

**References (Outgoing):**

- `TASK_NUMBER` → `oaseslive.amp_datmig_comp_task_lookup.FLEET`
- `DEFECT_CODE` → `oaseslive.defect_extensions.DEFECT_ID`
- `EMPLOYEE_NUMBER` → `oaseslive.defect_stage_employees.defect_id`
- `BOOKING_ID` → `oaseslive.oeim_booking_base_data.BOOKING_ROUNDING_UP_MINS`

### oaseslive.sfdc_component_changes

**References (Outgoing):**

- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `COMPONENT_CHANGE_ID` → `oaseslive.sfdc_component_changes.COMPONENT_CHANGE_ID`

**Referenced By (Incoming):**

- `oaseslive.sfdc_component_changes.COMPONENT_CHANGE_ID` → `COMPONENT_CHANGE_ID`

### oaseslive.sfdc_deleted_bookings

**References (Outgoing):**

- `TASK_NUMBER` → `oaseslive.amp_datmig_comp_task_lookup.FLEET`
- `DEFECT_CODE` → `oaseslive.defect_extensions.DEFECT_ID`
- `EMPLOYEE_NUMBER` → `oaseslive.defect_stage_employees.defect_id`
- `SEQUENCE_NUMBER` → `oaseslive.nrc_high_sequence_control.KEY_ID`

### oaseslive.sfdc_open_bookings

**References (Outgoing):**

- `TASK_NUMBER` → `oaseslive.amp_datmig_comp_task_lookup.FLEET`
- `DEFECT_CODE` → `oaseslive.defect_extensions.DEFECT_ID`
- `EMPLOYEE_NUMBER` → `oaseslive.defect_stage_employees.defect_id`

### oaseslive.shelf_li_dt_bkp_2020

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `COMPONENT_LIFE_LIMIT_ID` → `oaseslive.component_life_limits.component_life_limit_id`
- `SHELF_LIFE_DATE_ID` → `oaseslive.shelf_life_dates.shelf_life_date_id`

### oaseslive.shelf_life_dates

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `oaseslive.batch_file_header.KEY`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `component_life_limit_id` → `oaseslive.component_life_limits.component_life_limit_id`
- `shelf_life_date_id` → `oaseslive.shelf_life_dates.shelf_life_date_id`

**Referenced By (Incoming):**

- `oaseslive.shelf_li_dt_bkp_2020.SHELF_LIFE_DATE_ID` → `shelf_life_date_id`
- `oaseslive.shelf_life_dates.shelf_life_date_id` → `shelf_life_date_id`
- `oaseslive.shelf_life_dates_oases6834.SHELF_LIFE_DATE_ID` → `shelf_life_date_id`

### oaseslive.shelf_life_dates_oases6834

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `COMPONENT_LIFE_LIMIT_ID` → `oaseslive.component_life_limits.component_life_limit_id`
- `SHELF_LIFE_DATE_ID` → `oaseslive.shelf_life_dates.shelf_life_date_id`

### oaseslive.shelf_life_expiry_req_codes

**References (Outgoing):**

- `REQUIREMENT_CODE` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`

### oaseslive.shipment

**References (Outgoing):**

- `COMPANY_CODE` → `oaseslive.company_codes.COMPANY_CODE`
- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`
- `SHIPMENT_ID` → `oaseslive.shipment.SHIPMENT_ID`

**Referenced By (Incoming):**

- `oaseslive.airway_bill_references.SHIPMENT_ID` → `SHIPMENT_ID`
- `oaseslive.package.SHIPMENT_ID` → `SHIPMENT_ID`
- `oaseslive.shipment.SHIPMENT_ID` → `SHIPMENT_ID`
- `oaseslive.shipment_documents.SHIPMENT_ID` → `SHIPMENT_ID`
- `oaseslive.shipment_item.SHIPMENT_ID` → `SHIPMENT_ID`
- `oaseslive.shipment_status.SHIPMENT_ID` → `SHIPMENT_ID`

### oaseslive.shipment_demands

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `oaseslive.batch_file_header.KEY`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `consumable_history_id` → `oaseslive.consumable_history.id`
- `reason_id` → `oaseslive.demand_reason_to_movement_code.ID`
- `non_stock_part_number` → `oaseslive.non_stock_parts.part_number`
- `rotable_history_id` → `oaseslive.rotable_history.id`

### oaseslive.shipment_documents

**References (Outgoing):**

- `DOCUMENT_ID` → `oaseslive.aircraft_documents.AIRCRAFT_DOCUMENT_ID`
- `DOCUMENT_IMAGE_ID` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`
- `SHIPMENT_ID` → `oaseslive.shipment.SHIPMENT_ID`

### oaseslive.shipment_item

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `SHIPMENT_ID` → `oaseslive.shipment.SHIPMENT_ID`
- `SHIPMENT_ITEM_ID` → `oaseslive.shipment_item.SHIPMENT_ITEM_ID`

**Referenced By (Incoming):**

- `oaseslive.freight_costs.SHIPMENT_ITEM_ID` → `SHIPMENT_ITEM_ID`
- `oaseslive.shipment_item.SHIPMENT_ITEM_ID` → `SHIPMENT_ITEM_ID`
- `oaseslive.shipment_item_customs.SHIPMENT_ITEM_ID` → `SHIPMENT_ITEM_ID`

### oaseslive.shipment_item_customs

**References (Outgoing):**

- `CUSTOMS_ENTRY_NUMBER` → `oaseslive.batches_by_customs_entry.CUSTOMS_ENTRY_NUMBER`
- `CUSTOMS_STATUS_CODE` → `oaseslive.customs_status_codes.customs_status`
- `SHIPMENT_ITEM_ID` → `oaseslive.shipment_item.SHIPMENT_ITEM_ID`

### oaseslive.shipment_item_demands

**References (Outgoing):**

- `ITEM_ID` → `oaseslive.delivery_note_item_header_1.delivery_note_number`
- `DEMAND_ID` → `oaseslive.demand_reason_to_movement_code.ID`

### oaseslive.shipment_order_demands

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `order_number` → `oaseslive.batch_orders.BATCH_NUMBER`
- `demand_id` → `oaseslive.demand_reason_to_movement_code.ID`

### oaseslive.shipment_requirement_demands

**References (Outgoing):**

- `pick_number` → `oaseslive.condition_pick_table.PART_NUMBER`
- `demand_id` → `oaseslive.demand_reason_to_movement_code.ID`
- `requirement_number` → `oaseslive.nrc_requirements_actions.aircraft_short_reg`

### oaseslive.shipment_status

**References (Outgoing):**

- `SHIPMENT_ID` → `oaseslive.shipment.SHIPMENT_ID`
- `SHIPMENT_STATUS_ID` → `oaseslive.shipment_status.SHIPMENT_STATUS_ID`
- `SHIPMENT_STATUS_TYPE_ID` → `oaseslive.shipment_status_type.STATUS_ID`

**Referenced By (Incoming):**

- `oaseslive.shipment_status.SHIPMENT_STATUS_ID` → `SHIPMENT_STATUS_ID`

### oaseslive.shipment_status_type

**References (Outgoing):**

- `STATUS_ID` → `oaseslive.amp_revision_status.REVISION_STATUS_ID`

**Referenced By (Incoming):**

- `oaseslive.shipment_status.SHIPMENT_STATUS_TYPE_ID` → `STATUS_ID`

### oaseslive.shipment_stocktransfer_demands

**References (Outgoing):**

- `demand_id` → `oaseslive.demand_reason_to_movement_code.ID`

### oaseslive.shipment_works_orders_demands

**References (Outgoing):**

- `demand_id` → `oaseslive.demand_reason_to_movement_code.ID`

### oaseslive.short_long_serials

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `LONG_SERIAL_NUMBER` → `oaseslive.long_serial_number_xref.part_number`

### oaseslive.skill_codes

**References (Outgoing):**

- `SKILL_CODE` → `oaseslive.skill_codes.SKILL_CODE`

**Referenced By (Incoming):**

- `oaseslive.skill_codes.SKILL_CODE` → `SKILL_CODE`

### oaseslive.sold_hours_history

**References (Outgoing):**

- `DEFECT_NUMBER` → `oaseslive.defect_extensions.DEFECT_ID`

### oaseslive.stock_audit_batches

**References (Outgoing):**

- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `BIN_NUMBER` → `oaseslive.bins.bin_number`
- `STOCK_AUDIT_ID` → `oaseslive.stock_audit_batches.STOCK_AUDIT_ID`

**Referenced By (Incoming):**

- `oaseslive.stock_audit_batches.STOCK_AUDIT_ID` → `STOCK_AUDIT_ID`
- `oaseslive.stock_audit_bins.STOCK_AUDIT_ID` → `STOCK_AUDIT_ID`
- `oaseslive.stock_audits.STOCK_AUDIT_ID` → `STOCK_AUDIT_ID`

### oaseslive.stock_audit_bins

**References (Outgoing):**

- `BIN_NUMBER` → `oaseslive.bins.bin_number`
- `STOCK_AUDIT_ID` → `oaseslive.stock_audit_batches.STOCK_AUDIT_ID`

### oaseslive.stock_audits

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `STOCK_AUDIT_ID` → `oaseslive.stock_audit_batches.STOCK_AUDIT_ID`

### oaseslive.stock_by_bin

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `BIN_NUMBER` → `oaseslive.bins.bin_number`

### oaseslive.stock_documents

**References (Outgoing):**

- `BATCH_NUMBER` → `oaseslive.batch_file_header.KEY`
- `DOCUMENT_IMAGE_ID` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`
- `STOCK_DOCUMENT_ID` → `oaseslive.stock_documents.STOCK_DOCUMENT_ID`

**Referenced By (Incoming):**

- `oaseslive.stock_documents.STOCK_DOCUMENT_ID` → `STOCK_DOCUMENT_ID`

### oaseslive.stock_group_additional_data

**References (Outgoing):**

- `end_use_code` → `oaseslive.end_use_codes.END_USE_CODE`

### oaseslive.stock_groups

**References (Outgoing):**

- `vat_code` → `oaseslive.amp_workcard_activations.workcard_activation_id`

### oaseslive.stock_groups_bkp_oases382

**References (Outgoing):**

- `VAT_CODE` → `oaseslive.amp_workcard_activations.workcard_activation_id`

### oaseslive.stock_works_order_markups

**References (Outgoing):**

- `WORKS_ORDER_NUMBER` → `oaseslive.credit_works_order_cards.credit_note_no`

### oaseslive.strip_documents

**References (Outgoing):**

- `DOCUMENT_IMAGE_ID` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`
- `STRIP_DOCUMENT_ID` → `oaseslive.strip_documents.STRIP_DOCUMENT_ID`
- `STRIP_REPORT_NUMBER` → `oaseslive.strip_report_findings_text.STRIP_REPORT_NUMBER`

**Referenced By (Incoming):**

- `oaseslive.strip_documents.STRIP_DOCUMENT_ID` → `STRIP_DOCUMENT_ID`

### oaseslive.strip_report_findings_text

**References (Outgoing):**

- `STRIP_REPORT_NUMBER` → `oaseslive.strip_report_findings_text.STRIP_REPORT_NUMBER`

**Referenced By (Incoming):**

- `oaseslive.order_lines.strip_report_number` → `STRIP_REPORT_NUMBER`
- `oaseslive.requirement_recharge_details.STRIP_REPORT_NUMBER` → `STRIP_REPORT_NUMBER`
- `oaseslive.strip_documents.STRIP_REPORT_NUMBER` → `STRIP_REPORT_NUMBER`
- `oaseslive.strip_report_findings_text.STRIP_REPORT_NUMBER` → `STRIP_REPORT_NUMBER`
- `oaseslive.strip_report_header_1.STRIP_REPORT_NUMBER` → `STRIP_REPORT_NUMBER`
- `oaseslive.strip_report_header_2.STRIP_REPORT_NUMBER` → `STRIP_REPORT_NUMBER`
- `oaseslive.strip_report_modification_text.STRIP_REPORT_NUMBER` → `STRIP_REPORT_NUMBER`

### oaseslive.strip_report_header_1

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`
- `WORKS_ORDER_NUMBER` → `oaseslive.credit_works_order_cards.credit_note_no`
- `CURRENCY_CODE` → `oaseslive.currency_codes.currency_code`
- `STRIP_REPORT_NUMBER` → `oaseslive.strip_report_findings_text.STRIP_REPORT_NUMBER`

### oaseslive.strip_report_header_2

**References (Outgoing):**

- `STRIP_REPORT_NUMBER` → `oaseslive.strip_report_findings_text.STRIP_REPORT_NUMBER`

### oaseslive.strip_report_modification_text

**References (Outgoing):**

- `STRIP_REPORT_NUMBER` → `oaseslive.strip_report_findings_text.STRIP_REPORT_NUMBER`

### oaseslive.structural_damage

**References (Outgoing):**

- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `defect_number` → `oaseslive.defect_extensions.DEFECT_ID`

### oaseslive.sub_fleet_header

**References (Outgoing):**

- `fleet_code` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `sub_fleet_id` → `oaseslive.sub_fleets.sub_fleet_id`

### oaseslive.sub_fleets

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `sub_fleet_id` → `oaseslive.sub_fleets.sub_fleet_id`

**Referenced By (Incoming):**

- `oaseslive.amp_access_panel_effectivity.SUB_FLEET_ID` → `sub_fleet_id`
- `oaseslive.amp_accesspanel_effectivity_jn.SUB_FLEET_ID` → `sub_fleet_id`
- `oaseslive.amp_material_effectivity.SUB_FLEET_ID` → `sub_fleet_id`
- `oaseslive.amp_material_effectivity_jn.SUB_FLEET_ID` → `sub_fleet_id`
- `oaseslive.amp_workcard_ac_effectivity.SUB_FLEET_ID` → `sub_fleet_id`
- `oaseslive.amp_workcard_ac_effectivity_jn.SUB_FLEET_ID` → `sub_fleet_id`
- `oaseslive.dmg_rpr_doc_effectivity.SUB_FLEET_ID` → `sub_fleet_id`
- `oaseslive.dmg_rpr_document_order.SUB_FLEET_ID` → `sub_fleet_id`
- `oaseslive.security_user_effectivity.sub_fleet_id` → `sub_fleet_id`
- `oaseslive.sub_fleet_header.sub_fleet_id` → `sub_fleet_id`
- `oaseslive.sub_fleets.sub_fleet_id` → `sub_fleet_id`
- `oaseslive.sub_fleets_jn.SUB_FLEET_ID` → `sub_fleet_id`
- `oaseslive.units_of_measure.sub_fleet_id` → `sub_fleet_id`

### oaseslive.sub_fleets_jn

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `SUB_FLEET_ID` → `oaseslive.sub_fleets.sub_fleet_id`

### oaseslive.supplier_loan_contract_rates

**References (Outgoing):**

- `account_code` → `oaseslive.access_dim_accounts_info.INFO_ID`

### oaseslive.system_header_icarus

**References (Outgoing):**

- `KEY_ID` → `oaseslive.osys_key_to_reportid.OSYSKEY`

### oaseslive.talend_jobs

**References (Outgoing):**

- `TALEND_JOB_ID` → `oaseslive.talend_jobs.TALEND_JOB_ID`

**Referenced By (Incoming):**

- `oaseslive.talend_jobs.TALEND_JOB_ID` → `TALEND_JOB_ID`

### oaseslive.task_activity_link

**References (Outgoing):**

- `PART_NUMBER` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `VISIT_CODE` → `oaseslive.amp_datmig_fleet_visit_pack.FLEET`
- `PACKAGE_CODE` → `oaseslive.amp_package_notes.fleet`
- `SERIAL_NUMBER` → `oaseslive.completion_part_serial.PART_NUMBER`

### oaseslive.taskcard_wo_order_line

**References (Outgoing):**

- `ORDER_NUMBER` → `oaseslive.batch_orders.BATCH_NUMBER`

### oaseslive.tech_log_1

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.tech_log_2

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `alert_number` → `oaseslive.alert_colors.ALERT_TYPE_ID`
- `workcard_number` → `oaseslive.amp_access_panels_by_workcard.fleet`

### oaseslive.tech_log_3

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `report_id` → `oaseslive.amp_report_documents.FLEET`
- `revision_id` → `oaseslive.amp_revisions.revision_id`
- `corrosion_code` → `oaseslive.corrosion_categories.corrosion_code`
- `defect_id` → `oaseslive.defect_extensions.DEFECT_ID`
- `mel_revision_number` → `oaseslive.mel_revision_history.HISTORY_ID`

### oaseslive.tech_log_defect_text

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.tech_log_documents

**References (Outgoing):**

- `REPORT_ID` → `oaseslive.amp_report_documents.FLEET`
- `DOCUMENT_IMAGE_ID` → `oaseslive.document_image_source.DOCUMENT_IMAGE_SOURCE_ID`

### oaseslive.tech_log_nrc_xref

**References (Outgoing):**

- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`

### oaseslive.tech_log_rectification_text

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `SEQUENCE_NUMBER` → `oaseslive.nrc_high_sequence_control.KEY_ID`

### oaseslive.tech_log_workcard_link

**References (Outgoing):**

- `AIRCRAFT_CODE` → `oaseslive.aircraft_assembles.aircraft_code`
- `WORKCARD_NUMBER` → `oaseslive.amp_access_panels_by_workcard.fleet`

### oaseslive.temp_rfc_paragraphs

**References (Outgoing):**

- `RFC_ID` → `oaseslive.fleet_forecast_plans_rfc.PLAN_ID`
- `PARAGRAPH_ID` → `oaseslive.paragraph_cancels.RFC_ID`

### oaseslive.test_table

**References (Outgoing):**

- `KEY_ID` → `oaseslive.osys_key_to_reportid.OSYSKEY`

### oaseslive.third_party_account_id

**References (Outgoing):**

- `ACCOUNT_ID` → `oaseslive.access_dim_accounts_info.INFO_ID`
- `ACCOUNT_CODE` → `oaseslive.access_dim_accounts_info.INFO_ID`

### oaseslive.tiered_markup_range

**References (Outgoing):**

- `MARKUP_CODE` → `oaseslive.freight_cost_markups.FREIGHT_COST_MARKUP_ID`

### oaseslive.time_categories

**References (Outgoing):**

- `contract_id` → `oaseslive.customer_contract_rates.contract_id`
- `time_category_id` → `oaseslive.maint_cost_time_category_set.CATEGORY_SET_ID`

### oaseslive.tool_check_out_in

**References (Outgoing):**

- `task_number` → `oaseslive.amp_datmig_comp_task_lookup.FLEET`
- `batch_number` → `oaseslive.batch_file_header.KEY`
- `employee_number` → `oaseslive.defect_stage_employees.defect_id`

### oaseslive.units_of_measure

**References (Outgoing):**

- `part_number` → `oaseslive.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `oaseslive.aircraft_assembles.aircraft_code`
- `workcard_id` → `oaseslive.amp_access_panels_by_workcard.fleet`
- `serial_number` → `oaseslive.completion_part_serial.PART_NUMBER`
- `component_life_limit_id` → `oaseslive.component_life_limits.component_life_limit_id`
- `sub_fleet_id` → `oaseslive.sub_fleets.sub_fleet_id`

---

## Relationship Matrix

Visual representation of table relationships:

```
                                 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29

 0: PART_NUMBER_CHAPTERS_DJ-82
 1: aircraft_assembles
 2: amp_access_panels_by_workcard
 3: completion_part_serial
 4: amp_revisions
 5: access_dim_accounts_info
 6: batch_orders
 7: batch_file_header
 8: invoice_categories
 9: fleet_forecast_plans_rfc
10: currency_codes
11: accomplishment_history
12: amp_package_notes
13: amp_datmig_fleet_visit_pack
14: nrc_requirements_actions
15: amp_report_documents
16: life_code_levels
17: defect_extensions
18: maint_cost_budget_adsb
19: defect_stage_employees
20: document_image_source
21: maint_cost_time_category_set
22: dmg_rpr_damage
23: cost_codes
24: cq_quote_nrc_access_panels
25: paragraph_cancels
26: dataset_locks_by_user
27: rfc_frequency_phase_header
28: amp_workcard_activations
29: delivery_note_item_header_1

Matrix Legend: → = references, ← = referenced by, ↔ = bidirectional

 0 PART_NUMBER_CHAPTERS_DJ-82    ●  ·  · ←  ·  ·  ·  ·  ·  ·  · ←  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ←  ·  ·  ·  ·  ·  · ←
 1 aircraft_assembles             · ●  ·  ·  ·  ·  ·  ·  ·  ·  · ←  ·  ·  ·  ·  ·  · ←  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
 2 amp_access_panels_by_workcard  ·  · ●  · →  ·  ·  ·  ·  ·  ·  ·  ·  · ←  ·  ·  · ←  ·  ·  ·  ·  ·  ·  ·  ·  · ←  ·
 3 completion_part_serial        →  ·  · ●  ·  ·  ·  ·  ·  ·  · ←  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ←  ·  ·  ·  ·  ·  ·  ·
 4 amp_revisions                  ·  · ←  · ●  ·  ·  ·  ·  ·  · ← ←  ·  · ←  ·  · ←  ·  ·  ·  ·  ·  ·  · →  · ←  ·
 5 access_dim_accounts_info       ·  ·  ·  ·  · ●  ·  · →  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · →  ·
 6 batch_orders                   ·  ·  ·  ·  ·  · ● →  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
 7 batch_file_header              ·  ·  ·  ·  ·  · ← ●  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ←
 8 invoice_categories             ·  ·  ·  ·  · ←  ·  · ●  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
 9 fleet_forecast_plans_rfc       ·  ·  ·  ·  ·  ·  ·  ·  · ●  · ←  ·  ·  ·  ·  ·  · ←  ·  ·  ·  ·  ·  · ←  · ←  ·  ·
10 currency_codes                 ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
11 accomplishment_history        → →  · → →  ·  ·  ·  · →  · ● → →  · →  ·  ·  ·  · →  · →  ·  · →  ·  ·  ·  ·
12 amp_package_notes              ·  ·  ·  · →  ·  ·  ·  ·  ·  · ← ●  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
13 amp_datmig_fleet_visit_pack    ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ←  · ●  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
14 nrc_requirements_actions       ·  · →  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·  · →  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ←
15 amp_report_documents           ·  ·  ·  · →  ·  ·  ·  ·  ·  · ←  ·  ·  · ●  ·  ·  ·  · →  ·  ·  ·  ·  ·  ·  ·  ·  ·
16 life_code_levels               ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
17 defect_extensions              ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ←  ·  · ●  · ←  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
18 maint_cost_budget_adsb         · → →  · →  ·  ·  ·  · →  ·  ·  ·  ·  ·  ·  ·  · ●  ·  ·  ·  ·  ·  ·  ·  · →  · →
19 defect_stage_employees         ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · →  · ●  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
20 document_image_source          ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ←  ·  ·  · ←  ·  ·  ·  · ●  ·  ·  ·  ·  ·  ·  ·  ·  ·
21 maint_cost_time_category_set   ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·  ·  ·  ·  ·  ·  ·  ·
22 dmg_rpr_damage                →  ·  · →  ·  ·  ·  ·  ·  ·  · ←  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·  ·  ·  ·  ·  ·  ·
23 cost_codes                     ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·  ·  ·  ·  ·  ·
24 cq_quote_nrc_access_panels     ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·  ·  ·  ·  ·
25 paragraph_cancels              ·  ·  ·  ·  ·  ·  ·  ·  · →  · ←  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●  · ←  ·  ·
26 dataset_locks_by_user          ·  ·  ·  · ←  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·  ·  ·
27 rfc_frequency_phase_header     ·  ·  ·  ·  ·  ·  ·  ·  · →  ·  ·  ·  ·  ·  ·  ·  · ←  ·  ·  ·  ·  ·  · →  · ●  ·  ·
28 amp_workcard_activations       ·  · →  · → ←  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·
29 delivery_note_item_header_1   →  ·  ·  ·  ·  ·  · →  ·  ·  ·  ·  ·  · →  ·  ·  · ←  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●
```

---


---

## Target Schema Relationships


## Table of Contents

1. [Summary Statistics](#summary-statistics)
2. [Table Dependency Hierarchy](#table-dependency-hierarchy)
3. [Highly Connected Tables](#highly-connected-tables)
4. [Detailed Relationships](#detailed-relationships)
5. [Relationship Matrix](#relationship-matrix)

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total Tables | 966 |
| Total Relationships | 1966 |
| Tables with Relationships | 827 |
| Isolated Tables | 139 |

---

## Table Dependency Hierarchy

Tables organized by dependency levels (Level 0 = no dependencies):

### Level 0

- **lumina.aaafcb** (0 relationships)
- **lumina.accfcb** (0 relationships)
- **lumina.account_properties** (0 relationships)
- **lumina.accounting_periods** (0 relationships)
- **lumina.accounts_references** (1 relationships)
- **lumina.aircraft_header_mavis** (0 relationships)
- **lumina.aircraft_list_temp** (0 relationships)
- **lumina.aircraft_notes** (0 relationships)
- **lumina.aircraft_types** (3 relationships)
- **lumina.airport_codes** (1 relationships)
- **lumina.airvault_lookup** (0 relationships)
- **lumina.alert_colors** (11 relationships)
- **lumina.amp_datmig_100int** (0 relationships)
- **lumina.amp_datmig_a320_100int** (0 relationships)
- **lumina.amp_datmig_a320_samint** (0 relationships)
- **lumina.amp_datmig_fleet_visit_pack** (33 relationships)
- **lumina.amp_datmig_panel_eff** (0 relationships)
- **lumina.amp_datmig_panel_notes** (0 relationships)
- **lumina.amp_datmig_panels** (0 relationships)
- **lumina.amp_datmig_panels_by_card** (0 relationships)
- **lumina.amp_datmig_samint** (0 relationships)
- **lumina.amp_datmig_task_eff** (0 relationships)
- **lumina.amp_datmig_task_eff_a320** (0 relationships)
- **lumina.amp_datmig_task_eff_b737** (0 relationships)
- **lumina.amp_datmig_withdrawn_tasks** (0 relationships)
- **lumina.b737ng_activity_import_table** (1 relationships)
- **lumina.batch_file_header** (51 relationships)
- **lumina.batfcb** (0 relationships)
- **lumina.bbbfcb** (0 relationships)
- **lumina.camo_part_issue_alert_emails** (0 relationships)
- **lumina.cbcfcb** (0 relationships)
- **lumina.cfd_categories** (1 relationships)
- **lumina.cfd_categorires_bkpoases405** (1 relationships)
- **lumina.cg_ref_codes** (0 relationships)
- **lumina.chapter_alert_rates** (0 relationships)
- **lumina.chapters** (0 relationships)
- **lumina.chcfcb** (0 relationships)
- **lumina.credit_notes_header** (0 relationships)
- **lumina.currency_conversion** (0 relationships)
- **lumina.dckfcb** (0 relationships)
- **lumina.document_control_xref** (0 relationships)
- **lumina.document_dir_list** (0 relationships)
- **lumina.drn_maint_mod_applicability** (0 relationships)
- **lumina.drn_notes** (0 relationships)
- **lumina.email_licence** (5 relationships)
- **lumina.engineering_support_status** (1 relationships)
- **lumina.esignoff_roles** (0 relationships)
- **lumina.fleet_ata_references** (0 relationships)
- **lumina.fleet_build** (0 relationships)
- **lumina.fleet_build_chapters** (0 relationships)
- **lumina.fleet_chapter** (0 relationships)
- **lumina.fleet_header_1** (0 relationships)
- **lumina.fleet_header_mavis_1** (0 relationships)
- **lumina.fleet_header_mavis_2** (0 relationships)
- **lumina.fleet_notes** (0 relationships)
- **lumina.flight_types** (0 relationships)
- **lumina.forward_schedule_summary_hdr** (0 relationships)
- **lumina.forward_schedule_summary_refs** (0 relationships)
- **lumina.freight_default_costs** (0 relationships)
- **lumina.genlog** (0 relationships)
- **lumina.import_messages** (0 relationships)
- **lumina.invoice_categories** (37 relationships)
- **lumina.ivdfcb** (0 relationships)
- **lumina.ivhfcb** (0 relationships)
- **lumina.java_object_registry** (0 relationships)
- **lumina.job_references** (1 relationships)
- **lumina.lasfcb** (0 relationships)
- **lumina.lmc_base_data_defs** (1 relationships)
- **lumina.lngfcb** (0 relationships)
- **lumina.load_attachment_files** (0 relationships)
- **lumina.load_manufacturers_files** (0 relationships)
- **lumina.logfcb** (0 relationships)
- **lumina.maint_cost_mro_works_orders** (0 relationships)
- **lumina.manufacturer_codes** (0 relationships)
- **lumina.mavemp** (0 relationships)
- **lumina.mavlog** (0 relationships)
- **lumina.msrfcb** (0 relationships)
- **lumina.narrative_build** (0 relationships)
- **lumina.oeim_booking_base_data** (3 relationships)
- **lumina.oldfcb** (0 relationships)
- **lumina.operation_status** (0 relationships)
- **lumina.osys_to_aircraft_reg** (0 relationships)
- **lumina.part_properties** (0 relationships)
- **lumina.pirep_history_1** (0 relationships)
- **lumina.pirep_history_2** (0 relationships)
- **lumina.pirep_history_3** (0 relationships)
- **lumina.pirep_history_4** (0 relationships)
- **lumina.pirfcb** (0 relationships)
- **lumina.public_holidays** (2 relationships)
- **lumina.puwfcb** (0 relationships)
- **lumina.release_to_service_statement** (1 relationships)
- **lumina.release_types** (0 relationships)
- **lumina.relfcb** (0 relationships)
- **lumina.remfcb** (0 relationships)
- **lumina.removal_history_1** (0 relationships)
- **lumina.reqfil** (0 relationships)
- **lumina.rfc_status_contacts** (0 relationships)
- **lumina.rfid_antenna_txrx_settings** (0 relationships)
- **lumina.rfid_black_listed_tags** (0 relationships)
- **lumina.rfid_readers** (0 relationships)
- **lumina.rfid_users_default_reader** (0 relationships)
- **lumina.rfqfil** (0 relationships)
- **lumina.sabre_fleet_mel_equipment_map** (0 relationships)
- **lumina.sabre_mel_revision_processing** (0 relationships)
- **lumina.sabre_message_queue** (0 relationships)
- **lumina.sabre_messages** (0 relationships)
- **lumina.sap_payment_terms** (0 relationships)
- **lumina.scheduled_job_params** (0 relationships)
- **lumina.schema_version** (0 relationships)
- **lumina.secfcb** (0 relationships)
- **lumina.security_group_links** (0 relationships)
- **lumina.sfdc_comp_change_review_emails** (0 relationships)
- **lumina.shipment_demand_reasons** (0 relationships)
- **lumina.shipment_demand_types** (0 relationships)
- **lumina.shipment_uom_configuration** (0 relationships)
- **lumina.shtnam** (0 relationships)
- **lumina.sopfil** (0 relationships)
- **lumina.srqfil** (0 relationships)
- **lumina.stafcb** (0 relationships)
- **lumina.stcomm** (0 relationships)
- **lumina.stmisc** (0 relationships)
- **lumina.stock_group_depreciation** (0 relationships)
- **lumina.stpfil** (0 relationships)
- **lumina.streci** (0 relationships)
- **lumina.streco** (0 relationships)
- **lumina.strfcb** (0 relationships)
- **lumina.structural_damage_causes** (0 relationships)
- **lumina.structural_damage_parts** (0 relationships)
- **lumina.structural_damage_types** (0 relationships)
- **lumina.stwfcb** (0 relationships)
- **lumina.subchapters** (0 relationships)
- **lumina.suppress_recharge_list** (0 relationships)
- **lumina.sys_paras** (0 relationships)
- **lumina.table_name** (0 relationships)
- **lumina.table_name1** (0 relationships)
- **lumina.tablename** (0 relationships)
- **lumina.tech_log_types** (0 relationships)
- **lumina.tester** (0 relationships)
- **lumina.tmi_undefined** (0 relationships)
- **lumina.trlfcb** (0 relationships)
- **lumina.units_of_measure** (0 relationships)
- **lumina.units_of_measure_con_rates** (0 relationships)
- **lumina.units_of_measure_conversion** (0 relationships)
- **lumina.upnfil** (0 relationships)
- **lumina.warhdr** (0 relationships)
- **lumina.whsfcb** (0 relationships)
- **lumina.worfcb** (0 relationships)
- **lumina.work_schedule_header_1** (0 relationships)
- **lumina.work_schedule_history** (0 relationships)
- **lumina.work_schedule_os_codes** (0 relationships)
- **lumina.works_order_close_amendments** (0 relationships)
- **lumina.works_order_notes** (0 relationships)
- **lumina.works_order_number_list** (0 relationships)
- **lumina.works_orders_by_aircraft** (0 relationships)
- **lumina.xdffcb** (0 relationships)
- **lumina.zones** (0 relationships)

### Level 1

- **lumina.batch_record_camo** (1 relationships)
- **lumina.customs_status_codes** (2 relationships)
- **lumina.fleet_assembles** (1 relationships)
- **lumina.invoice_line_notes** (2 relationships)
- **lumina.licence_categories** (1 relationships)
- **lumina.maint_cost_mro_wo_invoices** (1 relationships)
- **lumina.oeim_invoice** (1 relationships)
- **lumina.oeim_invoice_snap_public_hol** (1 relationships)
- **lumina.oeim_invoice_snap_time_crits** (1 relationships)
- **lumina.oeim_invoice_snap_users** (2 relationships)
- **lumina.repetitive_defect_header_2** (1 relationships)
- **lumina.rp_calendar_addition_type** (1 relationships)

### Level 2

- **lumina.PART_NUMBER_CHAPTERS_DJ-82** (169 relationships)
- **lumina.access_dim_accounts_info** (74 relationships)
- **lumina.access_dim_sales_info** (5 relationships)
- **lumina.accomp_bkup** (10 relationships)
- **lumina.accomp_hist_delta_1763** (12 relationships)
- **lumina.accomp_hist_lost_sched** (10 relationships)
- **lumina.accomp_hist_lost_sched_val** (2 relationships)
- **lumina.accomp_values_bkup** (2 relationships)
- **lumina.accomplishment_history** (31 relationships)
- **lumina.accomplishment_history_values** (2 relationships)
- **lumina.account_amendment_history** (1 relationships)
- **lumina.account_ata_spec_2000_xref** (1 relationships)
- **lumina.account_available_warehouses** (20 relationships)
- **lumina.account_buying_contacts** (2 relationships)
- **lumina.account_header_1** (1 relationships)
- **lumina.account_header_2** (1 relationships)
- **lumina.account_location_email_address** (1 relationships)
- **lumina.account_location_header_1** (1 relationships)
- **lumina.account_location_header_2** (1 relationships)
- **lumina.account_location_header_3** (1 relationships)
- **lumina.account_location_header_4** (1 relationships)
- **lumina.account_location_header_5** (2 relationships)
- **lumina.account_location_header_6** (3 relationships)
- **lumina.account_location_header_7** (1 relationships)
- **lumina.account_location_header_8** (1 relationships)
- **lumina.account_location_header_9** (3 relationships)
- **lumina.account_location_notes** (1 relationships)
- **lumina.account_location_properties** (1 relationships)
- **lumina.account_supplier_approvals** (6 relationships)
- **lumina.account_system_header** (1 relationships)
- **lumina.accs_var_corrections_bkp** (1 relationships)
- **lumina.accum_cycles_static_data** (2 relationships)
- **lumina.add_extension_permissions** (14 relationships)
- **lumina.aircraft_assembles** (121 relationships)
- **lumina.aircraft_build** (3 relationships)
- **lumina.aircraft_build_chapters** (1 relationships)
- **lumina.aircraft_documents** (16 relationships)
- **lumina.aircraft_exclusions** (4 relationships)
- **lumina.aircraft_flight_hours_1** (6 relationships)
- **lumina.aircraft_flight_hours_2** (1 relationships)
- **lumina.aircraft_header_1** (2 relationships)
- **lumina.aircraft_header_2** (2 relationships)
- **lumina.aircraft_lease_details** (2 relationships)
- **lumina.aircraft_leased_apu** (3 relationships)
- **lumina.aircraft_leased_engines** (3 relationships)
- **lumina.aircraft_leased_landing_gear** (3 relationships)
- **lumina.aircraft_leased_propellers** (3 relationships)
- **lumina.aircraft_life** (7 relationships)
- **lumina.aircraft_life_dbf1065** (2 relationships)
- **lumina.aircraft_major_checks** (5 relationships)
- **lumina.aircraft_reg_xref** (1 relationships)
- **lumina.aircraft_short_reg_xref** (1 relationships)
- **lumina.aircraft_statistics** (1 relationships)
- **lumina.aircraft_subchapter_statistics** (1 relationships)
- **lumina.aircraft_weight** (1 relationships)
- **lumina.aircraft_weight_7487bkp** (1 relationships)
- **lumina.aircraft_weight_conf** (4 relationships)
- **lumina.aircraft_weight_conf_entries** (1 relationships)
- **lumina.aircraft_weight_conf_xref** (2 relationships)
- **lumina.airway_bill_references** (6 relationships)
- **lumina.alternate_parts** (11 relationships)
- **lumina.amp_acc_panel_desc_osd_33348** (2 relationships)
- **lumina.amp_access_panel_desc_hdr** (7 relationships)
- **lumina.amp_access_panel_descriptions** (2 relationships)
- **lumina.amp_access_panel_effectivity** (6 relationships)
- **lumina.amp_access_panel_notes** (1 relationships)
- **lumina.amp_access_panels_by_workcard** (100 relationships)
- **lumina.amp_accesspanel_effectivity_jn** (5 relationships)
- **lumina.amp_audit_notes** (9 relationships)
- **lumina.amp_comments** (5 relationships)
- **lumina.amp_component_intervals** (10 relationships)
- **lumina.amp_component_intervals_limits** (3 relationships)
- **lumina.amp_component_intervals_stages** (5 relationships)
- **lumina.amp_component_reset_on_compl** (2 relationships)
- **lumina.amp_data_migration_log** (10 relationships)
- **lumina.amp_datmig_accomplishments** (5 relationships)
- **lumina.amp_datmig_comp_task_lookup** (10 relationships)
- **lumina.amp_datmig_llp** (2 relationships)
- **lumina.amp_document_effectivity** (3 relationships)
- **lumina.amp_document_effectivity_bk** (3 relationships)
- **lumina.amp_documents_by_workcard** (5 relationships)
- **lumina.amp_documents_by_workcard_bk** (5 relationships)
- **lumina.amp_manufacturers_documents** (2 relationships)
- **lumina.amp_material_effectivity** (4 relationships)
- **lumina.amp_material_effectivity_jn** (3 relationships)
- **lumina.amp_materials_required_by_wc** (3 relationships)
- **lumina.amp_package_notes** (33 relationships)
- **lumina.amp_packages** (3 relationships)
- **lumina.amp_packages_by_visit** (3 relationships)
- **lumina.amp_packages_by_workcard** (3 relationships)
- **lumina.amp_planning_notes** (9 relationships)
- **lumina.amp_report_documents** (27 relationships)
- **lumina.amp_revision_history** (75 relationships)
- **lumina.amp_revision_status** (12 relationships)
- **lumina.amp_revisions** (3 relationships)
- **lumina.amp_visit_notes** (2 relationships)
- **lumina.amp_visits** (4 relationships)
- **lumina.amp_wc_aircraft_exclusions** (3 relationships)
- **lumina.amp_wc_in_limits_bak** (2 relationships)
- **lumina.amp_wc_in_stages_bak** (1 relationships)
- **lumina.amp_wcard_extended_desc_41** (2 relationships)
- **lumina.amp_workcard_ac_effectivity** (3 relationships)
- **lumina.amp_workcard_ac_effectivity_jn** (3 relationships)
- **lumina.amp_workcard_accomplishments** (2 relationships)
- **lumina.amp_workcard_activations** (19 relationships)
- **lumina.amp_workcard_call_workcard** (6 relationships)
- **lumina.amp_workcard_cancellations** (5 relationships)
- **lumina.amp_workcard_extended_desc** (2 relationships)
- **lumina.amp_workcard_h3_7487bkp** (2 relationships)
- **lumina.amp_workcard_header_1** (3 relationships)
- **lumina.amp_workcard_header_1_43216** (3 relationships)
- **lumina.amp_workcard_header_2** (2 relationships)
- **lumina.amp_workcard_header_3** (2 relationships)
- **lumina.amp_workcard_header_4** (2 relationships)
- **lumina.amp_workcard_header_5** (3 relationships)
- **lumina.amp_workcard_header_properties** (2 relationships)
- **lumina.amp_workcard_intervals** (16 relationships)
- **lumina.amp_workcard_intervals_limits** (2 relationships)
- **lumina.amp_workcard_intervals_stages** (1 relationships)
- **lumina.amp_workcard_lcl_applicability** (4 relationships)
- **lumina.amp_workcard_narrative** (2 relationships)
- **lumina.amp_workcard_not_with_workcard** (6 relationships)
- **lumina.amp_workcard_previously_acc_by** (4 relationships)
- **lumina.amp_workcard_publications** (7 relationships)
- **lumina.amp_workcard_saved_reports** (4 relationships)
- **lumina.amp_workcard_saved_reports_hdr** (1 relationships)
- **lumina.amp_workcard_sections** (13 relationships)
- **lumina.amp_workcards_by_package** (4 relationships)
- **lumina.amp_workcards_by_section** (4 relationships)
- **lumina.assemble_thrust_life_code** (5 relationships)
- **lumina.assembly_model_header** (3 relationships)
- **lumina.assembly_model_nodes** (3 relationships)
- **lumina.audit_trail** (2 relationships)
- **lumina.audit_trail_ids** (1 relationships)
- **lumina.audit_trail_meta_data** (3 relationships)
- **lumina.bar_codes** (4 relationships)
- **lumina.batch_history** (2 relationships)
- **lumina.batch_notes** (3 relationships)
- **lumina.batch_notes_gu4240** (3 relationships)
- **lumina.batch_orders** (67 relationships)
- **lumina.batch_record_1** (6 relationships)
- **lumina.batch_record_1_gu4240** (6 relationships)
- **lumina.batch_record_2** (3 relationships)
- **lumina.batches_by_airway_bill** (2 relationships)
- **lumina.batches_by_customs_entry** (6 relationships)
- **lumina.bins** (15 relationships)
- **lumina.bkp_mobile_permissions** (2 relationships)
- **lumina.block_countries** (6 relationships)
- **lumina.bulk_batch_header** (2 relationships)
- **lumina.cfd_xref_to_tech_log** (1 relationships)
- **lumina.company_codes** (13 relationships)
- **lumina.company_form_attachments** (7 relationships)
- **lumina.company_form_details** (3 relationships)
- **lumina.completion_fleet_ata_pos** (1 relationships)
- **lumina.completion_life_values** (4 relationships)
- **lumina.completion_maint_mod** (2 relationships)
- **lumina.completion_part_serial** (87 relationships)
- **lumina.component_life** (3 relationships)
- **lumina.component_life_limits** (12 relationships)
- **lumina.component_mods_history_by_part** (1 relationships)
- **lumina.component_movement_hist_life** (16 relationships)
- **lumina.component_movement_history** (2 relationships)
- **lumina.component_movement_history_ext** (7 relationships)
- **lumina.component_movt_hist_ext_8661** (7 relationships)
- **lumina.components** (3 relationships)
- **lumina.components_bkp_dj95** (3 relationships)
- **lumina.components_bkp_dj97** (3 relationships)
- **lumina.components_oases971** (3 relationships)
- **lumina.condition_codes** (10 relationships)
- **lumina.condition_pick_table** (10 relationships)
- **lumina.consumable_batch_locations** (2 relationships)
- **lumina.consumable_history** (8 relationships)
- **lumina.consumable_repair_xref_to_part** (4 relationships)
- **lumina.consumables_below_re_order** (1 relationships)
- **lumina.contacts_xref** (1 relationships)
- **lumina.continents** (3 relationships)
- **lumina.corrosion_categories** (4 relationships)
- **lumina.cost_codes** (20 relationships)
- **lumina.countries** (1 relationships)
- **lumina.cq_documents** (2 relationships)
- **lumina.cq_fixed_charge_xref** (4 relationships)
- **lumina.cq_quote_cards** (14 relationships)
- **lumina.cq_quote_materials** (3 relationships)
- **lumina.cq_quote_nrc_access_panels** (19 relationships)
- **lumina.cq_quote_nrcs** (3 relationships)
- **lumina.cq_quote_packages** (3 relationships)
- **lumina.cq_quote_status** (2 relationships)
- **lumina.cq_quote_status_contacts** (1 relationships)
- **lumina.cq_quotes** (3 relationships)
- **lumina.credit_works_order_cards** (13 relationships)
- **lumina.credit_works_orders** (1 relationships)
- **lumina.crs_signature_text** (2 relationships)
- **lumina.crs_text** (3 relationships)
- **lumina.currency_codes** (35 relationships)
- **lumina.customer_contract_rates** (11 relationships)
- **lumina.customer_contract_stop_incl** (3 relationships)
- **lumina.customer_contracts** (4 relationships)
- **lumina.customer_sales_order_xref** (14 relationships)
- **lumina.customs_tariff_codes** (5 relationships)
- **lumina.customs_tariff_codes_territory** (1 relationships)
- **lumina.daily_loans_out** (3 relationships)
- **lumina.dataset_locks_by_lock_type** (1 relationships)
- **lumina.dataset_locks_by_user** (22 relationships)
- **lumina.default_labour_rates** (3 relationships)
- **lumina.default_labour_windows** (3 relationships)
- **lumina.defect_extensions** (31 relationships)
- **lumina.defect_maint_stages** (1 relationships)
- **lumina.defect_stage_employees** (28 relationships)
- **lumina.deferred_defect_xref_to_cfd_no** (1 relationships)
- **lumina.delay_codes** (6 relationships)
- **lumina.delays** (3 relationships)
- **lumina.delivery_note_extended_remarks** (16 relationships)
- **lumina.delivery_note_header_1** (4 relationships)
- **lumina.delivery_note_header_2** (1 relationships)
- **lumina.delivery_note_header_3** (1 relationships)
- **lumina.delivery_note_header_4** (2 relationships)
- **lumina.delivery_note_item_header_1** (15 relationships)
- **lumina.delivery_note_item_header_2** (2 relationships)
- **lumina.delivery_note_master_list** (1 relationships)
- **lumina.demand_reason_to_movement_code** (9 relationships)
- **lumina.departments** (4 relationships)
- **lumina.dmg_rpr_action_taken_details** (2 relationships)
- **lumina.dmg_rpr_attachments** (2 relationships)
- **lumina.dmg_rpr_ca_approval_details** (2 relationships)
- **lumina.dmg_rpr_corrosion_levels** (2 relationships)
- **lumina.dmg_rpr_damage** (22 relationships)
- **lumina.dmg_rpr_damage_numbering** (3 relationships)
- **lumina.dmg_rpr_damage_types** (3 relationships)
- **lumina.dmg_rpr_dmg_2d_position_labels** (5 relationships)
- **lumina.dmg_rpr_dmg_2d_positions** (2 relationships)
- **lumina.dmg_rpr_doc_effectivity** (5 relationships)
- **lumina.dmg_rpr_doc_subject** (5 relationships)
- **lumina.dmg_rpr_document_order** (4 relationships)
- **lumina.dmg_rpr_documents** (2 relationships)
- **lumina.dmg_rpr_fitted_locations** (4 relationships)
- **lumina.dmg_rpr_idnt_inspect** (1 relationships)
- **lumina.dmg_rpr_idnt_inspect_info** (1 relationships)
- **lumina.dmg_rpr_inspection_type_dtls** (7 relationships)
- **lumina.dmg_rpr_inspections** (9 relationships)
- **lumina.dmg_rpr_interim_repairs** (9 relationships)
- **lumina.dmg_rpr_location** (5 relationships)
- **lumina.dmg_rpr_location_measurement** (6 relationships)
- **lumina.dmg_rpr_mat_types_fld_dtls** (1 relationships)
- **lumina.dmg_rpr_material_types_dtls** (4 relationships)
- **lumina.dmg_rpr_measurement_sections** (4 relationships)
- **lumina.dmg_rpr_measurement_zones** (5 relationships)
- **lumina.dmg_rpr_measurements** (1 relationships)
- **lumina.dmg_rpr_permanent_repairs** (7 relationships)
- **lumina.dmg_rpr_repair_req_details** (2 relationships)
- **lumina.dmg_rpr_section_details** (1 relationships)
- **lumina.dmg_rpr_section_fleet_details** (1 relationships)
- **lumina.dmg_rpr_stage_limits** (3 relationships)
- **lumina.dmg_rpr_stages** (5 relationships)
- **lumina.dmg_rpr_subject_sections** (4 relationships)
- **lumina.dmg_rpr_subject_zones** (3 relationships)
- **lumina.dmg_rpr_surface_finish_details** (3 relationships)
- **lumina.dmg_rpr_time_limited_repairs** (9 relationships)
- **lumina.document_classes** (11 relationships)
- **lumina.document_image_source** (27 relationships)
- **lumina.document_image_types** (1 relationships)
- **lumina.document_images** (1 relationships)
- **lumina.document_images_jn** (1 relationships)
- **lumina.drn_class_codes** (1 relationships)
- **lumina.drn_component_mods_history** (3 relationships)
- **lumina.drn_components_nsbl_history** (3 relationships)
- **lumina.drn_cycles** (3 relationships)
- **lumina.drn_fleet_ata** (2 relationships)
- **lumina.drn_life_limits** (4 relationships)
- **lumina.drn_maint_mod** (3 relationships)
- **lumina.drn_maint_mod_notes** (1 relationships)
- **lumina.drn_maintenance_history** (3 relationships)
- **lumina.drn_maintenance_history_notes** (1 relationships)
- **lumina.drn_mod_desc_order_hist** (2 relationships)
- **lumina.drn_modification_history** (3 relationships)
- **lumina.drn_modification_history_notes** (1 relationships)
- **lumina.drn_part_serial** (3 relationships)
- **lumina.dues_register** (4 relationships)
- **lumina.dummy_part_numbers** (1 relationships)
- **lumina.easa_trace** (3 relationships)
- **lumina.economic_blocks** (1 relationships)
- **lumina.email_notification** (2 relationships)
- **lumina.email_notification_categories** (3 relationships)
- **lumina.email_template** (3 relationships)
- **lumina.employee_experience_details** (3 relationships)
- **lumina.employee_presence** (1 relationships)
- **lumina.employee_presence_log** (2 relationships)
- **lumina.employee_training_details** (4 relationships)
- **lumina.employees** (2 relationships)
- **lumina.employees_licences** (4 relationships)
- **lumina.end_use_codes** (5 relationships)
- **lumina.engineering_support_history** (4 relationships)
- **lumina.esign_off_nrc** (2 relationships)
- **lumina.export_codes** (8 relationships)
- **lumina.extended_part_descriptions** (1 relationships)
- **lumina.extensions** (1 relationships)
- **lumina.fixed_charges** (1 relationships)
- **lumina.fleet_chap_part_header_1** (2 relationships)
- **lumina.fleet_chap_part_header_2** (1 relationships)
- **lumina.fleet_chap_part_header_3** (1 relationships)
- **lumina.fleet_chapter_part_aircraft** (2 relationships)
- **lumina.fleet_forecast_plans** (4 relationships)
- **lumina.fleet_forecast_plans_amp** (4 relationships)
- **lumina.fleet_forecast_plans_drn** (3 relationships)
- **lumina.fleet_forecast_plans_rfc** (35 relationships)
- **lumina.fleet_header_2** (1 relationships)
- **lumina.fleet_statistics** (1 relationships)
- **lumina.float_history** (2 relationships)
- **lumina.flown_sectors** (9 relationships)
- **lumina.flown_sectors_bkp** (4 relationships)
- **lumina.flown_sectors_con_680** (4 relationships)
- **lumina.flown_sectors_delta1817** (4 relationships)
- **lumina.forecast_cache** (11 relationships)
- **lumina.forecast_cache_ac_details** (1 relationships)
- **lumina.forecast_cache_revisions** (3 relationships)
- **lumina.forecast_filter_groups** (10 relationships)
- **lumina.forecast_filters** (2 relationships)
- **lumina.forecast_parameters** (2 relationships)
- **lumina.forecast_variation_details** (4 relationships)
- **lumina.form_number** (4 relationships)
- **lumina.forward_schedule_summary_vals** (1 relationships)
- **lumina.freight_cost_markups** (10 relationships)
- **lumina.freight_costs** (3 relationships)
- **lumina.future_flights** (1 relationships)
- **lumina.gl_global_codes** (2 relationships)
- **lumina.goods_received_sheet_document** (7 relationships)
- **lumina.hazardous_materials** (1 relationships)
- **lumina.ie96_historic** (8 relationships)
- **lumina.inherited_acquisition_costs** (3 relationships)
- **lumina.invoice_lines** (7 relationships)
- **lumina.invoice_system_header** (1 relationships)
- **lumina.invoice_trail_entries** (8 relationships)
- **lumina.invoices** (3 relationships)
- **lumina.jasper_workcard_templates** (1 relationships)
- **lumina.lasers_system_header** (1 relationships)
- **lumina.latest_repair_values** (3 relationships)
- **lumina.ldt** (1 relationships)
- **lumina.le80_defect_temp** (1 relationships)
- **lumina.life_code_entry** (3 relationships)
- **lumina.life_code_entry_backup** (3 relationships)
- **lumina.life_code_entry_dbf1065** (3 relationships)
- **lumina.life_code_levels** (27 relationships)
- **lumina.life_codes** (1 relationships)
- **lumina.lmc_base_data_options** (4 relationships)
- **lumina.lmc_base_data_reported_wc** (2 relationships)
- **lumina.loaned_units** (4 relationships)
- **lumina.long_serial_number_xref** (7 relationships)
- **lumina.maint_accomplishment_costs** (2 relationships)
- **lumina.maint_associated_cost_aircraft** (5 relationships)
- **lumina.maint_associated_costs** (2 relationships)
- **lumina.maint_card_pref_cost_cats** (1 relationships)
- **lumina.maint_cost_budget_adsb** (26 relationships)
- **lumina.maint_cost_budget_aircraft** (2 relationships)
- **lumina.maint_cost_budget_cfds** (3 relationships)
- **lumina.maint_cost_budget_costs** (6 relationships)
- **lumina.maint_cost_budget_defects** (3 relationships)
- **lumina.maint_cost_budget_labour_ests** (4 relationships)
- **lumina.maint_cost_budget_materials** (4 relationships)
- **lumina.maint_cost_budget_packages** (5 relationships)
- **lumina.maint_cost_budget_visits** (5 relationships)
- **lumina.maint_cost_budget_workcards** (9 relationships)
- **lumina.maint_cost_hourly_rate_set** (4 relationships)
- **lumina.maint_cost_hourly_rates** (4 relationships)
- **lumina.maint_cost_mro_wo_quotes** (1 relationships)
- **lumina.maint_cost_time_categories** (3 relationships)
- **lumina.maint_cost_time_category_set** (23 relationships)
- **lumina.maint_hist_associated_costs** (2 relationships)
- **lumina.maint_historic_defects** (1 relationships)
- **lumina.maint_labour_costs** (1 relationships)
- **lumina.maint_material_costs** (6 relationships)
- **lumina.maint_nrc_costs** (2 relationships)
- **lumina.maint_pack_pref_cost_cats** (1 relationships)
- **lumina.maint_works_order_costs** (1 relationships)
- **lumina.maintenance_cat_excl_subchap** (1 relationships)
- **lumina.maintenance_cat_incl_chapter** (1 relationships)
- **lumina.maintenance_cat_incl_parts** (2 relationships)
- **lumina.maintenance_cost_budgets** (1 relationships)
- **lumina.maintenance_cost_cat_fleet** (1 relationships)
- **lumina.maintenance_cost_categories** (1 relationships)
- **lumina.maintenance_cost_entry** (2 relationships)
- **lumina.maintenance_cost_invoices** (2 relationships)
- **lumina.maintenance_cost_quotes** (3 relationships)
- **lumina.maintenance_cost_types** (3 relationships)
- **lumina.mandatory_parts** (1 relationships)
- **lumina.manufacturers_work_documents** (2 relationships)
- **lumina.marketing_codes** (3 relationships)
- **lumina.markups** (1 relationships)
- **lumina.material_pool_agreement** (5 relationships)
- **lumina.material_pool_agreement_ac** (2 relationships)
- **lumina.material_pool_agreement_pn** (2 relationships)
- **lumina.mavis_system_header** (1 relationships)
- **lumina.maximum_preload_pick_quantity** (1 relationships)
- **lumina.measurement_alerts_aircraft** (4 relationships)
- **lumina.measurement_alerts_fleet** (3 relationships)
- **lumina.mel_items** (1 relationships)
- **lumina.mel_references** (1 relationships)
- **lumina.mel_revision_history** (6 relationships)
- **lumina.mel_revisions** (2 relationships)
- **lumina.monthly_loans_in** (3 relationships)
- **lumina.monthly_loans_out** (3 relationships)
- **lumina.movement_codes** (1 relationships)
- **lumina.n_s_extended_part_descriptions** (1 relationships)
- **lumina.netline_import_index** (1 relationships)
- **lumina.no_narrative_default** (1 relationships)
- **lumina.non_stock_parts** (4 relationships)
- **lumina.non_stock_parts_bkp_oases382** (2 relationships)
- **lumina.nrc_access_panels** (2 relationships)
- **lumina.nrc_defect_details** (3 relationships)
- **lumina.nrc_defect_notes** (2 relationships)
- **lumina.nrc_documents** (4 relationships)
- **lumina.nrc_high_sequence_control** (15 relationships)
- **lumina.nrc_materials** (2 relationships)
- **lumina.nrc_print_history** (4 relationships)
- **lumina.nrc_properties** (1 relationships)
- **lumina.nrc_rectification_notes** (2 relationships)
- **lumina.nrc_requirements_actions** (31 relationships)
- **lumina.nrc_status_history** (5 relationships)
- **lumina.nrc_tools** (2 relationships)
- **lumina.nrc_workcard_narrative** (1 relationships)
- **lumina.nrc_xref_to_scheduled_workcard** (3 relationships)
- **lumina.oases_message_log** (1 relationships)
- **lumina.oases_reports** (2 relationships)
- **lumina.oeim_credit_warranty** (6 relationships)
- **lumina.oeim_invoice_cards** (3 relationships)
- **lumina.oeim_invoice_fixed_charges** (2 relationships)
- **lumina.oeim_invoice_inclusive_hrs** (3 relationships)
- **lumina.oeim_invoice_materials** (8 relationships)
- **lumina.oeim_invoice_packages** (3 relationships)
- **lumina.oeim_invoice_snap_con_rates** (3 relationships)
- **lumina.oeim_invoice_snap_cost_codes** (2 relationships)
- **lumina.oeim_invoice_snap_currencies** (2 relationships)
- **lumina.oeim_invoice_snap_departments** (3 relationships)
- **lumina.oeim_invoice_snap_employees** (3 relationships)
- **lumina.oeim_invoice_snap_part_master** (2 relationships)
- **lumina.oeim_invoice_snap_pay_types** (2 relationships)
- **lumina.oeim_invoice_snap_pm_bkup** (2 relationships)
- **lumina.oeim_invoice_snap_serl_master** (4 relationships)
- **lumina.oeim_invoice_snap_sfdc_book** (5 relationships)
- **lumina.oeim_invoice_snap_time_cats** (2 relationships)
- **lumina.oeim_invoice_snap_vat_codes** (3 relationships)
- **lumina.oeim_invoice_warranty** (8 relationships)
- **lumina.oeim_invoice_warranty_refunds** (7 relationships)
- **lumina.oeim_invoice_works_orders** (2 relationships)
- **lumina.oeim_quote_dismissed** (4 relationships)
- **lumina.oeim_transaction_log_details** (2 relationships)
- **lumina.oeim_transaction_log_header** (1 relationships)
- **lumina.ord_po_unit_conv_delta1827** (1 relationships)
- **lumina.order_change_history** (3 relationships)
- **lumina.order_customs_info** (1 relationships)
- **lumina.order_delivery_note_remarks** (1 relationships)
- **lumina.order_email_chasing** (1 relationships)
- **lumina.order_goods_received** (3 relationships)
- **lumina.order_goods_received_invoices** (4 relationships)
- **lumina.order_header_1** (5 relationships)
- **lumina.order_header_2** (2 relationships)
- **lumina.order_header_3** (2 relationships)
- **lumina.order_header_4** (2 relationships)
- **lumina.order_history** (7 relationships)
- **lumina.order_line_additional_info** (5 relationships)
- **lumina.order_line_additional_info_2** (1 relationships)
- **lumina.order_line_notes** (1 relationships)
- **lumina.order_line_quotes_data** (3 relationships)
- **lumina.order_line_requirement_xref** (2 relationships)
- **lumina.order_line_weight_dimension** (3 relationships)
- **lumina.order_lines** (5 relationships)
- **lumina.order_numbers_by_supplier** (2 relationships)
- **lumina.order_print_date** (1 relationships)
- **lumina.order_purchase_unit_conversion** (1 relationships)
- **lumina.order_requirement_allocation** (3 relationships)
- **lumina.order_standard_text_blocks** (1 relationships)
- **lumina.order_supplier_approval** (2 relationships)
- **lumina.order_text** (1 relationships)
- **lumina.order_workshop_works_orders** (1 relationships)
- **lumina.orders_by_due_date** (1 relationships)
- **lumina.orders_to_part_number_xref** (2 relationships)
- **lumina.ordr_goods_bkp** (3 relationships)
- **lumina.original_purchase_values** (3 relationships)
- **lumina.osys_defect_act_to_defect_id** (1 relationships)
- **lumina.osys_defect_to_defect_id** (2 relationships)
- **lumina.osys_defect_to_tech_log_line** (1 relationships)
- **lumina.osys_key_to_reportid** (13 relationships)
- **lumina.outstation_codes** (2 relationships)
- **lumina.package** (2 relationships)
- **lumina.package_items** (5 relationships)
- **lumina.paragraph_cancels** (19 relationships)
- **lumina.part_applicability_codes** (1 relationships)
- **lumina.part_change_warning_chapters** (1 relationships)
- **lumina.part_change_warnings** (1 relationships)
- **lumina.part_customs_tariff_territory** (2 relationships)
- **lumina.part_master** (2 relationships)
- **lumina.part_master_bkp_oases382** (2 relationships)
- **lumina.part_number_amendment_history** (2 relationships)
- **lumina.part_number_chapters** (1 relationships)
- **lumina.part_number_essentiality_codes** (3 relationships)
- **lumina.part_number_marketing_codes** (2 relationships)
- **lumina.part_number_order_retention** (1 relationships)
- **lumina.part_number_owner_float_levels** (1 relationships)
- **lumina.part_number_properties** (1 relationships)
- **lumina.part_number_properties_serials** (2 relationships)
- **lumina.part_number_shelf_life_details** (2 relationships)
- **lumina.part_number_technical_notes** (1 relationships)
- **lumina.part_number_vat_codes** (2 relationships)
- **lumina.part_serial_documents** (5 relationships)
- **lumina.part_serial_master_list** (1 relationships)
- **lumina.part_xref_to_pick_history** (3 relationships)
- **lumina.parts_customs_tariff_codes** (2 relationships)
- **lumina.parts_freight_tiered_markups** (1 relationships)
- **lumina.parts_received_without_cost** (2 relationships)
- **lumina.parts_requiring_export_licence** (1 relationships)
- **lumina.payment_types** (3 relationships)
- **lumina.pdc_import_index** (1 relationships)
- **lumina.pick_hist_7890_bkp** (6 relationships)
- **lumina.pick_history** (6 relationships)
- **lumina.pirep_index_data** (1 relationships)
- **lumina.planners_notes** (4 relationships)
- **lumina.planners_notes_categories** (2 relationships)
- **lumina.planners_notes_statuses** (1 relationships)
- **lumina.planners_notes_xref** (11 relationships)
- **lumina.prefered_bins** (1 relationships)
- **lumina.preferred_suppliers_by_part** (2 relationships)
- **lumina.preorder_line_requirement_xref** (9 relationships)
- **lumina.preorder_line_stock_info** (5 relationships)
- **lumina.preorder_lines** (6 relationships)
- **lumina.preorders** (5 relationships)
- **lumina.price_codes** (2 relationships)
- **lumina.price_types** (4 relationships)
- **lumina.purchase_demand_by_part** (1 relationships)
- **lumina.quote_email_chasing** (1 relationships)
- **lumina.quotes_by_part** (3 relationships)
- **lumina.quotes_for_part_by_account** (2 relationships)
- **lumina.random_stock_check_bins** (6 relationships)
- **lumina.random_stock_check_date** (1 relationships)
- **lumina.random_stock_check_log** (1 relationships)
- **lumina.random_stock_check_parts** (2 relationships)
- **lumina.rd_xref_to_tech_logs** (4 relationships)
- **lumina.rdi_history** (3 relationships)
- **lumina.rdi_to_nrc** (2 relationships)
- **lumina.release_codes** (6 relationships)
- **lumina.reliability_report_logo_desc** (3 relationships)
- **lumina.removals** (2 relationships)
- **lumina.repair_approval_data** (3 relationships)
- **lumina.repetitive_defect_header_1** (2 relationships)
- **lumina.repetitive_defect_narrative** (2 relationships)
- **lumina.repetitive_defect_tech_logs** (2 relationships)
- **lumina.req_priority_desc_oases_1228** (6 relationships)
- **lumina.requests_for_quotes** (1 relationships)
- **lumina.requests_for_quotes_lines** (4 relationships)
- **lumina.requests_for_quotes_notes** (1 relationships)
- **lumina.requirement_planners_notes** (1 relationships)
- **lumina.requirement_priority_codes** (1 relationships)
- **lumina.requirement_priority_desc** (1 relationships)
- **lumina.requirement_priority_leadtimes** (1 relationships)
- **lumina.requirement_priority_sla** (2 relationships)
- **lumina.requirement_recharge_details** (5 relationships)
- **lumina.requirement_source_codes** (1 relationships)
- **lumina.requirement_to_rfq_xref** (15 relationships)
- **lumina.requirements** (8 relationships)
- **lumina.rfc_accomplishment** (1 relationships)
- **lumina.rfc_aircraft** (5 relationships)
- **lumina.rfc_change_origin** (5 relationships)
- **lumina.rfc_components** (6 relationships)
- **lumina.rfc_documents** (4 relationships)
- **lumina.rfc_download_effectivity** (2 relationships)
- **lumina.rfc_download_origin_codes** (3 relationships)
- **lumina.rfc_download_taxonomy** (4 relationships)
- **lumina.rfc_effectivity_ata** (1 relationships)
- **lumina.rfc_effectivity_fleet** (1 relationships)
- **lumina.rfc_effectivity_part** (2 relationships)
- **lumina.rfc_evaluation_history** (3 relationships)
- **lumina.rfc_evaluation_stages** (1 relationships)
- **lumina.rfc_frequency_phase_header** (17 relationships)
- **lumina.rfc_frequency_phase_limits** (4 relationships)
- **lumina.rfc_frequency_phases** (4 relationships)
- **lumina.rfc_header** (5 relationships)
- **lumina.rfc_header_publications** (2 relationships)
- **lumina.rfc_na_notes** (2 relationships)
- **lumina.rfc_paragraphs** (2 relationships)
- **lumina.rfc_policies** (1 relationships)
- **lumina.rfc_print_history_log** (2 relationships)
- **lumina.rfc_publications** (1 relationships)
- **lumina.rfc_regulating_authority** (6 relationships)
- **lumina.rfc_relationships** (1 relationships)
- **lumina.rfc_statement_sections** (2 relationships)
- **lumina.rfc_status** (3 relationships)
- **lumina.rfc_transaction_log** (2 relationships)
- **lumina.rfq_by_part_number** (2 relationships)
- **lumina.rfq_history** (5 relationships)
- **lumina.rfq_quote_received** (3 relationships)
- **lumina.rfq_quote_received_notes** (2 relationships)
- **lumina.rfq_requirement_xref** (2 relationships)
- **lumina.rfq_supplier_details** (2 relationships)
- **lumina.rfq_supplier_notes** (2 relationships)
- **lumina.rfq_to_order_xref** (3 relationships)
- **lumina.rotable_batch_locations** (9 relationships)
- **lumina.rotable_float_values** (1 relationships)
- **lumina.rotable_history** (9 relationships)
- **lumina.rotables_below_re_order** (1 relationships)
- **lumina.rp_base_plan_header** (6 relationships)
- **lumina.rp_basic_shift** (11 relationships)
- **lumina.rp_block_resource** (5 relationships)
- **lumina.rp_block_resource_days** (3 relationships)
- **lumina.rp_dependencies** (4 relationships)
- **lumina.rp_employee_allocation** (4 relationships)
- **lumina.rp_employee_allocation_header** (5 relationships)
- **lumina.rp_employee_calendar_addition** (5 relationships)
- **lumina.rp_employee_calendar_pattern** (3 relationships)
- **lumina.rp_milestone_history** (8 relationships)
- **lumina.rp_milestones** (2 relationships)
- **lumina.rp_shift_pattern** (4 relationships)
- **lumina.rp_shift_pattern_header** (1 relationships)
- **lumina.rp_weekends** (2 relationships)
- **lumina.rp_wo_base_estimated_defects** (3 relationships)
- **lumina.rp_wo_base_milestones** (2 relationships)
- **lumina.rp_wo_base_nrc_plan** (3 relationships)
- **lumina.rp_wo_base_workcard_plan** (3 relationships)
- **lumina.rp_wo_estimated_defects** (2 relationships)
- **lumina.rp_wo_milestones** (1 relationships)
- **lumina.rp_wo_nrc_plan** (2 relationships)
- **lumina.rp_wo_workcard_plan** (2 relationships)
- **lumina.sabre_flight_map** (1 relationships)
- **lumina.sabre_trace** (1 relationships)
- **lumina.sage_order_line_details** (1 relationships)
- **lumina.sales_history** (7 relationships)
- **lumina.sales_invoice_genled_xref** (1 relationships)
- **lumina.sales_invoices_xref** (2 relationships)
- **lumina.sales_notes_for_part** (1 relationships)
- **lumina.sales_order_dispatches** (7 relationships)
- **lumina.sales_order_history** (1 relationships)
- **lumina.sales_order_lines** (3 relationships)
- **lumina.sales_order_notes** (1 relationships)
- **lumina.sales_order_parameters** (1 relationships)
- **lumina.sales_order_payments** (3 relationships)
- **lumina.sales_orders** (4 relationships)
- **lumina.sales_orders_by_part** (2 relationships)
- **lumina.sales_prices** (6 relationships)
- **lumina.sales_quotes_out_history** (5 relationships)
- **lumina.sales_request_quote_detail** (13 relationships)
- **lumina.sales_request_quote_header** (5 relationships)
- **lumina.sales_request_quote_notes** (1 relationships)
- **lumina.sales_requested_unknown_parts** (3 relationships)
- **lumina.sales_requests_by_part** (2 relationships)
- **lumina.sales_requests_by_unknown_part** (2 relationships)
- **lumina.sample_fleets** (2 relationships)
- **lumina.sample_fleets_jn** (2 relationships)
- **lumina.sap_order_header** (2 relationships)
- **lumina.sap_order_line** (2 relationships)
- **lumina.schedule_forecast_xref** (9 relationships)
- **lumina.schedule_source** (4 relationships)
- **lumina.scope_type_rating** (4 relationships)
- **lumina.sectors** (1 relationships)
- **lumina.security_audit_log_header** (4 relationships)
- **lumina.security_audit_log_meta_data** (2 relationships)
- **lumina.security_group_perm_attribute** (7 relationships)
- **lumina.security_group_permissions** (2 relationships)
- **lumina.security_group_policies** (2 relationships)
- **lumina.security_groups** (1 relationships)
- **lumina.security_permission_def_attrib** (2 relationships)
- **lumina.security_policy** (8 relationships)
- **lumina.security_policy_perm_attribute** (3 relationships)
- **lumina.security_policy_permissions** (2 relationships)
- **lumina.security_user_effectivity** (2 relationships)
- **lumina.security_user_groups** (1 relationships)
- **lumina.security_user_notifications** (3 relationships)
- **lumina.security_user_perm_attribute** (2 relationships)
- **lumina.security_user_permissions** (1 relationships)
- **lumina.security_user_permissions_bkp** (1 relationships)
- **lumina.security_user_policies** (1 relationships)
- **lumina.serial_numbers_by_part** (2 relationships)
- **lumina.sfdc_activity** (4 relationships)
- **lumina.sfdc_bookings** (4 relationships)
- **lumina.sfdc_component_changes** (3 relationships)
- **lumina.sfdc_deleted_bookings** (4 relationships)
- **lumina.sfdc_open_bookings** (3 relationships)
- **lumina.shelf_li_dt_bkp_2020** (5 relationships)
- **lumina.shelf_life_dates** (8 relationships)
- **lumina.shelf_life_dates_oases6834** (5 relationships)
- **lumina.shelf_life_expiry_req_codes** (1 relationships)
- **lumina.shipment** (9 relationships)
- **lumina.shipment_demands** (7 relationships)
- **lumina.shipment_documents** (3 relationships)
- **lumina.shipment_item** (8 relationships)
- **lumina.shipment_item_customs** (3 relationships)
- **lumina.shipment_item_demands** (2 relationships)
- **lumina.shipment_order_demands** (3 relationships)
- **lumina.shipment_requirement_demands** (3 relationships)
- **lumina.shipment_status** (4 relationships)
- **lumina.shipment_status_type** (2 relationships)
- **lumina.shipment_stocktransfer_demands** (1 relationships)
- **lumina.shipment_works_orders_demands** (1 relationships)
- **lumina.short_long_serials** (2 relationships)
- **lumina.skill_codes** (2 relationships)
- **lumina.sold_hours_history** (1 relationships)
- **lumina.stock_audit_batches** (6 relationships)
- **lumina.stock_audit_bins** (2 relationships)
- **lumina.stock_audits** (2 relationships)
- **lumina.stock_by_bin** (2 relationships)
- **lumina.stock_documents** (4 relationships)
- **lumina.stock_group_additional_data** (1 relationships)
- **lumina.stock_groups** (1 relationships)
- **lumina.stock_groups_bkp_oases382** (1 relationships)
- **lumina.stock_works_order_markups** (1 relationships)
- **lumina.strip_documents** (4 relationships)
- **lumina.strip_report_findings_text** (8 relationships)
- **lumina.strip_report_header_1** (6 relationships)
- **lumina.strip_report_header_2** (1 relationships)
- **lumina.strip_report_modification_text** (1 relationships)
- **lumina.structural_damage** (2 relationships)
- **lumina.sub_fleet_header** (15 relationships)
- **lumina.sub_fleets** (2 relationships)
- **lumina.sub_fleets_jn** (2 relationships)
- **lumina.supplier_loan_contract_rates** (1 relationships)
- **lumina.system_header_icarus** (1 relationships)
- **lumina.talend_jobs** (2 relationships)
- **lumina.task_activity_link** (6 relationships)
- **lumina.taskcard_wo_order_line** (1 relationships)
- **lumina.tech_log_1** (1 relationships)
- **lumina.tech_log_2** (3 relationships)
- **lumina.tech_log_3** (6 relationships)
- **lumina.tech_log_defect_text** (1 relationships)
- **lumina.tech_log_documents** (2 relationships)
- **lumina.tech_log_nrc_xref** (1 relationships)
- **lumina.tech_log_rectification_text** (2 relationships)
- **lumina.tech_log_workcard_link** (2 relationships)
- **lumina.temp_rfc_paragraphs** (2 relationships)
- **lumina.test_table** (1 relationships)
- **lumina.third_party_account_id** (2 relationships)
- **lumina.tiered_markup_range** (1 relationships)
- **lumina.time_categories** (2 relationships)
- **lumina.tool_check_out_in** (3 relationships)
- **lumina.tool_check_out_in_duplicates** (3 relationships)
- **lumina.trades** (14 relationships)
- **lumina.training_details** (1 relationships)
- **lumina.transaction_header_mavis** (1 relationships)
- **lumina.transaction_header_trex_lasers** (1 relationships)
- **lumina.transaction_log_icarus** (13 relationships)
- **lumina.transaction_log_icarus_8134** (13 relationships)
- **lumina.transaction_log_lasers** (2 relationships)
- **lumina.transaction_log_mavis** (2 relationships)
- **lumina.transaction_log_trecs** (2 relationships)
- **lumina.transaction_types** (3 relationships)
- **lumina.uf_forecast_cache** (11 relationships)
- **lumina.unit_owners** (3 relationships)
- **lumina.unknown_part_numbers** (2 relationships)
- **lumina.unmatched_issues_and_returns** (2 relationships)
- **lumina.unsatified_service_exchanges** (4 relationships)
- **lumina.uom_conversion_at_part_level** (1 relationships)
- **lumina.user_warehouse_access** (2 relationships)
- **lumina.variations** (3 relationships)
- **lumina.variations_xref** (9 relationships)
- **lumina.variations_xref_overrides** (2 relationships)
- **lumina.vat_codes** (2 relationships)
- **lumina.warehouse_distribution** (2 relationships)
- **lumina.warehouse_header_1** (1 relationships)
- **lumina.warehouse_header_2** (2 relationships)
- **lumina.warehouse_lmc_email_address** (1 relationships)
- **lumina.warehouse_replenishment_data** (2 relationships)
- **lumina.warranty_claims** (7 relationships)
- **lumina.warranty_exclusions** (4 relationships)
- **lumina.warranty_terms** (8 relationships)
- **lumina.warranty_terms_documents** (2 relationships)
- **lumina.wcr_boeing_tb_revision** (4 relationships)
- **lumina.wcr_msg_log** (2 relationships)
- **lumina.wcr_temp_access_panels** (3 relationships)
- **lumina.wcr_temp_base1** (8 relationships)
- **lumina.wcr_temp_narratives** (3 relationships)
- **lumina.weight_and_balance_documents** (3 relationships)
- **lumina.wo_auto_amended_contacts** (1 relationships)
- **lumina.wo_releases** (1 relationships)
- **lumina.work_sch_def_2_lg318** (2 relationships)
- **lumina.work_schedule_defect_1** (3 relationships)
- **lumina.work_schedule_defect_2** (2 relationships)
- **lumina.work_schedule_defect_3** (5 relationships)
- **lumina.work_schedule_defect_4** (4 relationships)
- **lumina.work_schedule_header_2** (2 relationships)
- **lumina.work_schedule_header_3** (1 relationships)
- **lumina.work_schedule_ms_codes** (1 relationships)
- **lumina.work_schedule_trades** (1 relationships)
- **lumina.work_schedule_workcards** (2 relationships)
- **lumina.work_schedule_zones** (1 relationships)
- **lumina.workcard_accomplishments** (1 relationships)
- **lumina.workcard_activations** (2 relationships)
- **lumina.workcard_cancellations** (2 relationships)
- **lumina.workcard_default_status** (1 relationships)
- **lumina.workcard_documents_filter** (2 relationships)
- **lumina.workcard_form_number** (2 relationships)
- **lumina.workcard_forms** (2 relationships)
- **lumina.workcard_properties** (1 relationships)
- **lumina.workcard_status_codes** (1 relationships)
- **lumina.workpack_printing_control** (1 relationships)
- **lumina.works_order_contracts** (2 relationships)
- **lumina.works_order_documents** (1 relationships)
- **lumina.works_order_issues_and_returns** (4 relationships)
- **lumina.works_order_issues_and_rtn_bac** (4 relationships)
- **lumina.works_order_markup_header** (1 relationships)
- **lumina.works_order_markup_table** (1 relationships)
- **lumina.works_order_sub_status** (4 relationships)
- **lumina.works_orders** (7 relationships)
- **lumina.works_orders_by_account** (2 relationships)
- **lumina.works_orders_by_part_number** (1 relationships)

---

## Highly Connected Tables

Tables with the most relationships (central entities):

| Rank | Table | Total Relationships | Incoming | Outgoing |
|------|-------|---------------------|----------|----------|
| 1 | `lumina.PART_NUMBER_CHAPTERS_DJ-82` | 169 | 168 | 1 |
| 2 | `lumina.aircraft_assembles` | 121 | 120 | 1 |
| 3 | `lumina.amp_access_panels_by_workcard` | 100 | 97 | 3 |
| 4 | `lumina.completion_part_serial` | 87 | 85 | 2 |
| 5 | `lumina.amp_revision_history` | 75 | 72 | 3 |
| 6 | `lumina.access_dim_accounts_info` | 74 | 70 | 4 |
| 7 | `lumina.batch_orders` | 67 | 65 | 2 |
| 8 | `lumina.batch_file_header` | 51 | 51 | 0 |
| 9 | `lumina.invoice_categories` | 37 | 37 | 0 |
| 10 | `lumina.currency_codes` | 35 | 34 | 1 |
| 11 | `lumina.fleet_forecast_plans_rfc` | 35 | 33 | 2 |
| 12 | `lumina.amp_datmig_fleet_visit_pack` | 33 | 33 | 0 |
| 13 | `lumina.amp_package_notes` | 33 | 31 | 2 |
| 14 | `lumina.accomplishment_history` | 31 | 19 | 12 |
| 15 | `lumina.defect_extensions` | 31 | 29 | 2 |
| 16 | `lumina.nrc_requirements_actions` | 31 | 28 | 3 |
| 17 | `lumina.defect_stage_employees` | 28 | 24 | 4 |
| 18 | `lumina.amp_report_documents` | 27 | 25 | 2 |
| 19 | `lumina.document_image_source` | 27 | 26 | 1 |
| 20 | `lumina.life_code_levels` | 27 | 25 | 2 |

---

## Detailed Relationships

Complete list of all table relationships:

### lumina.PART_NUMBER_CHAPTERS_DJ-82

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

**Referenced By (Incoming):**

- `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number` → `part_number`
- `lumina.accomp_bkup.part_number` → `part_number`
- `lumina.accomp_hist_delta_1763.part_number` → `part_number`
- `lumina.accomp_hist_lost_sched.part_number` → `part_number`
- `lumina.accomplishment_history.part_number` → `part_number`
- `lumina.accum_cycles_static_data.part_number` → `part_number`
- `lumina.aircraft_build.part_number` → `part_number`
- `lumina.aircraft_leased_apu.part_number` → `part_number`
- `lumina.aircraft_leased_engines.part_number` → `part_number`
- `lumina.aircraft_leased_landing_gear.part_number` → `part_number`
- `lumina.aircraft_leased_propellers.part_number` → `part_number`
- `lumina.aircraft_major_checks.part_number` → `part_number`
- `lumina.alternate_parts.part_number` → `part_number`
- `lumina.amp_component_intervals.part_number` → `part_number`
- `lumina.amp_datmig_accomplishments.part_number` → `part_number`
- `lumina.amp_datmig_llp.part_number` → `part_number`
- `lumina.amp_material_effectivity.part_number` → `part_number`
- `lumina.amp_material_effectivity_jn.part_number` → `part_number`
- `lumina.amp_workcard_intervals.part_number` → `part_number`
- `lumina.batch_notes.part_number` → `part_number`
- `lumina.batch_notes_gu4240.part_number` → `part_number`
- `lumina.batch_record_1.part_number` → `part_number`
- `lumina.batch_record_1_gu4240.part_number` → `part_number`
- `lumina.completion_life_values.part_number` → `part_number`
- `lumina.completion_part_serial.part_number` → `part_number`
- `lumina.component_life.part_number` → `part_number`
- `lumina.component_mods_history_by_part.part_number` → `part_number`
- `lumina.component_movement_hist_life.part_number` → `part_number`
- `lumina.component_movement_history.part_number` → `part_number`
- `lumina.component_movement_history_ext.part_number` → `part_number`
- `lumina.component_movt_hist_ext_8661.part_number` → `part_number`
- `lumina.components.part_number` → `part_number`
- `lumina.components_bkp_dj95.part_number` → `part_number`
- `lumina.components_bkp_dj97.part_number` → `part_number`
- `lumina.components_oases971.part_number` → `part_number`
- `lumina.condition_pick_table.part_number` → `part_number`
- `lumina.consumable_batch_locations.part_number` → `part_number`
- `lumina.consumable_history.part_number` → `part_number`
- `lumina.consumable_repair_xref_to_part.part_number` → `part_number`
- `lumina.consumables_below_re_order.part_number` → `part_number`
- `lumina.cq_quote_materials.part_number` → `part_number`
- `lumina.credit_works_order_cards.part_number` → `part_number`
- `lumina.daily_loans_out.part_number` → `part_number`
- `lumina.delivery_note_item_header_1.part_number` → `part_number`
- `lumina.dmg_rpr_damage.part_number` → `part_number`
- `lumina.dmg_rpr_fitted_locations.part_number` → `part_number`
- `lumina.drn_component_mods_history.part_number` → `part_number`
- `lumina.drn_components_nsbl_history.part_number` → `part_number`
- `lumina.drn_life_limits.part_number` → `part_number`
- `lumina.drn_part_serial.part_number` → `part_number`
- `lumina.dues_register.part_number` → `part_number`
- `lumina.dummy_part_numbers.part_number` → `part_number`
- `lumina.extended_part_descriptions.part_number` → `part_number`
- `lumina.fleet_chap_part_header_1.part_number` → `part_number`
- `lumina.fleet_chap_part_header_2.part_number` → `part_number`
- `lumina.fleet_chap_part_header_3.part_number` → `part_number`
- `lumina.fleet_chapter_part_aircraft.part_number` → `part_number`
- `lumina.fleet_forecast_plans_drn.part_number` → `part_number`
- `lumina.float_history.part_number` → `part_number`
- `lumina.hazardous_materials.part_number` → `part_number`
- `lumina.ie96_historic.part_number` → `part_number`
- `lumina.inherited_acquisition_costs.part_number` → `part_number`
- `lumina.invoice_trail_entries.part_number` → `part_number`
- `lumina.latest_repair_values.part_number` → `part_number`
- `lumina.loaned_units.part_number` → `part_number`
- `lumina.long_serial_number_xref.part_number` → `part_number`
- `lumina.maint_cost_budget_materials.part_number` → `part_number`
- `lumina.maint_material_costs.part_number` → `part_number`
- `lumina.maintenance_cat_incl_parts.part_number` → `part_number`
- `lumina.material_pool_agreement_pn.part_number` → `part_number`
- `lumina.maximum_preload_pick_quantity.part_number` → `part_number`
- `lumina.monthly_loans_in.part_number` → `part_number`
- `lumina.monthly_loans_out.part_number` → `part_number`
- `lumina.n_s_extended_part_descriptions.part_number` → `part_number`
- `lumina.non_stock_parts.part_number` → `part_number`
- `lumina.non_stock_parts_bkp_oases382.part_number` → `part_number`
- `lumina.nrc_materials.part_number` → `part_number`
- `lumina.oeim_credit_warranty.part_number` → `part_number`
- `lumina.oeim_invoice_materials.part_number` → `part_number`
- `lumina.oeim_invoice_snap_part_master.part_number` → `part_number`
- `lumina.oeim_invoice_snap_pm_bkup.part_number` → `part_number`
- `lumina.oeim_invoice_snap_serl_master.part_number` → `part_number`
- `lumina.oeim_invoice_warranty.part_number` → `part_number`
- `lumina.oeim_invoice_warranty_refunds.part_number` → `part_number`
- `lumina.oeim_quote_dismissed.part_number` → `part_number`
- `lumina.order_goods_received.part_number` → `part_number`
- `lumina.order_history.part_number` → `part_number`
- `lumina.orders_to_part_number_xref.part_number` → `part_number`
- `lumina.ordr_goods_bkp.part_number` → `part_number`
- `lumina.original_purchase_values.part_number` → `part_number`
- `lumina.part_change_warning_chapters.part_number` → `part_number`
- `lumina.part_change_warnings.part_number` → `part_number`
- `lumina.part_customs_tariff_territory.part_number` → `part_number`
- `lumina.part_master.part_number` → `part_number`
- `lumina.part_master_bkp_oases382.part_number` → `part_number`
- `lumina.part_number_amendment_history.part_number` → `part_number`
- `lumina.part_number_chapters.part_number` → `part_number`
- `lumina.part_number_essentiality_codes.part_number` → `part_number`
- `lumina.part_number_marketing_codes.part_number` → `part_number`
- `lumina.part_number_order_retention.part_number` → `part_number`
- `lumina.part_number_owner_float_levels.part_number` → `part_number`
- `lumina.part_number_properties.part_number` → `part_number`
- `lumina.part_number_properties_serials.part_number` → `part_number`
- `lumina.part_number_shelf_life_details.part_number` → `part_number`
- `lumina.part_number_technical_notes.part_number` → `part_number`
- `lumina.part_number_vat_codes.part_number` → `part_number`
- `lumina.part_serial_documents.part_number` → `part_number`
- `lumina.part_serial_master_list.part_number` → `part_number`
- `lumina.part_xref_to_pick_history.part_number` → `part_number`
- `lumina.parts_customs_tariff_codes.part_number` → `part_number`
- `lumina.parts_received_without_cost.part_number` → `part_number`
- `lumina.parts_requiring_export_licence.part_number` → `part_number`
- `lumina.planners_notes_xref.part_number` → `part_number`
- `lumina.prefered_bins.part_number` → `part_number`
- `lumina.preferred_suppliers_by_part.part_number` → `part_number`
- `lumina.preorder_lines.part_number` → `part_number`
- `lumina.purchase_demand_by_part.part_number` → `part_number`
- `lumina.quotes_by_part.part_number` → `part_number`
- `lumina.quotes_for_part_by_account.part_number` → `part_number`
- `lumina.random_stock_check_parts.part_number` → `part_number`
- `lumina.removals.part_number` → `part_number`
- `lumina.requests_for_quotes_lines.part_number` → `part_number`
- `lumina.requirements.part_number` → `part_number`
- `lumina.rfc_components.part_number` → `part_number`
- `lumina.rfc_download_effectivity.part_number` → `part_number`
- `lumina.rfc_effectivity_part.part_number` → `part_number`
- `lumina.rfq_by_part_number.part_number` → `part_number`
- `lumina.rfq_history.part_number` → `part_number`
- `lumina.rotable_batch_locations.part_number` → `part_number`
- `lumina.rotable_float_values.part_number` → `part_number`
- `lumina.rotable_history.part_number` → `part_number`
- `lumina.rotables_below_re_order.part_number` → `part_number`
- `lumina.sales_history.part_number` → `part_number`
- `lumina.sales_notes_for_part.part_number` → `part_number`
- `lumina.sales_orders_by_part.part_number` → `part_number`
- `lumina.sales_prices.part_number` → `part_number`
- `lumina.sales_quotes_out_history.part_number` → `part_number`
- `lumina.sales_request_quote_detail.part_number` → `part_number`
- `lumina.sales_requests_by_part.part_number` → `part_number`
- `lumina.schedule_forecast_xref.part_number` → `part_number`
- `lumina.schedule_source.part_number` → `part_number`
- `lumina.serial_numbers_by_part.part_number` → `part_number`
- `lumina.shelf_li_dt_bkp_2020.part_number` → `part_number`
- `lumina.shelf_life_dates.part_number` → `part_number`
- `lumina.shelf_life_dates_oases6834.part_number` → `part_number`
- `lumina.shipment_demands.part_number` → `part_number`
- `lumina.shipment_item.part_number` → `part_number`
- `lumina.short_long_serials.part_number` → `part_number`
- `lumina.stock_audits.part_number` → `part_number`
- `lumina.stock_by_bin.part_number` → `part_number`
- `lumina.strip_report_header_1.part_number` → `part_number`
- `lumina.task_activity_link.part_number` → `part_number`
- `lumina.transaction_log_icarus.part_number` → `part_number`
- `lumina.transaction_log_icarus_8134.part_number` → `part_number`
- `lumina.unit_owners.part_number` → `part_number`
- `lumina.unmatched_issues_and_returns.part_number` → `part_number`
- `lumina.unsatified_service_exchanges.part_number` → `part_number`
- `lumina.uom_conversion_at_part_level.part_number` → `part_number`
- `lumina.variations_xref.part_number` → `part_number`
- `lumina.warehouse_distribution.part_number` → `part_number`
- `lumina.warehouse_replenishment_data.part_number` → `part_number`
- `lumina.warranty_claims.part_number` → `part_number`
- `lumina.warranty_exclusions.part_number` → `part_number`
- `lumina.warranty_terms.part_number` → `part_number`
- `lumina.works_order_issues_and_returns.part_number` → `part_number`
- `lumina.works_order_issues_and_rtn_bac.part_number` → `part_number`
- `lumina.works_orders.part_number` → `part_number`
- `lumina.works_orders_by_part_number.part_number` → `part_number`

### lumina.access_dim_accounts_info

**References (Outgoing):**

- `info_id` → `lumina.access_dim_accounts_info.info_id`
- `account_id` → `lumina.access_dim_accounts_info.info_id`
- `vat_code` → `lumina.amp_workcard_activations.workcard_activation_id`
- `invoice_number` → `lumina.invoice_categories.invoice_category`

**Referenced By (Incoming):**

- `lumina.access_dim_accounts_info.info_id` → `info_id`
- `lumina.access_dim_accounts_info.account_id` → `info_id`
- `lumina.access_dim_sales_info.info_id` → `info_id`
- `lumina.account_amendment_history.account_code` → `info_id`
- `lumina.account_ata_spec_2000_xref.account_code` → `info_id`
- `lumina.account_available_warehouses.account_code` → `info_id`
- `lumina.account_buying_contacts.account_code` → `info_id`
- `lumina.account_header_1.account_code` → `info_id`
- `lumina.account_header_2.account_code` → `info_id`
- `lumina.account_location_email_address.account_code` → `info_id`
- `lumina.account_location_header_1.account_code` → `info_id`
- `lumina.account_location_header_2.account_code` → `info_id`
- `lumina.account_location_header_3.account_code` → `info_id`
- `lumina.account_location_header_4.account_code` → `info_id`
- `lumina.account_location_header_5.account_code` → `info_id`
- `lumina.account_location_header_6.account_code` → `info_id`
- `lumina.account_location_header_6.account_id` → `info_id`
- `lumina.account_location_header_7.account_code` → `info_id`
- `lumina.account_location_header_8.account_code` → `info_id`
- `lumina.account_location_header_9.account_code` → `info_id`
- `lumina.account_location_notes.account_code` → `info_id`
- `lumina.account_location_properties.account_code` → `info_id`
- `lumina.account_supplier_approvals.account_code` → `info_id`
- `lumina.airway_bill_references.account_code` → `info_id`
- `lumina.contacts_xref.account_code` → `info_id`
- `lumina.cq_quotes.account_code` → `info_id`
- `lumina.credit_works_orders.account_code` → `info_id`
- `lumina.customer_contracts.account_code` → `info_id`
- `lumina.daily_loans_out.account_code` → `info_id`
- `lumina.delivery_note_header_1.account_code` → `info_id`
- `lumina.delivery_note_header_4.account_code` → `info_id`
- `lumina.ie96_historic.account_code` → `info_id`
- `lumina.invoice_lines.account_code` → `info_id`
- `lumina.invoices.account_code` → `info_id`
- `lumina.loaned_units.account_code` → `info_id`
- `lumina.maintenance_cost_quotes.account_code` → `info_id`
- `lumina.oeim_invoice_works_orders.account_code` → `info_id`
- `lumina.order_header_1.account_code` → `info_id`
- `lumina.order_numbers_by_supplier.account_code` → `info_id`
- `lumina.preferred_suppliers_by_part.account_code` → `info_id`
- `lumina.preorders.account_code` → `info_id`
- `lumina.quotes_by_part.account_code` → `info_id`
- `lumina.quotes_for_part_by_account.account_code` → `info_id`
- `lumina.repair_approval_data.account_code` → `info_id`
- `lumina.requirement_priority_sla.account_code` → `info_id`
- `lumina.rfq_history.account_code` → `info_id`
- `lumina.rfq_quote_received.account_code` → `info_id`
- `lumina.rfq_quote_received_notes.account_code` → `info_id`
- `lumina.rfq_supplier_details.account_code` → `info_id`
- `lumina.rfq_supplier_notes.account_code` → `info_id`
- `lumina.rfq_to_order_xref.account_code` → `info_id`
- `lumina.rotable_batch_locations.account_code` → `info_id`
- `lumina.rotable_history.account_code` → `info_id`
- `lumina.sales_orders.account_code` → `info_id`
- `lumina.sales_prices.account_code` → `info_id`
- `lumina.sales_quotes_out_history.account_code` → `info_id`
- `lumina.sales_request_quote_header.account_code` → `info_id`
- `lumina.shipment_order_demands.account_code` → `info_id`
- `lumina.supplier_loan_contract_rates.account_code` → `info_id`
- `lumina.third_party_account_id.account_id` → `info_id`
- `lumina.third_party_account_id.account_code` → `info_id`
- `lumina.transaction_log_icarus.account_code` → `info_id`
- `lumina.transaction_log_icarus_8134.account_code` → `info_id`
- `lumina.uf_forecast_cache.ac_code` → `info_id`
- `lumina.unit_owners.account_code` → `info_id`
- `lumina.warranty_exclusions.account_code` → `info_id`
- `lumina.warranty_terms.account_code` → `info_id`
- `lumina.work_schedule_ms_codes.account_code` → `info_id`
- `lumina.works_orders.account_code` → `info_id`
- `lumina.works_orders_by_account.account_code` → `info_id`

### lumina.access_dim_sales_info

**References (Outgoing):**

- `info_id` → `lumina.access_dim_accounts_info.info_id`
- `audit_number` → `lumina.amp_audit_notes.fleet_code`
- `vat_code` → `lumina.amp_workcard_activations.workcard_activation_id`
- `customer_code` → `lumina.customer_contract_rates.contract_id`
- `sales_order_number` → `lumina.customer_sales_order_xref.customer_sales_order_number`

### lumina.accomp_bkup

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `accomplishment_id` → `lumina.accomplishment_history.accomplishment_id`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `visit_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `report_id` → `lumina.amp_report_documents.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `paragraph_id` → `lumina.paragraph_cancels.rfc_id`

### lumina.accomp_hist_delta_1763

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `accomplishment_id` → `lumina.accomplishment_history.accomplishment_id`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `visit_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `report_id` → `lumina.amp_report_documents.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `damage_id` → `lumina.dmg_rpr_damage.damage_id`
- `document_image_id` → `lumina.document_image_source.document_image_source_id`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `paragraph_id` → `lumina.paragraph_cancels.rfc_id`

### lumina.accomp_hist_lost_sched

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `accomplishment_id` → `lumina.accomplishment_history.accomplishment_id`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `visit_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `report_id` → `lumina.amp_report_documents.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `paragraph_id` → `lumina.paragraph_cancels.rfc_id`

### lumina.accomp_hist_lost_sched_val

**References (Outgoing):**

- `accomplishment_id` → `lumina.accomplishment_history.accomplishment_id`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

### lumina.accomp_values_bkup

**References (Outgoing):**

- `accomplishment_id` → `lumina.accomplishment_history.accomplishment_id`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

### lumina.accomplishment_history

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `accomplishment_id` → `lumina.accomplishment_history.accomplishment_id`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `visit_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `report_id` → `lumina.amp_report_documents.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `damage_id` → `lumina.dmg_rpr_damage.damage_id`
- `document_image_id` → `lumina.document_image_source.document_image_source_id`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `paragraph_id` → `lumina.paragraph_cancels.rfc_id`

**Referenced By (Incoming):**

- `lumina.accomp_bkup.accomplishment_id` → `accomplishment_id`
- `lumina.accomp_hist_delta_1763.accomplishment_id` → `accomplishment_id`
- `lumina.accomp_hist_lost_sched.accomplishment_id` → `accomplishment_id`
- `lumina.accomp_hist_lost_sched_val.accomplishment_id` → `accomplishment_id`
- `lumina.accomp_values_bkup.accomplishment_id` → `accomplishment_id`
- `lumina.accomplishment_history.accomplishment_id` → `accomplishment_id`
- `lumina.accomplishment_history_values.accomplishment_id` → `accomplishment_id`
- `lumina.accs_var_corrections_bkp.accomplishment_id` → `accomplishment_id`
- `lumina.amp_revision_history.history_id` → `accomplishment_id`
- `lumina.component_movement_hist_life.history_id` → `accomplishment_id`
- `lumina.component_movement_history_ext.history_id` → `accomplishment_id`
- `lumina.component_movt_hist_ext_8661.history_id` → `accomplishment_id`
- `lumina.maint_accomplishment_costs.accomplishment_id` → `accomplishment_id`
- `lumina.mel_revision_history.history_id` → `accomplishment_id`
- `lumina.order_change_history.history_id` → `accomplishment_id`
- `lumina.rfc_accomplishment.accomplishment_code` → `accomplishment_id`
- `lumina.rfc_download_origin_codes.accomplishment_code` → `accomplishment_id`
- `lumina.rfc_header.accomplishment_code` → `accomplishment_id`
- `lumina.rp_milestone_history.history_id` → `accomplishment_id`

### lumina.accomplishment_history_values

**References (Outgoing):**

- `accomplishment_id` → `lumina.accomplishment_history.accomplishment_id`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

### lumina.account_amendment_history

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.account_ata_spec_2000_xref

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.account_available_warehouses

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `warehouse_code` → `lumina.account_available_warehouses.account_code`

**Referenced By (Incoming):**

- `lumina.account_available_warehouses.warehouse_code` → `account_code`
- `lumina.bins.warehouse_code` → `account_code`
- `lumina.condition_pick_table.warehouse_code` → `account_code`
- `lumina.random_stock_check_bins.warehouse_code` → `account_code`
- `lumina.random_stock_check_date.warehouse_code` → `account_code`
- `lumina.random_stock_check_log.warehouse_code` → `account_code`
- `lumina.random_stock_check_parts.warehouse_code` → `account_code`
- `lumina.rp_block_resource.warehouse_code` → `account_code`
- `lumina.rp_employee_calendar_addition.warehouse_code` → `account_code`
- `lumina.rp_employee_calendar_pattern.warehouse_code` → `account_code`
- `lumina.transaction_log_icarus.warehouse_code` → `account_code`
- `lumina.transaction_log_icarus_8134.warehouse_code` → `account_code`
- `lumina.user_warehouse_access.warehouse_code` → `account_code`
- `lumina.warehouse_distribution.warehouse_code` → `account_code`
- `lumina.warehouse_header_1.warehouse_code` → `account_code`
- `lumina.warehouse_header_2.warehouse_code` → `account_code`
- `lumina.warehouse_lmc_email_address.warehouse_code` → `account_code`
- `lumina.warehouse_replenishment_data.warehouse_code` → `account_code`

### lumina.account_buying_contacts

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `mobile_number` → `lumina.bkp_mobile_permissions.oases_security_token`

### lumina.account_header_1

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.account_header_2

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.account_location_email_address

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.account_location_header_1

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.account_location_header_2

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.account_location_header_3

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.account_location_header_4

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.account_location_header_5

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `currency_code` → `lumina.currency_codes.currency_code`

### lumina.account_location_header_6

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `account_id` → `lumina.access_dim_accounts_info.info_id`
- `state_code` → `lumina.release_to_service_statement.release_statement`

### lumina.account_location_header_7

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.account_location_header_8

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.account_location_header_9

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `customer_number` → `lumina.customer_contract_rates.contract_id`
- `end_use_number` → `lumina.end_use_codes.end_use_code`

### lumina.account_location_notes

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.account_location_properties

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.account_supplier_approvals

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `supplier_approval_number` → `lumina.account_supplier_approvals.account_code`

**Referenced By (Incoming):**

- `lumina.account_supplier_approvals.supplier_approval_number` → `account_code`
- `lumina.consumable_history.approval_code` → `account_code`
- `lumina.order_supplier_approval.supplier_approval_number` → `account_code`
- `lumina.work_schedule_defect_3.approval_number` → `account_code`

### lumina.account_system_header

**References (Outgoing):**

- `key_id` → `lumina.osys_key_to_reportid.osyskey`

### lumina.accounts_references

**Referenced By (Incoming):**

- `lumina.customs_status_codes.reference_number` → `accounts_reference`

### lumina.accs_var_corrections_bkp

**References (Outgoing):**

- `accomplishment_id` → `lumina.accomplishment_history.accomplishment_id`

### lumina.accum_cycles_static_data

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

**Referenced By (Incoming):**

- `lumina.drn_cycles.cycle_number` → `parent_part_number`

### lumina.add_extension_permissions

**References (Outgoing):**

- `user_id` → `lumina.dataset_locks_by_user.user_id`

**Referenced By (Incoming):**

- `lumina.bkp_mobile_permissions.permission_id` → `user_id`
- `lumina.defect_extensions.extension_id` → `user_id`
- `lumina.extensions.extension_id` → `user_id`
- `lumina.rfc_status.permission_id` → `user_id`
- `lumina.security_audit_log_header.permission_id` → `user_id`
- `lumina.security_group_perm_attribute.permission_id` → `user_id`
- `lumina.security_group_permissions.permission_id` → `user_id`
- `lumina.security_permission_def_attrib.permission_id` → `user_id`
- `lumina.security_policy_perm_attribute.permission_id` → `user_id`
- `lumina.security_policy_permissions.permission_id` → `user_id`
- `lumina.security_user_perm_attribute.permission_id` → `user_id`
- `lumina.security_user_permissions.permission_id` → `user_id`
- `lumina.security_user_permissions_bkp.permission_id` → `user_id`

### lumina.aircraft_assembles

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

**Referenced By (Incoming):**

- `lumina.accomp_bkup.aircraft_code` → `aircraft_code`
- `lumina.accomp_hist_delta_1763.aircraft_code` → `aircraft_code`
- `lumina.accomp_hist_lost_sched.aircraft_code` → `aircraft_code`
- `lumina.accomplishment_history.aircraft_code` → `aircraft_code`
- `lumina.aircraft_assembles.aircraft_code` → `aircraft_code`
- `lumina.aircraft_build.aircraft_code` → `aircraft_code`
- `lumina.aircraft_build_chapters.aircraft_code` → `aircraft_code`
- `lumina.aircraft_documents.aircraft_code` → `aircraft_code`
- `lumina.aircraft_exclusions.aircraft_code` → `aircraft_code`
- `lumina.aircraft_flight_hours_1.aircraft_code` → `aircraft_code`
- `lumina.aircraft_flight_hours_2.aircraft_code` → `aircraft_code`
- `lumina.aircraft_header_1.aircraft_code` → `aircraft_code`
- `lumina.aircraft_header_2.aircraft_code` → `aircraft_code`
- `lumina.aircraft_lease_details.aircraft_code` → `aircraft_code`
- `lumina.aircraft_leased_apu.aircraft_code` → `aircraft_code`
- `lumina.aircraft_leased_engines.aircraft_code` → `aircraft_code`
- `lumina.aircraft_leased_landing_gear.aircraft_code` → `aircraft_code`
- `lumina.aircraft_leased_propellers.aircraft_code` → `aircraft_code`
- `lumina.aircraft_life.aircraft_code` → `aircraft_code`
- `lumina.aircraft_life_dbf1065.aircraft_code` → `aircraft_code`
- `lumina.aircraft_major_checks.aircraft_code` → `aircraft_code`
- `lumina.aircraft_reg_xref.aircraft_code` → `aircraft_code`
- `lumina.aircraft_short_reg_xref.aircraft_code` → `aircraft_code`
- `lumina.aircraft_subchapter_statistics.aircraft_code` → `aircraft_code`
- `lumina.aircraft_weight.aircraft_code` → `aircraft_code`
- `lumina.aircraft_weight_7487bkp.aircraft_code` → `aircraft_code`
- `lumina.aircraft_weight_conf_xref.aircraft_code` → `aircraft_code`
- `lumina.amp_access_panel_effectivity.aircraft_code` → `aircraft_code`
- `lumina.amp_accesspanel_effectivity_jn.aircraft_code` → `aircraft_code`
- `lumina.amp_datmig_accomplishments.aircraft_code` → `aircraft_code`
- `lumina.amp_document_effectivity.aircraft_code` → `aircraft_code`
- `lumina.amp_document_effectivity_bk.aircraft_code` → `aircraft_code`
- `lumina.amp_workcard_ac_effectivity.aircraft_code` → `aircraft_code`
- `lumina.amp_workcard_ac_effectivity_jn.aircraft_code` → `aircraft_code`
- `lumina.amp_workcard_intervals.aircraft_code` → `aircraft_code`
- `lumina.assemble_thrust_life_code.aircraft_code` → `aircraft_code`
- `lumina.cfd_xref_to_tech_log.aircraft_code` → `aircraft_code`
- `lumina.completion_fleet_ata_pos.aircraft_code` → `aircraft_code`
- `lumina.completion_life_values.aircraft_code` → `aircraft_code`
- `lumina.completion_maint_mod.aircraft_code` → `aircraft_code`
- `lumina.component_movement_history_ext.aircraft_code` → `aircraft_code`
- `lumina.component_movt_hist_ext_8661.aircraft_code` → `aircraft_code`
- `lumina.components.aircraft_code` → `aircraft_code`
- `lumina.components_bkp_dj95.aircraft_code` → `aircraft_code`
- `lumina.components_bkp_dj97.aircraft_code` → `aircraft_code`
- `lumina.components_oases971.aircraft_code` → `aircraft_code`
- `lumina.cq_quotes.aircraft_code` → `aircraft_code`
- `lumina.crs_signature_text.aircraft_code` → `aircraft_code`
- `lumina.customer_contracts.aircraft_code` → `aircraft_code`
- `lumina.deferred_defect_xref_to_cfd_no.aircraft_code` → `aircraft_code`
- `lumina.dmg_rpr_damage_numbering.aircraft_code` → `aircraft_code`
- `lumina.dmg_rpr_doc_effectivity.aircraft_code` → `aircraft_code`
- `lumina.dmg_rpr_document_order.aircraft_code` → `aircraft_code`
- `lumina.dmg_rpr_fitted_locations.aircraft_code` → `aircraft_code`
- `lumina.dmg_rpr_location.aircraft_code` → `aircraft_code`
- `lumina.drn_cycles.aircraft_code` → `aircraft_code`
- `lumina.drn_fleet_ata.aircraft_code` → `aircraft_code`
- `lumina.drn_life_limits.aircraft_code` → `aircraft_code`
- `lumina.drn_maint_mod.aircraft_code` → `aircraft_code`
- `lumina.drn_maint_mod_notes.aircraft_code` → `aircraft_code`
- `lumina.drn_maintenance_history.aircraft_code` → `aircraft_code`
- `lumina.drn_maintenance_history_notes.aircraft_code` → `aircraft_code`
- `lumina.drn_mod_desc_order_hist.aircraft_code` → `aircraft_code`
- `lumina.drn_modification_history.aircraft_code` → `aircraft_code`
- `lumina.drn_modification_history_notes.aircraft_code` → `aircraft_code`
- `lumina.fleet_chapter_part_aircraft.aircraft_code` → `aircraft_code`
- `lumina.fleet_forecast_plans.aircraft_code` → `aircraft_code`
- `lumina.flown_sectors.aircraft_code` → `aircraft_code`
- `lumina.flown_sectors_bkp.aircraft_code` → `aircraft_code`
- `lumina.flown_sectors_con_680.aircraft_code` → `aircraft_code`
- `lumina.flown_sectors_delta1817.aircraft_code` → `aircraft_code`
- `lumina.forecast_cache.aircraft_code` → `aircraft_code`
- `lumina.forecast_cache_revisions.aircraft_code` → `aircraft_code`
- `lumina.future_flights.aircraft_code` → `aircraft_code`
- `lumina.le80_defect_temp.aircraft_code` → `aircraft_code`
- `lumina.life_code_entry.aircraft_code` → `aircraft_code`
- `lumina.life_code_entry_backup.aircraft_code` → `aircraft_code`
- `lumina.life_code_entry_dbf1065.aircraft_code` → `aircraft_code`
- `lumina.lmc_base_data_options.aircraft_code` → `aircraft_code`
- `lumina.maint_associated_cost_aircraft.aircraft_code` → `aircraft_code`
- `lumina.maint_cost_budget_adsb.aircraft_code` → `aircraft_code`
- `lumina.maint_cost_budget_aircraft.aircraft_code` → `aircraft_code`
- `lumina.maint_cost_budget_cfds.aircraft_code` → `aircraft_code`
- `lumina.maint_cost_budget_defects.aircraft_code` → `aircraft_code`
- `lumina.maint_cost_budget_packages.aircraft_code` → `aircraft_code`
- `lumina.maint_cost_budget_visits.aircraft_code` → `aircraft_code`
- `lumina.maint_cost_budget_workcards.aircraft_code` → `aircraft_code`
- `lumina.material_pool_agreement_ac.aircraft_code` → `aircraft_code`
- `lumina.measurement_alerts_aircraft.aircraft_code` → `aircraft_code`
- `lumina.no_narrative_default.aircraft_code` → `aircraft_code`
- `lumina.pirep_index_data.aircraft_code` → `aircraft_code`
- `lumina.planners_notes_xref.aircraft_code` → `aircraft_code`
- `lumina.rd_xref_to_tech_logs.aircraft_code` → `aircraft_code`
- `lumina.removals.aircraft_code` → `aircraft_code`
- `lumina.repetitive_defect_header_1.aircraft_code` → `aircraft_code`
- `lumina.rfc_aircraft.aircraft_code` → `aircraft_code`
- `lumina.sample_fleets.aircraft_code` → `aircraft_code`
- `lumina.sample_fleets_jn.aircraft_code` → `aircraft_code`
- `lumina.schedule_forecast_xref.aircraft_code` → `aircraft_code`
- `lumina.schedule_source.aircraft_code` → `aircraft_code`
- `lumina.security_user_effectivity.aircraft_code` → `aircraft_code`
- `lumina.sub_fleets.aircraft_code` → `aircraft_code`
- `lumina.sub_fleets_jn.aircraft_code` → `aircraft_code`
- `lumina.task_activity_link.aircraft_code` → `aircraft_code`
- `lumina.tech_log_1.aircraft_code` → `aircraft_code`
- `lumina.tech_log_2.aircraft_code` → `aircraft_code`
- `lumina.tech_log_3.aircraft_code` → `aircraft_code`
- `lumina.tech_log_defect_text.aircraft_code` → `aircraft_code`
- `lumina.tech_log_nrc_xref.aircraft_code` → `aircraft_code`
- `lumina.tech_log_rectification_text.aircraft_code` → `aircraft_code`
- `lumina.tech_log_workcard_link.aircraft_code` → `aircraft_code`
- `lumina.variations.aircraft_code` → `aircraft_code`
- `lumina.variations_xref.aircraft_code` → `aircraft_code`
- `lumina.wcr_boeing_tb_revision.aircraft_code` → `aircraft_code`
- `lumina.wcr_msg_log.aircraft_code` → `aircraft_code`
- `lumina.wcr_temp_base1.aircraft_code` → `aircraft_code`
- `lumina.weight_and_balance_documents.aircraft_code` → `aircraft_code`
- `lumina.wo_auto_amended_contacts.aircraft_code` → `aircraft_code`
- `lumina.workcard_documents_filter.aircraft_code` → `aircraft_code`
- `lumina.workcard_form_number.aircraft_code` → `aircraft_code`

### lumina.aircraft_build

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.aircraft_build_chapters

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.aircraft_documents

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `aircraft_document_id` → `lumina.aircraft_documents.aircraft_document_id`
- `document_image_id` → `lumina.document_image_source.document_image_source_id`

**Referenced By (Incoming):**

- `lumina.aircraft_documents.aircraft_document_id` → `aircraft_document_id`
- `lumina.amp_document_effectivity.document_id` → `aircraft_document_id`
- `lumina.amp_document_effectivity_bk.document_id` → `aircraft_document_id`
- `lumina.amp_documents_by_workcard.document_id` → `aircraft_document_id`
- `lumina.amp_documents_by_workcard_bk.document_id` → `aircraft_document_id`
- `lumina.amp_manufacturers_documents.document_id` → `aircraft_document_id`
- `lumina.document_classes.document_id` → `aircraft_document_id`
- `lumina.esign_off_nrc.document_id` → `aircraft_document_id`
- `lumina.manufacturers_work_documents.document_id` → `aircraft_document_id`
- `lumina.nrc_documents.document_id` → `aircraft_document_id`
- `lumina.shipment_documents.document_id` → `aircraft_document_id`
- `lumina.wcr_temp_base1.document_id` → `aircraft_document_id`
- `lumina.weight_and_balance_documents.document_id` → `aircraft_document_id`

### lumina.aircraft_exclusions

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `aircraft_exclusion_id` → `lumina.aircraft_exclusions.aircraft_exclusion_id`

**Referenced By (Incoming):**

- `lumina.aircraft_exclusions.aircraft_exclusion_id` → `aircraft_exclusion_id`
- `lumina.warranty_exclusions.exclusion_id` → `aircraft_exclusion_id`

### lumina.aircraft_flight_hours_1

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

**Referenced By (Incoming):**

- `lumina.flown_sectors.flight_number` → `aircraft_code`
- `lumina.flown_sectors_bkp.flight_number` → `aircraft_code`
- `lumina.flown_sectors_con_680.flight_number` → `aircraft_code`
- `lumina.flown_sectors_delta1817.flight_number` → `aircraft_code`
- `lumina.work_schedule_defect_3.flight_number` → `aircraft_code`

### lumina.aircraft_flight_hours_2

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.aircraft_header_1

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `line_number` → `lumina.invoice_line_notes.invoice_number`

### lumina.aircraft_header_2

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `effectivity_code` → `lumina.amp_access_panel_effectivity.ap_ac_effectivity_id`

### lumina.aircraft_lease_details

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

**Referenced By (Incoming):**

- `lumina.oeim_transaction_log_details.detail_number` → `aircraft_code`

### lumina.aircraft_leased_apu

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.aircraft_leased_engines

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.aircraft_leased_landing_gear

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.aircraft_leased_propellers

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.aircraft_life

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

**Referenced By (Incoming):**

- `lumina.assemble_thrust_life_code.life_code` → `aircraft_code`
- `lumina.life_code_levels.life_code` → `aircraft_code`
- `lumina.life_codes.life_code` → `aircraft_code`
- `lumina.measurement_alerts_aircraft.life_code` → `aircraft_code`
- `lumina.measurement_alerts_fleet.life_code` → `aircraft_code`

### lumina.aircraft_life_dbf1065

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

### lumina.aircraft_major_checks

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `visit_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.aircraft_reg_xref

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.aircraft_short_reg_xref

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.aircraft_statistics

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`

### lumina.aircraft_subchapter_statistics

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.aircraft_types

**Referenced By (Incoming):**

- `lumina.rp_calendar_addition_type.type_id` → `aircraft_type`
- `lumina.rp_dependencies.type_id` → `aircraft_type`
- `lumina.rp_employee_calendar_addition.type_id` → `aircraft_type`

### lumina.aircraft_weight

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.aircraft_weight_7487bkp

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.aircraft_weight_conf

**References (Outgoing):**

- `conf_id` → `lumina.aircraft_weight_conf.conf_id`

**Referenced By (Incoming):**

- `lumina.aircraft_weight_conf.conf_id` → `conf_id`
- `lumina.aircraft_weight_conf_entries.conf_id` → `conf_id`
- `lumina.aircraft_weight_conf_xref.conf_id` → `conf_id`

### lumina.aircraft_weight_conf_entries

**References (Outgoing):**

- `conf_id` → `lumina.aircraft_weight_conf.conf_id`

### lumina.aircraft_weight_conf_xref

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `conf_id` → `lumina.aircraft_weight_conf.conf_id`

### lumina.airport_codes

**Referenced By (Incoming):**

- `lumina.warehouse_header_2.airport_id` → `icao_code`

### lumina.airway_bill_references

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `order_number` → `lumina.batch_orders.batch_number`
- `delivery_note_number` → `lumina.delivery_note_extended_remarks.delivery_note_number`
- `shipment_id` → `lumina.shipment.shipment_id`

**Referenced By (Incoming):**

- `lumina.batches_by_airway_bill.airway_bill_number` → `awb_id`
- `lumina.order_line_additional_info.airway_bill_number` → `awb_id`

### lumina.alert_colors

**Referenced By (Incoming):**

- `lumina.forecast_cache.alert_number` → `alert_type_id`
- `lumina.planners_notes_xref.alert_number` → `alert_type_id`
- `lumina.rd_xref_to_tech_logs.alert_number` → `alert_type_id`
- `lumina.rdi_history.alert_number` → `alert_type_id`
- `lumina.repetitive_defect_header_1.alert_number` → `alert_type_id`
- `lumina.repetitive_defect_header_2.alert_number` → `alert_type_id`
- `lumina.repetitive_defect_narrative.alert_number` → `alert_type_id`
- `lumina.repetitive_defect_tech_logs.alert_number` → `alert_type_id`
- `lumina.requirements.alert_number` → `alert_type_id`
- `lumina.tech_log_2.alert_number` → `alert_type_id`
- `lumina.uf_forecast_cache.alert_number` → `alert_type_id`

### lumina.alternate_parts

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `alternate_part_number` → `lumina.alternate_parts.part_number`

**Referenced By (Incoming):**

- `lumina.alternate_parts.alternate_part_number` → `part_number`
- `lumina.fleet_chap_part_header_1.alternate_part_number` → `part_number`
- `lumina.pick_hist_7890_bkp.alternate_part_number` → `part_number`
- `lumina.pick_history.alternate_part_number` → `part_number`
- `lumina.rfc_aircraft.na_id` → `part_number`
- `lumina.rfc_components.na_id` → `part_number`
- `lumina.rfc_na_notes.na_id` → `part_number`
- `lumina.rfc_na_notes.na_code` → `part_number`
- `lumina.uf_forecast_cache.na_id` → `part_number`

### lumina.amp_acc_panel_desc_osd_33348

**References (Outgoing):**

- `access_panel_code` → `lumina.amp_access_panel_desc_hdr.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.amp_access_panel_desc_hdr

**References (Outgoing):**

- `revision_id` → `lumina.amp_revision_history.history_id`

**Referenced By (Incoming):**

- `lumina.amp_acc_panel_desc_osd_33348.access_panel_code` → `fleet`
- `lumina.amp_access_panel_descriptions.access_panel_code` → `fleet`
- `lumina.amp_access_panel_effectivity.access_panel_code` → `fleet`
- `lumina.amp_accesspanel_effectivity_jn.access_panel_code` → `fleet`
- `lumina.cq_quote_nrc_access_panels.access_panel_code` → `fleet`
- `lumina.nrc_access_panels.access_panel_code` → `fleet`

### lumina.amp_access_panel_descriptions

**References (Outgoing):**

- `access_panel_code` → `lumina.amp_access_panel_desc_hdr.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.amp_access_panel_effectivity

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `access_panel_code` → `lumina.amp_access_panel_desc_hdr.fleet`
- `fleet_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `sub_fleet_id` → `lumina.sub_fleet_header.sub_fleet_id`

**Referenced By (Incoming):**

- `lumina.aircraft_header_2.effectivity_code` → `ap_ac_effectivity_id`

### lumina.amp_access_panel_notes

**References (Outgoing):**

- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.amp_access_panels_by_workcard

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `sequence_number` → `lumina.nrc_high_sequence_control.key_id`

**Referenced By (Incoming):**

- `lumina.aircraft_statistics.workcard_number` → `fleet`
- `lumina.amp_access_panels_by_workcard.workcard_number` → `fleet`
- `lumina.amp_audit_notes.workcard_number` → `fleet`
- `lumina.amp_comments.workcard_number` → `fleet`
- `lumina.amp_document_effectivity.workcard_id` → `fleet`
- `lumina.amp_document_effectivity_bk.workcard_id` → `fleet`
- `lumina.amp_documents_by_workcard.workcard_number` → `fleet`
- `lumina.amp_documents_by_workcard.workcard_id` → `fleet`
- `lumina.amp_documents_by_workcard_bk.workcard_number` → `fleet`
- `lumina.amp_documents_by_workcard_bk.workcard_id` → `fleet`
- `lumina.amp_material_effectivity.workcard_id` → `fleet`
- `lumina.amp_material_effectivity_jn.workcard_id` → `fleet`
- `lumina.amp_materials_required_by_wc.workcard_number` → `fleet`
- `lumina.amp_packages_by_workcard.workcard_number` → `fleet`
- `lumina.amp_planning_notes.workcard_number` → `fleet`
- `lumina.amp_wc_aircraft_exclusions.workcard_number` → `fleet`
- `lumina.amp_wcard_extended_desc_41.workcard_number` → `fleet`
- `lumina.amp_workcard_ac_effectivity.workcard_id` → `fleet`
- `lumina.amp_workcard_ac_effectivity_jn.workcard_id` → `fleet`
- `lumina.amp_workcard_accomplishments.workcard_number` → `fleet`
- `lumina.amp_workcard_activations.workcard_number` → `fleet`
- `lumina.amp_workcard_call_workcard.workcard_number` → `fleet`
- `lumina.amp_workcard_cancellations.workcard_number` → `fleet`
- `lumina.amp_workcard_extended_desc.workcard_number` → `fleet`
- `lumina.amp_workcard_header_1.workcard_number` → `fleet`
- `lumina.amp_workcard_header_1.workcard_id` → `fleet`
- `lumina.amp_workcard_header_1_43216.workcard_number` → `fleet`
- `lumina.amp_workcard_header_1_43216.workcard_id` → `fleet`
- `lumina.amp_workcard_header_2.workcard_number` → `fleet`
- `lumina.amp_workcard_header_4.workcard_number` → `fleet`
- `lumina.amp_workcard_header_5.workcard_number` → `fleet`
- `lumina.amp_workcard_header_properties.workcard_number` → `fleet`
- `lumina.amp_workcard_intervals.workcard_id` → `fleet`
- `lumina.amp_workcard_lcl_applicability.workcard_number` → `fleet`
- `lumina.amp_workcard_narrative.workcard_number` → `fleet`
- `lumina.amp_workcard_not_with_workcard.workcard_number` → `fleet`
- `lumina.amp_workcard_previously_acc_by.workcard_number` → `fleet`
- `lumina.amp_workcard_publications.workcard_id` → `fleet`
- `lumina.amp_workcards_by_package.workcard_number` → `fleet`
- `lumina.amp_workcards_by_section.workcard_number` → `fleet`
- `lumina.bar_codes.workcard_number` → `fleet`
- `lumina.cq_quote_cards.workcard_number` → `fleet`
- `lumina.cq_quote_materials.workcard_number` → `fleet`
- `lumina.dmg_rpr_inspections.workcard_number` → `fleet`
- `lumina.dmg_rpr_interim_repairs.workcard_number` → `fleet`
- `lumina.dmg_rpr_permanent_repairs.workcard_number` → `fleet`
- `lumina.dmg_rpr_time_limited_repairs.workcard_number` → `fleet`
- `lumina.engineering_support_history.workcard_number` → `fleet`
- `lumina.fleet_statistics.workcard_number` → `fleet`
- `lumina.forecast_cache.workcard_code` → `fleet`
- `lumina.forecast_variation_details.workcard_number` → `fleet`
- `lumina.lmc_base_data_reported_wc.workcard_number` → `fleet`
- `lumina.maint_card_pref_cost_cats.workcard_number` → `fleet`
- `lumina.maint_cost_budget_adsb.workcard_id` → `fleet`
- `lumina.maint_cost_budget_adsb.workcard_number` → `fleet`
- `lumina.maint_cost_budget_workcards.workcard_id` → `fleet`
- `lumina.maint_cost_budget_workcards.workcard_number` → `fleet`
- `lumina.nrc_defect_notes.workcard_number` → `fleet`
- `lumina.nrc_print_history.workcard_number` → `fleet`
- `lumina.nrc_rectification_notes.workcard_number` → `fleet`
- `lumina.nrc_requirements_actions.workcard_number` → `fleet`
- `lumina.nrc_status_history.workcard_number` → `fleet`
- `lumina.nrc_xref_to_scheduled_workcard.workcard_number` → `fleet`
- `lumina.oeim_credit_warranty.card_number` → `fleet`
- `lumina.oeim_invoice_cards.card_number` → `fleet`
- `lumina.oeim_invoice_inclusive_hrs.card_number` → `fleet`
- `lumina.oeim_invoice_materials.card_number` → `fleet`
- `lumina.oeim_invoice_warranty.card_number` → `fleet`
- `lumina.oeim_invoice_warranty_refunds.card_number` → `fleet`
- `lumina.oeim_quote_dismissed.workcard_number` → `fleet`
- `lumina.rfc_frequency_phases.workcard_number` → `fleet`
- `lumina.rp_dependencies.workcard_number` → `fleet`
- `lumina.rp_employee_allocation.workcard_number` → `fleet`
- `lumina.rp_wo_base_workcard_plan.workcard_number` → `fleet`
- `lumina.rp_wo_workcard_plan.workcard_number` → `fleet`
- `lumina.schedule_forecast_xref.workcard_number` → `fleet`
- `lumina.schedule_forecast_xref.workcard_id` → `fleet`
- `lumina.sfdc_component_changes.workcard_number` → `fleet`
- `lumina.structural_damage.workcard_number` → `fleet`
- `lumina.task_activity_link.workcard_number` → `fleet`
- `lumina.tech_log_2.workcard_number` → `fleet`
- `lumina.tech_log_workcard_link.workcard_number` → `fleet`
- `lumina.uf_forecast_cache.workcard_id` → `fleet`
- `lumina.wcr_temp_access_panels.workcard_number` → `fleet`
- `lumina.wcr_temp_base1.workcard_number` → `fleet`
- `lumina.wcr_temp_base1.workcard_id` → `fleet`
- `lumina.wcr_temp_narratives.workcard_number` → `fleet`
- `lumina.work_sch_def_2_lg318.workcard_number` → `fleet`
- `lumina.work_schedule_defect_1.workcard_number` → `fleet`
- `lumina.work_schedule_defect_2.workcard_number` → `fleet`
- `lumina.work_schedule_defect_3.workcard_number` → `fleet`
- `lumina.work_schedule_defect_4.workcard_number` → `fleet`
- `lumina.work_schedule_workcards.workcard_number` → `fleet`
- `lumina.workcard_accomplishments.workcard_number` → `fleet`
- `lumina.workcard_activations.workcard_number` → `fleet`
- `lumina.workcard_cancellations.workcard_number` → `fleet`
- `lumina.workcard_forms.workcard_number` → `fleet`

### lumina.amp_accesspanel_effectivity_jn

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `access_panel_code` → `lumina.amp_access_panel_desc_hdr.fleet`
- `fleet_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `sub_fleet_id` → `lumina.sub_fleet_header.sub_fleet_id`

### lumina.amp_audit_notes

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `fleet_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `visit_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

**Referenced By (Incoming):**

- `lumina.access_dim_sales_info.audit_number` → `fleet_code`
- `lumina.audit_trail.audit_id` → `fleet_code`
- `lumina.audit_trail_ids.audit_id` → `fleet_code`
- `lumina.audit_trail_meta_data.audit_id` → `fleet_code`

### lumina.amp_comments

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `fleet_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `visit_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.amp_component_intervals

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `component_interval_id` → `lumina.amp_component_intervals.component_interval_id`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `component_life_limit_id` → `lumina.component_life_limits.component_life_limit_id`

**Referenced By (Incoming):**

- `lumina.amp_component_intervals.component_interval_id` → `component_interval_id`
- `lumina.amp_component_intervals_limits.component_interval_id` → `component_interval_id`
- `lumina.amp_component_intervals_stages.component_interval_id` → `component_interval_id`
- `lumina.amp_component_reset_on_compl.component_interval_id` → `component_interval_id`
- `lumina.uf_forecast_cache.interval_id` → `component_interval_id`

### lumina.amp_component_intervals_limits

**References (Outgoing):**

- `component_interval_id` → `lumina.amp_component_intervals.component_interval_id`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_stage_limits.limit_id` → `component_interval_id`

### lumina.amp_component_intervals_stages

**References (Outgoing):**

- `component_interval_id` → `lumina.amp_component_intervals.component_interval_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_stage_limits.stage_id` → `component_interval_id`
- `lumina.dmg_rpr_stages.stage_id` → `component_interval_id`
- `lumina.rfc_evaluation_stages.stage_code` → `component_interval_id`
- `lumina.rfc_status.stage_code` → `component_interval_id`

### lumina.amp_component_reset_on_compl

**References (Outgoing):**

- `component_interval_id` → `lumina.amp_component_intervals.component_interval_id`
- `component_life_limit_id` → `lumina.component_life_limits.component_life_limit_id`

### lumina.amp_data_migration_log

**References (Outgoing):**

- `log_number` → `lumina.amp_data_migration_log.log_number`

**Referenced By (Incoming):**

- `lumina.amp_data_migration_log.log_number` → `log_number`
- `lumina.oases_message_log.log_number` → `log_number`
- `lumina.oeim_transaction_log_details.log_number` → `log_number`
- `lumina.oeim_transaction_log_header.log_number` → `log_number`
- `lumina.rfc_print_history_log.log_id` → `log_number`
- `lumina.rfc_transaction_log.log_id` → `log_number`
- `lumina.transaction_log_lasers.log_number` → `log_number`
- `lumina.transaction_log_mavis.log_number` → `log_number`
- `lumina.transaction_log_trecs.log_number` → `log_number`

### lumina.amp_datmig_accomplishments

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `visit_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.amp_datmig_comp_task_lookup

**References (Outgoing):**

- `package_code` → `lumina.amp_package_notes.fleet`

**Referenced By (Incoming):**

- `lumina.employee_presence_log.task_number` → `fleet`
- `lumina.oeim_invoice_snap_sfdc_book.task_number` → `fleet`
- `lumina.sfdc_bookings.task_number` → `fleet`
- `lumina.sfdc_deleted_bookings.task_number` → `fleet`
- `lumina.sfdc_open_bookings.task_number` → `fleet`
- `lumina.tool_check_out_in.task_number` → `fleet`
- `lumina.tool_check_out_in_duplicates.task_number` → `fleet`
- `lumina.wcr_temp_access_panels.task_number` → `fleet`
- `lumina.wcr_temp_narratives.task_number` → `fleet`

### lumina.amp_datmig_fleet_visit_pack

**Referenced By (Incoming):**

- `lumina.accomp_bkup.visit_code` → `fleet`
- `lumina.accomp_hist_delta_1763.visit_code` → `fleet`
- `lumina.accomp_hist_lost_sched.visit_code` → `fleet`
- `lumina.accomplishment_history.visit_code` → `fleet`
- `lumina.aircraft_major_checks.visit_code` → `fleet`
- `lumina.amp_access_panel_effectivity.fleet_code` → `fleet`
- `lumina.amp_accesspanel_effectivity_jn.fleet_code` → `fleet`
- `lumina.amp_audit_notes.fleet_code` → `fleet`
- `lumina.amp_audit_notes.visit_code` → `fleet`
- `lumina.amp_comments.fleet_code` → `fleet`
- `lumina.amp_comments.visit_code` → `fleet`
- `lumina.amp_datmig_accomplishments.visit_code` → `fleet`
- `lumina.amp_packages_by_visit.visit_code` → `fleet`
- `lumina.amp_planning_notes.fleet_code` → `fleet`
- `lumina.amp_planning_notes.visit_code` → `fleet`
- `lumina.amp_visit_notes.visit_code` → `fleet`
- `lumina.amp_visits.visit_code` → `fleet`
- `lumina.assemble_thrust_life_code.fleet_code` → `fleet`
- `lumina.dmg_rpr_doc_effectivity.fleet_code` → `fleet`
- `lumina.dmg_rpr_document_order.fleet_code` → `fleet`
- `lumina.fleet_assembles.fleet_code` → `fleet`
- `lumina.forecast_cache.visit_code` → `fleet`
- `lumina.forecast_cache_revisions.fleet_code` → `fleet`
- `lumina.maint_cost_budget_visits.visit_code` → `fleet`
- `lumina.planners_notes_xref.visit_code` → `fleet`
- `lumina.sample_fleets.fleet_code` → `fleet`
- `lumina.sample_fleets_jn.fleet_code` → `fleet`
- `lumina.schedule_forecast_xref.visit_code` → `fleet`
- `lumina.sub_fleet_header.fleet_code` → `fleet`
- `lumina.task_activity_link.visit_code` → `fleet`
- `lumina.uf_forecast_cache.fleet_code` → `fleet`
- `lumina.uf_forecast_cache.visit_code` → `fleet`
- `lumina.variations_xref.visit_code` → `fleet`

### lumina.amp_datmig_llp

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.amp_document_effectivity

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `document_id` → `lumina.aircraft_documents.aircraft_document_id`
- `workcard_id` → `lumina.amp_access_panels_by_workcard.fleet`

### lumina.amp_document_effectivity_bk

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `document_id` → `lumina.aircraft_documents.aircraft_document_id`
- `workcard_id` → `lumina.amp_access_panels_by_workcard.fleet`

### lumina.amp_documents_by_workcard

**References (Outgoing):**

- `document_id` → `lumina.aircraft_documents.aircraft_document_id`
- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `workcard_id` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `sequence_number` → `lumina.nrc_high_sequence_control.key_id`

### lumina.amp_documents_by_workcard_bk

**References (Outgoing):**

- `document_id` → `lumina.aircraft_documents.aircraft_document_id`
- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `workcard_id` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `sequence_number` → `lumina.nrc_high_sequence_control.key_id`

### lumina.amp_manufacturers_documents

**References (Outgoing):**

- `document_id` → `lumina.aircraft_documents.aircraft_document_id`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.amp_material_effectivity

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `workcard_id` → `lumina.amp_access_panels_by_workcard.fleet`
- `sub_fleet_id` → `lumina.sub_fleet_header.sub_fleet_id`

**Referenced By (Incoming):**

- `lumina.maint_cost_budget_materials.material_id` → `workcard_material_id`

### lumina.amp_material_effectivity_jn

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `workcard_id` → `lumina.amp_access_panels_by_workcard.fleet`
- `sub_fleet_id` → `lumina.sub_fleet_header.sub_fleet_id`

### lumina.amp_materials_required_by_wc

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `sequence_number` → `lumina.nrc_high_sequence_control.key_id`

### lumina.amp_package_notes

**References (Outgoing):**

- `package_code` → `lumina.amp_package_notes.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

**Referenced By (Incoming):**

- `lumina.accomp_bkup.package_code` → `fleet`
- `lumina.accomp_hist_delta_1763.package_code` → `fleet`
- `lumina.accomp_hist_lost_sched.package_code` → `fleet`
- `lumina.accomplishment_history.package_code` → `fleet`
- `lumina.aircraft_major_checks.package_code` → `fleet`
- `lumina.amp_audit_notes.package_code` → `fleet`
- `lumina.amp_comments.package_code` → `fleet`
- `lumina.amp_datmig_accomplishments.package_code` → `fleet`
- `lumina.amp_datmig_comp_task_lookup.package_code` → `fleet`
- `lumina.amp_package_notes.package_code` → `fleet`
- `lumina.amp_packages.package_code` → `fleet`
- `lumina.amp_packages_by_visit.package_code` → `fleet`
- `lumina.amp_planning_notes.package_code` → `fleet`
- `lumina.amp_workcards_by_package.package_code` → `fleet`
- `lumina.cq_quote_cards.package_code` → `fleet`
- `lumina.cq_quote_packages.package_code` → `fleet`
- `lumina.forecast_cache.package_code` → `fleet`
- `lumina.maint_cost_budget_packages.package_code` → `fleet`
- `lumina.maint_pack_pref_cost_cats.package_code` → `fleet`
- `lumina.oeim_invoice_cards.package_code` → `fleet`
- `lumina.oeim_invoice_materials.package_code` → `fleet`
- `lumina.oeim_invoice_packages.package_code` → `fleet`
- `lumina.oeim_invoice_warranty.package_code` → `fleet`
- `lumina.oeim_quote_dismissed.package_code` → `fleet`
- `lumina.package.package_id` → `fleet`
- `lumina.package_items.package_id` → `fleet`
- `lumina.planners_notes_xref.package_code` → `fleet`
- `lumina.schedule_forecast_xref.package_code` → `fleet`
- `lumina.task_activity_link.package_code` → `fleet`
- `lumina.uf_forecast_cache.package_code` → `fleet`
- `lumina.variations_xref.package_code` → `fleet`

### lumina.amp_packages

**References (Outgoing):**

- `package_code` → `lumina.amp_package_notes.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

**Referenced By (Incoming):**

- `lumina.fleet_forecast_plans_amp.package_codes` → `fleet`

### lumina.amp_packages_by_visit

**References (Outgoing):**

- `visit_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.amp_packages_by_workcard

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `sequence_number` → `lumina.nrc_high_sequence_control.key_id`

### lumina.amp_planning_notes

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `fleet_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `visit_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

**Referenced By (Incoming):**

- `lumina.fleet_forecast_plans.plan_id` → `fleet_code`
- `lumina.fleet_forecast_plans_amp.plan_id` → `fleet_code`
- `lumina.fleet_forecast_plans_drn.plan_id` → `fleet_code`
- `lumina.fleet_forecast_plans_rfc.plan_id` → `fleet_code`

### lumina.amp_report_documents

**References (Outgoing):**

- `revision_id` → `lumina.amp_revision_history.history_id`
- `document_image_id` → `lumina.document_image_source.document_image_source_id`

**Referenced By (Incoming):**

- `lumina.accomp_bkup.report_id` → `fleet`
- `lumina.accomp_hist_delta_1763.report_id` → `fleet`
- `lumina.accomp_hist_lost_sched.report_id` → `fleet`
- `lumina.accomplishment_history.report_id` → `fleet`
- `lumina.completion_maint_mod.report_id` → `fleet`
- `lumina.component_movement_history_ext.report_id` → `fleet`
- `lumina.component_movt_hist_ext_8661.report_id` → `fleet`
- `lumina.delays.report_id` → `fleet`
- `lumina.drn_component_mods_history.report_id` → `fleet`
- `lumina.drn_maintenance_history.report_id` → `fleet`
- `lumina.drn_modification_history.report_id` → `fleet`
- `lumina.flown_sectors.report_id` → `fleet`
- `lumina.flown_sectors_bkp.report_id` → `fleet`
- `lumina.flown_sectors_con_680.report_id` → `fleet`
- `lumina.flown_sectors_delta1817.report_id` → `fleet`
- `lumina.life_code_entry.report_id` → `fleet`
- `lumina.life_code_entry_backup.report_id` → `fleet`
- `lumina.life_code_entry_dbf1065.report_id` → `fleet`
- `lumina.netline_import_index.report_id` → `fleet`
- `lumina.oases_reports.report_id` → `fleet`
- `lumina.osys_key_to_reportid.report_id` → `fleet`
- `lumina.pdc_import_index.report_id` → `fleet`
- `lumina.sabre_flight_map.report_id` → `fleet`
- `lumina.tech_log_3.report_id` → `fleet`
- `lumina.tech_log_documents.report_id` → `fleet`

### lumina.amp_revision_history

**References (Outgoing):**

- `history_id` → `lumina.accomplishment_history.accomplishment_id`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `user_id` → `lumina.dataset_locks_by_user.user_id`

**Referenced By (Incoming):**

- `lumina.accomp_bkup.revision_id` → `history_id`
- `lumina.accomp_hist_delta_1763.revision_id` → `history_id`
- `lumina.accomp_hist_lost_sched.revision_id` → `history_id`
- `lumina.accomplishment_history.revision_id` → `history_id`
- `lumina.amp_acc_panel_desc_osd_33348.revision_id` → `history_id`
- `lumina.amp_access_panel_desc_hdr.revision_id` → `history_id`
- `lumina.amp_access_panel_descriptions.revision_id` → `history_id`
- `lumina.amp_access_panel_effectivity.revision_id` → `history_id`
- `lumina.amp_access_panel_notes.revision_id` → `history_id`
- `lumina.amp_access_panels_by_workcard.revision_id` → `history_id`
- `lumina.amp_accesspanel_effectivity_jn.revision_id` → `history_id`
- `lumina.amp_audit_notes.revision_id` → `history_id`
- `lumina.amp_comments.revision_id` → `history_id`
- `lumina.amp_component_intervals.revision_id` → `history_id`
- `lumina.amp_documents_by_workcard.revision_id` → `history_id`
- `lumina.amp_documents_by_workcard_bk.revision_id` → `history_id`
- `lumina.amp_manufacturers_documents.revision_id` → `history_id`
- `lumina.amp_materials_required_by_wc.revision_id` → `history_id`
- `lumina.amp_package_notes.revision_id` → `history_id`
- `lumina.amp_packages.revision_id` → `history_id`
- `lumina.amp_packages_by_visit.revision_id` → `history_id`
- `lumina.amp_packages_by_workcard.revision_id` → `history_id`
- `lumina.amp_planning_notes.revision_id` → `history_id`
- `lumina.amp_report_documents.revision_id` → `history_id`
- `lumina.amp_revision_history.revision_id` → `history_id`
- `lumina.amp_revisions.revision_id` → `history_id`
- `lumina.amp_visit_notes.revision_id` → `history_id`
- `lumina.amp_visits.revision_id` → `history_id`
- `lumina.amp_wc_aircraft_exclusions.revision_id` → `history_id`
- `lumina.amp_wcard_extended_desc_41.revision_id` → `history_id`
- `lumina.amp_workcard_accomplishments.revision_id` → `history_id`
- `lumina.amp_workcard_activations.revision_id` → `history_id`
- `lumina.amp_workcard_call_workcard.revision_id` → `history_id`
- `lumina.amp_workcard_cancellations.revision_id` → `history_id`
- `lumina.amp_workcard_extended_desc.revision_id` → `history_id`
- `lumina.amp_workcard_h3_7487bkp.revision_id` → `history_id`
- `lumina.amp_workcard_header_1.revision_id` → `history_id`
- `lumina.amp_workcard_header_1_43216.revision_id` → `history_id`
- `lumina.amp_workcard_header_2.revision_id` → `history_id`
- `lumina.amp_workcard_header_3.revision_id` → `history_id`
- `lumina.amp_workcard_header_4.revision_id` → `history_id`
- `lumina.amp_workcard_header_5.revision_number` → `history_id`
- `lumina.amp_workcard_header_5.revision_id` → `history_id`
- `lumina.amp_workcard_header_properties.revision_id` → `history_id`
- `lumina.amp_workcard_lcl_applicability.revision_id` → `history_id`
- `lumina.amp_workcard_narrative.revision_id` → `history_id`
- `lumina.amp_workcard_not_with_workcard.revision_id` → `history_id`
- `lumina.amp_workcard_previously_acc_by.revision_id` → `history_id`
- `lumina.amp_workcards_by_package.revision_id` → `history_id`
- `lumina.amp_workcards_by_section.revision_id` → `history_id`
- `lumina.fleet_forecast_plans.revision_id` → `history_id`
- `lumina.forecast_cache.revision_id` → `history_id`
- `lumina.forecast_cache_ac_details.revision_id` → `history_id`
- `lumina.forecast_cache_revisions.revision_id` → `history_id`
- `lumina.maint_cost_budget_adsb.revision_id` → `history_id`
- `lumina.maint_cost_budget_packages.revision_id` → `history_id`
- `lumina.maint_cost_budget_visits.revision_id` → `history_id`
- `lumina.maint_cost_budget_workcards.revision_id` → `history_id`
- `lumina.manufacturers_work_documents.revision_id` → `history_id`
- `lumina.mel_items.revision_id` → `history_id`
- `lumina.mel_references.revision_id` → `history_id`
- `lumina.mel_revision_history.revision_id` → `history_id`
- `lumina.mel_revisions.revision_id` → `history_id`
- `lumina.planners_notes_xref.revision_id` → `history_id`
- `lumina.rp_dependencies.revision_id` → `history_id`
- `lumina.tech_log_3.revision_id` → `history_id`
- `lumina.variations_xref.revision_id` → `history_id`
- `lumina.wcr_boeing_tb_revision.revision_id` → `history_id`
- `lumina.wcr_msg_log.revision_id` → `history_id`
- `lumina.wcr_temp_access_panels.revision_id` → `history_id`
- `lumina.wcr_temp_base1.revision_id` → `history_id`
- `lumina.wcr_temp_narratives.revision_id` → `history_id`

### lumina.amp_revision_status

**References (Outgoing):**

- `revision_status_id` → `lumina.amp_revision_status.revision_status_id`

**Referenced By (Incoming):**

- `lumina.amp_revision_status.revision_status_id` → `revision_status_id`
- `lumina.amp_revisions.revision_status_id` → `revision_status_id`
- `lumina.cq_quote_status.status_id` → `revision_status_id`
- `lumina.cq_quote_status_contacts.status_id` → `revision_status_id`
- `lumina.nrc_status_history.status_code` → `revision_status_id`
- `lumina.planners_notes.status_id` → `revision_status_id`
- `lumina.planners_notes_statuses.status_id` → `revision_status_id`
- `lumina.rd_xref_to_tech_logs.status_code` → `revision_status_id`
- `lumina.shipment_status_type.status_id` → `revision_status_id`
- `lumina.workcard_status_codes.status_code` → `revision_status_id`
- `lumina.works_order_sub_status.status_code` → `revision_status_id`

### lumina.amp_revisions

**References (Outgoing):**

- `revision_id` → `lumina.amp_revision_history.history_id`
- `revision_status_id` → `lumina.amp_revision_status.revision_status_id`
- `user_id` → `lumina.dataset_locks_by_user.user_id`

### lumina.amp_visit_notes

**References (Outgoing):**

- `visit_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.amp_visits

**References (Outgoing):**

- `visit_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `sequence_number` → `lumina.nrc_high_sequence_control.key_id`

**Referenced By (Incoming):**

- `lumina.fleet_forecast_plans_amp.visit_codes` → `fleet`

### lumina.amp_wc_aircraft_exclusions

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `sequence_number` → `lumina.nrc_high_sequence_control.key_id`

### lumina.amp_wc_in_limits_bak

**References (Outgoing):**

- `workcard_interval_id` → `lumina.amp_workcard_intervals.workcard_interval_id`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

### lumina.amp_wc_in_stages_bak

**References (Outgoing):**

- `workcard_interval_id` → `lumina.amp_workcard_intervals.workcard_interval_id`

### lumina.amp_wcard_extended_desc_41

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.amp_workcard_ac_effectivity

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `workcard_id` → `lumina.amp_access_panels_by_workcard.fleet`
- `sub_fleet_id` → `lumina.sub_fleet_header.sub_fleet_id`

### lumina.amp_workcard_ac_effectivity_jn

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `workcard_id` → `lumina.amp_access_panels_by_workcard.fleet`
- `sub_fleet_id` → `lumina.sub_fleet_header.sub_fleet_id`

### lumina.amp_workcard_accomplishments

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.amp_workcard_activations

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `workcard_activation_id` → `lumina.amp_workcard_activations.workcard_activation_id`

**Referenced By (Incoming):**

- `lumina.access_dim_accounts_info.vat_code` → `workcard_activation_id`
- `lumina.access_dim_sales_info.vat_code` → `workcard_activation_id`
- `lumina.amp_workcard_activations.workcard_activation_id` → `workcard_activation_id`
- `lumina.invoice_lines.vat_code` → `workcard_activation_id`
- `lumina.oeim_invoice_snap_vat_codes.vat_code` → `workcard_activation_id`
- `lumina.order_goods_received_invoices.vat_code` → `workcard_activation_id`
- `lumina.order_line_quotes_data.vat_code` → `workcard_activation_id`
- `lumina.order_lines.vat_code` → `workcard_activation_id`
- `lumina.part_number_vat_codes.vat_code` → `workcard_activation_id`
- `lumina.preorder_lines.vat_code` → `workcard_activation_id`
- `lumina.stock_groups.vat_code` → `workcard_activation_id`
- `lumina.stock_groups_bkp_oases382.vat_code` → `workcard_activation_id`
- `lumina.transaction_log_icarus.vat_code` → `workcard_activation_id`
- `lumina.transaction_log_icarus_8134.vat_code` → `workcard_activation_id`
- `lumina.vat_codes.vat_code` → `workcard_activation_id`
- `lumina.workcard_activations.workcard_activation_id` → `workcard_activation_id`

### lumina.amp_workcard_call_workcard

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `workcard_call_workcard_id` → `lumina.amp_workcard_call_workcard.workcard_call_workcard_id`
- `call_workcard_number` → `lumina.amp_workcard_call_workcard.workcard_call_workcard_id`

**Referenced By (Incoming):**

- `lumina.amp_workcard_call_workcard.workcard_call_workcard_id` → `workcard_call_workcard_id`
- `lumina.amp_workcard_call_workcard.call_workcard_number` → `workcard_call_workcard_id`

### lumina.amp_workcard_cancellations

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `workcard_cancellation_id` → `lumina.amp_workcard_cancellations.workcard_cancellation_id`

**Referenced By (Incoming):**

- `lumina.amp_workcard_cancellations.workcard_cancellation_id` → `workcard_cancellation_id`
- `lumina.workcard_cancellations.workcard_cancellation_id` → `workcard_cancellation_id`

### lumina.amp_workcard_extended_desc

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.amp_workcard_h3_7487bkp

**References (Outgoing):**

- `revision_id` → `lumina.amp_revision_history.history_id`
- `phase_code` → `lumina.rfc_frequency_phase_header.rfc_id`

### lumina.amp_workcard_header_1

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `workcard_id` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.amp_workcard_header_1_43216

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `workcard_id` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.amp_workcard_header_2

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.amp_workcard_header_3

**References (Outgoing):**

- `revision_id` → `lumina.amp_revision_history.history_id`
- `phase_code` → `lumina.rfc_frequency_phase_header.rfc_id`

### lumina.amp_workcard_header_4

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.amp_workcard_header_5

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_number` → `lumina.amp_revision_history.history_id`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.amp_workcard_header_properties

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.amp_workcard_intervals

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `workcard_id` → `lumina.amp_access_panels_by_workcard.fleet`
- `workcard_interval_id` → `lumina.amp_workcard_intervals.workcard_interval_id`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `component_life_limit_id` → `lumina.component_life_limits.component_life_limit_id`
- `sub_fleet_id` → `lumina.sub_fleet_header.sub_fleet_id`

**Referenced By (Incoming):**

- `lumina.amp_wc_in_limits_bak.workcard_interval_id` → `workcard_interval_id`
- `lumina.amp_wc_in_stages_bak.workcard_interval_id` → `workcard_interval_id`
- `lumina.amp_workcard_intervals.workcard_interval_id` → `workcard_interval_id`
- `lumina.amp_workcard_intervals_limits.workcard_interval_id` → `workcard_interval_id`
- `lumina.amp_workcard_intervals_stages.workcard_interval_id` → `workcard_interval_id`
- `lumina.forecast_cache.workcard_interval_id` → `workcard_interval_id`
- `lumina.planners_notes_xref.workcard_interval_id` → `workcard_interval_id`
- `lumina.schedule_forecast_xref.workcard_interval_id` → `workcard_interval_id`
- `lumina.variations_xref.workcard_interval_id` → `workcard_interval_id`

### lumina.amp_workcard_intervals_limits

**References (Outgoing):**

- `workcard_interval_id` → `lumina.amp_workcard_intervals.workcard_interval_id`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

### lumina.amp_workcard_intervals_stages

**References (Outgoing):**

- `workcard_interval_id` → `lumina.amp_workcard_intervals.workcard_interval_id`

### lumina.amp_workcard_lcl_applicability

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

**Referenced By (Incoming):**

- `lumina.part_applicability_codes.applicability_code` → `life_code_level_id`

### lumina.amp_workcard_narrative

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.amp_workcard_not_with_workcard

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `workcard_not_with_workcard_id` → `lumina.amp_workcard_not_with_workcard.workcard_not_with_workcard_id`
- `not_with_workcard_number` → `lumina.amp_workcard_not_with_workcard.workcard_not_with_workcard_id`

**Referenced By (Incoming):**

- `lumina.amp_workcard_not_with_workcard.workcard_not_with_workcard_id` → `workcard_not_with_workcard_id`
- `lumina.amp_workcard_not_with_workcard.not_with_workcard_number` → `workcard_not_with_workcard_id`

### lumina.amp_workcard_previously_acc_by

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `workcard_previously_acc_id` → `lumina.amp_workcard_previously_acc_by.workcard_previously_acc_id`

**Referenced By (Incoming):**

- `lumina.amp_workcard_previously_acc_by.workcard_previously_acc_id` → `workcard_previously_acc_id`

### lumina.amp_workcard_publications

**References (Outgoing):**

- `workcard_id` → `lumina.amp_access_panels_by_workcard.fleet`
- `publication_id` → `lumina.amp_workcard_publications.publication_id`
- `publication_code` → `lumina.amp_workcard_publications.publication_id`

**Referenced By (Incoming):**

- `lumina.amp_workcard_publications.publication_id` → `publication_id`
- `lumina.amp_workcard_publications.publication_code` → `publication_id`
- `lumina.rfc_header_publications.publication_code` → `publication_id`
- `lumina.rfc_publications.publication_code` → `publication_id`

### lumina.amp_workcard_saved_reports

**References (Outgoing):**

- `saved_report_id` → `lumina.amp_workcard_saved_reports.saved_report_id`

**Referenced By (Incoming):**

- `lumina.amp_workcard_saved_reports.saved_report_id` → `saved_report_id`
- `lumina.amp_workcard_saved_reports_hdr.saved_report_id` → `saved_report_id`
- `lumina.wcr_boeing_tb_revision.save_id` → `saved_report_id`

### lumina.amp_workcard_saved_reports_hdr

**References (Outgoing):**

- `saved_report_id` → `lumina.amp_workcard_saved_reports.saved_report_id`

### lumina.amp_workcard_sections

**References (Outgoing):**

- `section_id` → `lumina.amp_workcard_sections.section_id`
- `section_code` → `lumina.amp_workcard_sections.section_id`

**Referenced By (Incoming):**

- `lumina.amp_workcard_sections.section_id` → `section_id`
- `lumina.amp_workcard_sections.section_code` → `section_id`
- `lumina.amp_workcards_by_section.section_id` → `section_id`
- `lumina.dmg_rpr_damage.section_id` → `section_id`
- `lumina.dmg_rpr_measurement_sections.section_id` → `section_id`
- `lumina.dmg_rpr_section_details.section_id` → `section_id`
- `lumina.dmg_rpr_section_fleet_details.section_id` → `section_id`
- `lumina.dmg_rpr_subject_sections.section_id` → `section_id`
- `lumina.rfc_header.section_id` → `section_id`
- `lumina.rfc_statement_sections.section_id` → `section_id`
- `lumina.rfc_statement_sections.section_code` → `section_id`

### lumina.amp_workcards_by_package

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

**Referenced By (Incoming):**

- `lumina.fleet_forecast_plans_amp.workcard_numbers` → `fleet`

### lumina.amp_workcards_by_section

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `section_id` → `lumina.amp_workcard_sections.section_id`
- `user_id` → `lumina.dataset_locks_by_user.user_id`

### lumina.assemble_thrust_life_code

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `life_code` → `lumina.aircraft_life.aircraft_code`
- `fleet_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `life_code_id` → `lumina.assemble_thrust_life_code.life_code_id`

**Referenced By (Incoming):**

- `lumina.assemble_thrust_life_code.life_code_id` → `life_code_id`

### lumina.assembly_model_header

**References (Outgoing):**

- `model_id` → `lumina.assembly_model_header.model_id`

**Referenced By (Incoming):**

- `lumina.assembly_model_header.model_id` → `model_id`
- `lumina.assembly_model_nodes.model_id` → `model_id`

### lumina.assembly_model_nodes

**References (Outgoing):**

- `model_id` → `lumina.assembly_model_header.model_id`
- `node_id` → `lumina.assembly_model_nodes.model_id`

**Referenced By (Incoming):**

- `lumina.assembly_model_nodes.node_id` → `model_id`

### lumina.audit_trail

**References (Outgoing):**

- `audit_id` → `lumina.amp_audit_notes.fleet_code`
- `user_id` → `lumina.dataset_locks_by_user.user_id`

### lumina.audit_trail_ids

**References (Outgoing):**

- `audit_id` → `lumina.amp_audit_notes.fleet_code`

### lumina.audit_trail_meta_data

**References (Outgoing):**

- `audit_id` → `lumina.amp_audit_notes.fleet_code`
- `meta_id` → `lumina.audit_trail_meta_data.meta_id`

**Referenced By (Incoming):**

- `lumina.audit_trail_meta_data.meta_id` → `meta_id`

### lumina.b737ng_activity_import_table

**Referenced By (Incoming):**

- `lumina.sfdc_activity.activity_id` → `schedule_reference`

### lumina.bar_codes

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `bar_code` → `lumina.bar_codes.works_order_number`
- `works_order_number` → `lumina.credit_works_order_cards.credit_note_no`

**Referenced By (Incoming):**

- `lumina.bar_codes.bar_code` → `works_order_number`

### lumina.batch_file_header

**Referenced By (Incoming):**

- `lumina.batch_history.batch_number` → `key`
- `lumina.batch_notes.batch_number` → `key`
- `lumina.batch_notes_gu4240.batch_number` → `key`
- `lumina.batch_orders.batch_number` → `key`
- `lumina.batch_record_1.batch_number` → `key`
- `lumina.batch_record_1_gu4240.batch_number` → `key`
- `lumina.batch_record_2.batch_number` → `key`
- `lumina.batch_record_camo.batch_number` → `key`
- `lumina.batches_by_airway_bill.batch_number` → `key`
- `lumina.batches_by_customs_entry.batch_number` → `key`
- `lumina.component_movement_history_ext.batch_number` → `key`
- `lumina.component_movt_hist_ext_8661.batch_number` → `key`
- `lumina.consumable_batch_locations.batch_number` → `key`
- `lumina.consumable_history.batch_number` → `key`
- `lumina.consumable_repair_xref_to_part.batch_number` → `key`
- `lumina.credit_works_order_cards.batch_number` → `key`
- `lumina.delivery_note_item_header_1.batch_number` → `key`
- `lumina.goods_received_sheet_document.batch_number` → `key`
- `lumina.ie96_historic.batch_number` → `key`
- `lumina.inherited_acquisition_costs.batch_number` → `key`
- `lumina.invoice_lines.batch_number` → `key`
- `lumina.invoice_trail_entries.batch_number` → `key`
- `lumina.maint_material_costs.batch_number` → `key`
- `lumina.nrc_tools.batch_number` → `key`
- `lumina.oeim_credit_warranty.batch_number` → `key`
- `lumina.oeim_invoice_materials.batch_number` → `key`
- `lumina.oeim_invoice_warranty.batch_number` → `key`
- `lumina.oeim_invoice_warranty_refunds.batch_number` → `key`
- `lumina.order_history.batch_number` → `key`
- `lumina.pick_hist_7890_bkp.batch_number` → `key`
- `lumina.pick_history.batch_number` → `key`
- `lumina.preorder_line_stock_info.batch_number` → `key`
- `lumina.repair_approval_data.batch_number` → `key`
- `lumina.requirement_recharge_details.batch_number` → `key`
- `lumina.rotable_batch_locations.batch_number` → `key`
- `lumina.rotable_history.batch_number` → `key`
- `lumina.sales_history.batch_number` → `key`
- `lumina.sales_order_dispatches.batch_number` → `key`
- `lumina.shelf_li_dt_bkp_2020.batch_number` → `key`
- `lumina.shelf_life_dates.batch_number` → `key`
- `lumina.shelf_life_dates_oases6834.batch_number` → `key`
- `lumina.shipment_demands.batch_number` → `key`
- `lumina.shipment_item.batch_number` → `key`
- `lumina.stock_audit_batches.batch_number` → `key`
- `lumina.stock_documents.batch_number` → `key`
- `lumina.tool_check_out_in.batch_number` → `key`
- `lumina.tool_check_out_in_duplicates.batch_number` → `key`
- `lumina.transaction_log_icarus.batch_number` → `key`
- `lumina.transaction_log_icarus_8134.batch_number` → `key`
- `lumina.unsatified_service_exchanges.batch_number` → `key`
- `lumina.warranty_claims.batch_number` → `key`

### lumina.batch_history

**References (Outgoing):**

- `batch_number` → `lumina.batch_file_header.key`
- `user_id` → `lumina.dataset_locks_by_user.user_id`

### lumina.batch_notes

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.batch_notes_gu4240

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.batch_orders

**References (Outgoing):**

- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`

**Referenced By (Incoming):**

- `lumina.airway_bill_references.order_number` → `batch_number`
- `lumina.batch_orders.order_number` → `batch_number`
- `lumina.batch_record_1.order_number` → `batch_number`
- `lumina.batch_record_1_gu4240.order_number` → `batch_number`
- `lumina.consumable_history.order_number` → `batch_number`
- `lumina.consumable_repair_xref_to_part.order_number` → `batch_number`
- `lumina.credit_works_order_cards.order_number` → `batch_number`
- `lumina.delivery_note_header_1.order_number` → `batch_number`
- `lumina.dmg_rpr_document_order.order_number` → `batch_number`
- `lumina.freight_costs.order_number` → `batch_number`
- `lumina.ie96_historic.order_number` → `batch_number`
- `lumina.invoice_lines.order_number` → `batch_number`
- `lumina.invoice_trail_entries.order_number` → `batch_number`
- `lumina.loaned_units.order_number` → `batch_number`
- `lumina.monthly_loans_in.order_number` → `batch_number`
- `lumina.oeim_credit_warranty.order_number` → `batch_number`
- `lumina.oeim_invoice_materials.order_number` → `batch_number`
- `lumina.oeim_invoice_warranty.order_number` → `batch_number`
- `lumina.oeim_invoice_warranty_refunds.order_number` → `batch_number`
- `lumina.ord_po_unit_conv_delta1827.order_number` → `batch_number`
- `lumina.order_change_history.order_number` → `batch_number`
- `lumina.order_customs_info.order_number` → `batch_number`
- `lumina.order_delivery_note_remarks.order_number` → `batch_number`
- `lumina.order_email_chasing.order_number` → `batch_number`
- `lumina.order_goods_received.order_number` → `batch_number`
- `lumina.order_goods_received_invoices.order_number` → `batch_number`
- `lumina.order_header_1.order_number` → `batch_number`
- `lumina.order_header_2.order_number` → `batch_number`
- `lumina.order_header_3.order_number` → `batch_number`
- `lumina.order_header_4.order_number` → `batch_number`
- `lumina.order_history.order_number` → `batch_number`
- `lumina.order_line_additional_info.order_number` → `batch_number`
- `lumina.order_line_additional_info_2.order_number` → `batch_number`
- `lumina.order_line_notes.order_number` → `batch_number`
- `lumina.order_line_quotes_data.order_number` → `batch_number`
- `lumina.order_line_requirement_xref.order_number` → `batch_number`
- `lumina.order_line_weight_dimension.order_number` → `batch_number`
- `lumina.order_lines.order_number` → `batch_number`
- `lumina.order_numbers_by_supplier.order_number` → `batch_number`
- `lumina.order_print_date.order_number` → `batch_number`
- `lumina.order_purchase_unit_conversion.order_number` → `batch_number`
- `lumina.order_requirement_allocation.order_number` → `batch_number`
- `lumina.order_supplier_approval.order_number` → `batch_number`
- `lumina.order_text.order_number` → `batch_number`
- `lumina.order_workshop_works_orders.order_number` → `batch_number`
- `lumina.orders_by_due_date.order_number` → `batch_number`
- `lumina.orders_to_part_number_xref.order_number` → `batch_number`
- `lumina.ordr_goods_bkp.order_number` → `batch_number`
- `lumina.parts_received_without_cost.order_number` → `batch_number`
- `lumina.pick_hist_7890_bkp.order_number` → `batch_number`
- `lumina.pick_history.order_number` → `batch_number`
- `lumina.quote_email_chasing.order_number` → `batch_number`
- `lumina.rfq_to_order_xref.order_number` → `batch_number`
- `lumina.rotable_history.order_number` → `batch_number`
- `lumina.sage_order_line_details.order_number` → `batch_number`
- `lumina.sales_history.order_number` → `batch_number`
- `lumina.sap_order_header.order_number` → `batch_number`
- `lumina.sap_order_line.order_number` → `batch_number`
- `lumina.shipment_order_demands.order_number` → `batch_number`
- `lumina.strip_report_header_1.order_number` → `batch_number`
- `lumina.taskcard_wo_order_line.order_number` → `batch_number`
- `lumina.transaction_log_icarus.order_number` → `batch_number`
- `lumina.transaction_log_icarus_8134.order_number` → `batch_number`
- `lumina.unsatified_service_exchanges.order_number` → `batch_number`
- `lumina.works_orders.order_number` → `batch_number`

### lumina.batch_record_1

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `currency_code` → `lumina.currency_codes.currency_code`
- `goods_received_number` → `lumina.goods_received_sheet_document.batch_number`

### lumina.batch_record_1_gu4240

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `currency_code` → `lumina.currency_codes.currency_code`
- `goods_received_number` → `lumina.goods_received_sheet_document.batch_number`

### lumina.batch_record_2

**References (Outgoing):**

- `batch_number` → `lumina.batch_file_header.key`
- `customs_entry_number` → `lumina.batches_by_customs_entry.customs_entry_number`
- `currency_code` → `lumina.currency_codes.currency_code`

### lumina.batch_record_camo

**References (Outgoing):**

- `batch_number` → `lumina.batch_file_header.key`

### lumina.batches_by_airway_bill

**References (Outgoing):**

- `airway_bill_number` → `lumina.airway_bill_references.awb_id`
- `batch_number` → `lumina.batch_file_header.key`

### lumina.batches_by_customs_entry

**References (Outgoing):**

- `batch_number` → `lumina.batch_file_header.key`
- `customs_entry_number` → `lumina.batches_by_customs_entry.customs_entry_number`

**Referenced By (Incoming):**

- `lumina.batch_record_2.customs_entry_number` → `customs_entry_number`
- `lumina.batches_by_customs_entry.customs_entry_number` → `customs_entry_number`
- `lumina.maintenance_cost_entry.entry_id` → `customs_entry_number`
- `lumina.shipment_item_customs.customs_entry_number` → `customs_entry_number`

### lumina.bins

**References (Outgoing):**

- `warehouse_code` → `lumina.account_available_warehouses.account_code`
- `bin_number` → `lumina.bins.bin_number`

**Referenced By (Incoming):**

- `lumina.bins.bin_number` → `bin_number`
- `lumina.ie96_historic.bin_number` → `bin_number`
- `lumina.order_lines.bin_number` → `bin_number`
- `lumina.preorder_line_stock_info.bin_number` → `bin_number`
- `lumina.random_stock_check_bins.bin_number` → `bin_number`
- `lumina.rotable_batch_locations.bin_number` → `bin_number`
- `lumina.stock_audit_batches.bin_number` → `bin_number`
- `lumina.stock_audit_bins.bin_number` → `bin_number`
- `lumina.stock_by_bin.bin_number` → `bin_number`
- `lumina.transaction_log_icarus.bin_number` → `bin_number`
- `lumina.transaction_log_icarus_8134.bin_number` → `bin_number`
- `lumina.works_order_issues_and_returns.bin_number` → `bin_number`
- `lumina.works_order_issues_and_rtn_bac.bin_number` → `bin_number`

### lumina.bkp_mobile_permissions

**References (Outgoing):**

- `permission_id` → `lumina.add_extension_permissions.user_id`

**Referenced By (Incoming):**

- `lumina.account_buying_contacts.mobile_number` → `oases_security_token`

### lumina.block_countries

**References (Outgoing):**

- `block_code` → `lumina.block_countries.block_code`

**Referenced By (Incoming):**

- `lumina.block_countries.block_code` → `block_code`
- `lumina.economic_blocks.block_code` → `block_code`
- `lumina.order_standard_text_blocks.block_number` → `block_code`
- `lumina.rp_block_resource.block_id` → `block_code`
- `lumina.rp_block_resource_days.block_id` → `block_code`

### lumina.bulk_batch_header

**References (Outgoing):**

- `bulk_batch_number` → `lumina.bulk_batch_header.bulk_batch_number`

**Referenced By (Incoming):**

- `lumina.bulk_batch_header.bulk_batch_number` → `bulk_batch_number`

### lumina.cfd_categories

**Referenced By (Incoming):**

- `lumina.requirements.cfd_number` → `cfd_category`

### lumina.cfd_categorires_bkpoases405

**Referenced By (Incoming):**

- `lumina.oeim_invoice_snap_users.oases_id` → `cfd_category`

### lumina.cfd_xref_to_tech_log

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.company_codes

**References (Outgoing):**

- `company_code` → `lumina.company_codes.company_code`

**Referenced By (Incoming):**

- `lumina.company_codes.company_code` → `company_code`
- `lumina.company_form_details.company_code` → `company_code`
- `lumina.delivery_note_header_1.company_code` → `company_code`
- `lumina.order_header_1.company_code` → `company_code`
- `lumina.preorders.company_code` → `company_code`
- `lumina.sales_orders.company_code` → `company_code`
- `lumina.sales_request_quote_header.company_code` → `company_code`
- `lumina.shipment.company_code` → `company_code`
- `lumina.transaction_log_icarus.company_code` → `company_code`
- `lumina.transaction_log_icarus_8134.company_code` → `company_code`
- `lumina.works_orders.company_code` → `company_code`
- `lumina.works_orders_by_account.company_code` → `company_code`

### lumina.company_form_attachments

**References (Outgoing):**

- `attachment_id` → `lumina.company_form_attachments.attachment_id`
- `company_form_id` → `lumina.company_form_attachments.attachment_id`

**Referenced By (Incoming):**

- `lumina.company_form_attachments.attachment_id` → `attachment_id`
- `lumina.company_form_attachments.company_form_id` → `attachment_id`
- `lumina.company_form_details.company_form_id` → `attachment_id`
- `lumina.company_form_details.form_number` → `attachment_id`
- `lumina.form_number.form_number` → `attachment_id`

### lumina.company_form_details

**References (Outgoing):**

- `company_code` → `lumina.company_codes.company_code`
- `company_form_id` → `lumina.company_form_attachments.attachment_id`
- `form_number` → `lumina.company_form_attachments.attachment_id`

### lumina.completion_fleet_ata_pos

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.completion_life_values

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

### lumina.completion_maint_mod

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `report_id` → `lumina.amp_report_documents.fleet`

### lumina.completion_part_serial

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `lumina.completion_part_serial.part_number`

**Referenced By (Incoming):**

- `lumina.accomp_bkup.serial_number` → `part_number`
- `lumina.accomp_hist_delta_1763.serial_number` → `part_number`
- `lumina.accomp_hist_lost_sched.serial_number` → `part_number`
- `lumina.accomplishment_history.serial_number` → `part_number`
- `lumina.aircraft_build.serial_number` → `part_number`
- `lumina.aircraft_leased_apu.serial_number` → `part_number`
- `lumina.aircraft_leased_engines.serial_number` → `part_number`
- `lumina.aircraft_leased_landing_gear.serial_number` → `part_number`
- `lumina.aircraft_leased_propellers.serial_number` → `part_number`
- `lumina.aircraft_major_checks.serial_number` → `part_number`
- `lumina.amp_component_intervals.serial_number` → `part_number`
- `lumina.amp_datmig_accomplishments.serial_number` → `part_number`
- `lumina.amp_datmig_llp.serial_number` → `part_number`
- `lumina.amp_workcard_intervals.serial_number` → `part_number`
- `lumina.batch_notes.serial_number` → `part_number`
- `lumina.batch_notes_gu4240.serial_number` → `part_number`
- `lumina.batch_record_1.serial_number` → `part_number`
- `lumina.batch_record_1_gu4240.serial_number` → `part_number`
- `lumina.completion_life_values.serial_number` → `part_number`
- `lumina.completion_part_serial.serial_number` → `part_number`
- `lumina.component_life.serial_number` → `part_number`
- `lumina.component_movement_hist_life.serial_number` → `part_number`
- `lumina.component_movement_history.serial_number` → `part_number`
- `lumina.component_movement_history_ext.serial_number` → `part_number`
- `lumina.component_movt_hist_ext_8661.serial_number` → `part_number`
- `lumina.components.serial_number` → `part_number`
- `lumina.components_bkp_dj95.serial_number` → `part_number`
- `lumina.components_bkp_dj97.serial_number` → `part_number`
- `lumina.components_oases971.serial_number` → `part_number`
- `lumina.credit_works_order_cards.serial_number` → `part_number`
- `lumina.daily_loans_out.serial_number` → `part_number`
- `lumina.dmg_rpr_damage.serial_number` → `part_number`
- `lumina.dmg_rpr_fitted_locations.serial_number` → `part_number`
- `lumina.drn_component_mods_history.serial_number` → `part_number`
- `lumina.drn_components_nsbl_history.serial_number` → `part_number`
- `lumina.drn_life_limits.serial_number` → `part_number`
- `lumina.drn_part_serial.serial_number` → `part_number`
- `lumina.dues_register.serial_number` → `part_number`
- `lumina.fleet_forecast_plans_drn.serial_number` → `part_number`
- `lumina.ie96_historic.serial_number` → `part_number`
- `lumina.inherited_acquisition_costs.serial_number` → `part_number`
- `lumina.invoice_trail_entries.serial_number` → `part_number`
- `lumina.latest_repair_values.serial_number` → `part_number`
- `lumina.loaned_units.serial_number` → `part_number`
- `lumina.long_serial_number_xref.serial_number` → `part_number`
- `lumina.maint_material_costs.serial_number` → `part_number`
- `lumina.monthly_loans_in.serial_number` → `part_number`
- `lumina.monthly_loans_out.serial_number` → `part_number`
- `lumina.oeim_credit_warranty.serial_number` → `part_number`
- `lumina.oeim_invoice_materials.serial_number` → `part_number`
- `lumina.oeim_invoice_snap_serl_master.serial_number` → `part_number`
- `lumina.oeim_invoice_warranty.serial_number` → `part_number`
- `lumina.oeim_invoice_warranty_refunds.serial_number` → `part_number`
- `lumina.order_history.serial_number` → `part_number`
- `lumina.original_purchase_values.serial_number` → `part_number`
- `lumina.part_number_properties_serials.serial_number` → `part_number`
- `lumina.part_serial_documents.serial_number` → `part_number`
- `lumina.pick_hist_7890_bkp.serial_number` → `part_number`
- `lumina.pick_history.serial_number` → `part_number`
- `lumina.planners_notes_xref.serial_number` → `part_number`
- `lumina.preorder_line_stock_info.serial_number` → `part_number`
- `lumina.rfc_components.serial_number` → `part_number`
- `lumina.rotable_batch_locations.serial_number` → `part_number`
- `lumina.rotable_history.serial_number` → `part_number`
- `lumina.sales_history.serial_number` → `part_number`
- `lumina.sales_order_dispatches.serial_number` → `part_number`
- `lumina.schedule_forecast_xref.serial_number` → `part_number`
- `lumina.schedule_source.serial_number` → `part_number`
- `lumina.serial_numbers_by_part.serial_number` → `part_number`
- `lumina.shelf_li_dt_bkp_2020.serial_number` → `part_number`
- `lumina.shelf_life_dates.serial_number` → `part_number`
- `lumina.shelf_life_dates_oases6834.serial_number` → `part_number`
- `lumina.shipment_demands.serial_number` → `part_number`
- `lumina.shipment_item.serial_number` → `part_number`
- `lumina.strip_report_header_1.serial_number` → `part_number`
- `lumina.task_activity_link.serial_number` → `part_number`
- `lumina.transaction_log_icarus.serial_number` → `part_number`
- `lumina.transaction_log_icarus_8134.serial_number` → `part_number`
- `lumina.unit_owners.serial_number` → `part_number`
- `lumina.unsatified_service_exchanges.serial_number` → `part_number`
- `lumina.variations_xref.serial_number` → `part_number`
- `lumina.warranty_claims.serial_number` → `part_number`
- `lumina.warranty_exclusions.serial_number` → `part_number`
- `lumina.warranty_terms.serial_number` → `part_number`
- `lumina.works_orders.serial_number` → `part_number`

### lumina.component_life

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

### lumina.component_life_limits

**References (Outgoing):**

- `component_life_limit_id` → `lumina.component_life_limits.component_life_limit_id`

**Referenced By (Incoming):**

- `lumina.amp_component_intervals.component_life_limit_id` → `component_life_limit_id`
- `lumina.amp_component_reset_on_compl.component_life_limit_id` → `component_life_limit_id`
- `lumina.amp_workcard_intervals.component_life_limit_id` → `component_life_limit_id`
- `lumina.component_life_limits.component_life_limit_id` → `component_life_limit_id`
- `lumina.component_movement_history_ext.component_life_limit_id` → `component_life_limit_id`
- `lumina.component_movt_hist_ext_8661.component_life_limit_id` → `component_life_limit_id`
- `lumina.forecast_cache.component_life_limit_id` → `component_life_limit_id`
- `lumina.part_number_shelf_life_details.component_life_limit_id` → `component_life_limit_id`
- `lumina.shelf_li_dt_bkp_2020.component_life_limit_id` → `component_life_limit_id`
- `lumina.shelf_life_dates.component_life_limit_id` → `component_life_limit_id`
- `lumina.shelf_life_dates_oases6834.component_life_limit_id` → `component_life_limit_id`

### lumina.component_mods_history_by_part

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.component_movement_hist_life

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `history_id` → `lumina.accomplishment_history.accomplishment_id`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

**Referenced By (Incoming):**

- `lumina.consumable_history.movement_code` → `part_number`
- `lumina.demand_reason_to_movement_code.movement_code` → `part_number`
- `lumina.movement_codes.movement_code` → `part_number`
- `lumina.order_lines.movement_code` → `part_number`
- `lumina.preorder_line_stock_info.movement_code` → `part_number`
- `lumina.repair_approval_data.movement_code` → `part_number`
- `lumina.requests_for_quotes_lines.movement_code` → `part_number`
- `lumina.rotable_batch_locations.movement_code` → `part_number`
- `lumina.rotable_history.movement_code` → `part_number`
- `lumina.transaction_log_icarus.movement_code` → `part_number`
- `lumina.transaction_log_icarus_8134.movement_code` → `part_number`
- `lumina.works_orders.movement_code` → `part_number`

### lumina.component_movement_history

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.component_movement_history_ext

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `history_id` → `lumina.accomplishment_history.accomplishment_id`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `report_id` → `lumina.amp_report_documents.fleet`
- `batch_number` → `lumina.batch_file_header.key`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `component_life_limit_id` → `lumina.component_life_limits.component_life_limit_id`

### lumina.component_movt_hist_ext_8661

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `history_id` → `lumina.accomplishment_history.accomplishment_id`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `report_id` → `lumina.amp_report_documents.fleet`
- `batch_number` → `lumina.batch_file_header.key`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `component_life_limit_id` → `lumina.component_life_limits.component_life_limit_id`

### lumina.components

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.components_bkp_dj95

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.components_bkp_dj97

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.components_oases971

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.condition_codes

**References (Outgoing):**

- `condition_code` → `lumina.condition_codes.condition_code`

**Referenced By (Incoming):**

- `lumina.condition_codes.condition_code` → `condition_code`
- `lumina.order_history.condition_code` → `condition_code`
- `lumina.order_line_additional_info.condition_code` → `condition_code`
- `lumina.preorder_lines.condition_code` → `condition_code`
- `lumina.rfq_history.condition_code` → `condition_code`
- `lumina.sales_history.condition_code` → `condition_code`
- `lumina.sales_prices.condition_code` → `condition_code`
- `lumina.sales_quotes_out_history.condition_code` → `condition_code`
- `lumina.warranty_terms.condition_code` → `condition_code`

### lumina.condition_pick_table

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `warehouse_code` → `lumina.account_available_warehouses.account_code`
- `pick_number` → `lumina.condition_pick_table.part_number`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`

**Referenced By (Incoming):**

- `lumina.condition_pick_table.pick_number` → `part_number`
- `lumina.delivery_note_item_header_2.pick_number` → `part_number`
- `lumina.part_xref_to_pick_history.pick_number` → `part_number`
- `lumina.pick_hist_7890_bkp.pick_number` → `part_number`
- `lumina.pick_history.pick_number` → `part_number`
- `lumina.shipment_requirement_demands.pick_number` → `part_number`

### lumina.consumable_batch_locations

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`

### lumina.consumable_history

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `approval_code` → `lumina.account_supplier_approvals.account_code`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`
- `movement_code` → `lumina.component_movement_hist_life.part_number`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`
- `authority_code` → `lumina.rfc_regulating_authority.authority_code`

**Referenced By (Incoming):**

- `lumina.shipment_demands.consumable_history_id` → `id`

### lumina.consumable_repair_xref_to_part

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_permanent_repairs.repair_id` → `part_number`

### lumina.consumables_below_re_order

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.contacts_xref

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.continents

**References (Outgoing):**

- `continent_id` → `lumina.continents.continent_id`

**Referenced By (Incoming):**

- `lumina.continents.continent_id` → `continent_id`
- `lumina.countries.continent_id` → `continent_id`

### lumina.corrosion_categories

**References (Outgoing):**

- `corrosion_code` → `lumina.corrosion_categories.corrosion_code`

**Referenced By (Incoming):**

- `lumina.corrosion_categories.corrosion_code` → `corrosion_code`
- `lumina.nrc_defect_details.corrosion_code` → `corrosion_code`
- `lumina.tech_log_3.corrosion_code` → `corrosion_code`

### lumina.cost_codes

**References (Outgoing):**

- `cost_code` → `lumina.cost_codes.id`

**Referenced By (Incoming):**

- `lumina.cost_codes.cost_code` → `id`
- `lumina.cq_fixed_charge_xref.cost_code` → `id`
- `lumina.cq_quote_cards.cost_code` → `id`
- `lumina.cq_quote_nrcs.cost_code` → `id`
- `lumina.cq_quote_packages.cost_code` → `id`
- `lumina.customer_contract_rates.cost_code` → `id`
- `lumina.customer_contract_stop_incl.cost_code` → `id`
- `lumina.default_labour_rates.cost_code` → `id`
- `lumina.fixed_charges.cost_code` → `id`
- `lumina.maint_cost_budget_workcards.cost_code` → `id`
- `lumina.maint_cost_hourly_rates.cost_code` → `id`
- `lumina.maintenance_cost_entry.cost_id` → `id`
- `lumina.maintenance_cost_types.cost_id` → `id`
- `lumina.mandatory_parts.cost_code` → `id`
- `lumina.oeim_invoice_fixed_charges.cost_code` → `id`
- `lumina.oeim_invoice_packages.cost_code` → `id`
- `lumina.oeim_invoice_snap_con_rates.cost_code` → `id`
- `lumina.oeim_invoice_snap_cost_codes.cost_code` → `id`
- `lumina.requirement_recharge_details.cost_code` → `id`

### lumina.countries

**References (Outgoing):**

- `continent_id` → `lumina.continents.continent_id`

### lumina.cq_documents

**References (Outgoing):**

- `quote_id` → `lumina.cq_quote_cards.quote_id`
- `document_image_id` → `lumina.document_image_source.document_image_source_id`

### lumina.cq_fixed_charge_xref

**References (Outgoing):**

- `cost_code` → `lumina.cost_codes.id`
- `fixed_charge_id` → `lumina.cq_fixed_charge_xref.quote_id`
- `quote_id` → `lumina.cq_quote_cards.quote_id`

**Referenced By (Incoming):**

- `lumina.cq_fixed_charge_xref.fixed_charge_id` → `quote_id`

### lumina.cq_quote_cards

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `cost_code` → `lumina.cost_codes.id`
- `quote_id` → `lumina.cq_quote_cards.quote_id`

**Referenced By (Incoming):**

- `lumina.cq_documents.quote_id` → `quote_id`
- `lumina.cq_fixed_charge_xref.quote_id` → `quote_id`
- `lumina.cq_quote_cards.quote_id` → `quote_id`
- `lumina.cq_quote_materials.quote_id` → `quote_id`
- `lumina.cq_quote_nrc_access_panels.quote_id` → `quote_id`
- `lumina.cq_quote_nrcs.quote_id` → `quote_id`
- `lumina.cq_quote_packages.quote_id` → `quote_id`
- `lumina.cq_quotes.quote_id` → `quote_id`
- `lumina.maint_cost_mro_wo_quotes.quote_id` → `quote_id`
- `lumina.maintenance_cost_quotes.quote_id` → `quote_id`

### lumina.cq_quote_materials

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `quote_id` → `lumina.cq_quote_cards.quote_id`

### lumina.cq_quote_nrc_access_panels

**References (Outgoing):**

- `access_panel_code` → `lumina.amp_access_panel_desc_hdr.fleet`
- `quote_id` → `lumina.cq_quote_cards.quote_id`
- `quote_nrc_id` → `lumina.cq_quote_nrc_access_panels.quote_id`

**Referenced By (Incoming):**

- `lumina.cq_quote_nrc_access_panels.quote_nrc_id` → `quote_id`
- `lumina.cq_quote_nrcs.quote_nrc_id` → `quote_id`
- `lumina.esign_off_nrc.nrc_number` → `quote_id`
- `lumina.maint_nrc_costs.nrc_number` → `quote_id`
- `lumina.nrc_access_panels.nrc_number` → `quote_id`
- `lumina.nrc_documents.nrc_number` → `quote_id`
- `lumina.nrc_materials.nrc_number` → `quote_id`
- `lumina.nrc_properties.nrc_number` → `quote_id`
- `lumina.nrc_tools.nrc_number` → `quote_id`
- `lumina.nrc_workcard_narrative.nrc_number` → `quote_id`
- `lumina.nrc_xref_to_scheduled_workcard.nrc_number` → `quote_id`
- `lumina.rdi_to_nrc.nrc_number` → `quote_id`
- `lumina.rp_employee_allocation.nrc_number` → `quote_id`
- `lumina.rp_wo_base_nrc_plan.nrc_number` → `quote_id`
- `lumina.rp_wo_nrc_plan.nrc_number` → `quote_id`
- `lumina.work_schedule_defect_1.nrc_number` → `quote_id`

### lumina.cq_quote_nrcs

**References (Outgoing):**

- `cost_code` → `lumina.cost_codes.id`
- `quote_id` → `lumina.cq_quote_cards.quote_id`
- `quote_nrc_id` → `lumina.cq_quote_nrc_access_panels.quote_id`

### lumina.cq_quote_packages

**References (Outgoing):**

- `package_code` → `lumina.amp_package_notes.fleet`
- `cost_code` → `lumina.cost_codes.id`
- `quote_id` → `lumina.cq_quote_cards.quote_id`

### lumina.cq_quote_status

**References (Outgoing):**

- `status_id` → `lumina.amp_revision_status.revision_status_id`
- `policy_id` → `lumina.security_policy.policy_id`

### lumina.cq_quote_status_contacts

**References (Outgoing):**

- `status_id` → `lumina.amp_revision_status.revision_status_id`

### lumina.cq_quotes

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `quote_id` → `lumina.cq_quote_cards.quote_id`

### lumina.credit_works_order_cards

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`

**Referenced By (Incoming):**

- `lumina.bar_codes.works_order_number` → `credit_note_no`
- `lumina.forecast_cache.works_order_number` → `credit_note_no`
- `lumina.order_header_2.works_order_number` → `credit_note_no`
- `lumina.stock_works_order_markups.works_order_number` → `credit_note_no`
- `lumina.strip_report_header_1.works_order_number` → `credit_note_no`
- `lumina.transaction_log_icarus.works_order_number` → `credit_note_no`
- `lumina.transaction_log_icarus_8134.works_order_number` → `credit_note_no`
- `lumina.work_schedule_header_2.works_order_number` → `credit_note_no`

### lumina.credit_works_orders

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.crs_signature_text

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `crs_text_id` → `lumina.crs_text.crs_text_id`

### lumina.crs_text

**References (Outgoing):**

- `crs_text_id` → `lumina.crs_text.crs_text_id`

**Referenced By (Incoming):**

- `lumina.crs_signature_text.crs_text_id` → `crs_text_id`
- `lumina.crs_text.crs_text_id` → `crs_text_id`

### lumina.currency_codes

**References (Outgoing):**

- `currency_code` → `lumina.currency_codes.currency_code`

**Referenced By (Incoming):**

- `lumina.account_location_header_5.currency_code` → `currency_code`
- `lumina.batch_record_1.currency_code` → `currency_code`
- `lumina.batch_record_1_gu4240.currency_code` → `currency_code`
- `lumina.batch_record_2.currency_code` → `currency_code`
- `lumina.currency_codes.currency_code` → `currency_code`
- `lumina.invoice_lines.currency_code` → `currency_code`
- `lumina.invoice_trail_entries.currency_code` → `currency_code`
- `lumina.invoices.currency_code` → `currency_code`
- `lumina.latest_repair_values.currency_code` → `currency_code`
- `lumina.maint_associated_costs.currency_code` → `currency_code`
- `lumina.maintenance_cost_invoices.currency_code` → `currency_code`
- `lumina.maintenance_cost_quotes.currency_code` → `currency_code`
- `lumina.material_pool_agreement.currency_code` → `currency_code`
- `lumina.oeim_invoice_snap_currencies.currency_code` → `currency_code`
- `lumina.order_goods_received_invoices.currency_code` → `currency_code`
- `lumina.order_header_1.currency_code` → `currency_code`
- `lumina.order_history.currency_code` → `currency_code`
- `lumina.order_line_quotes_data.currency_code` → `currency_code`
- `lumina.original_purchase_values.currency_code` → `currency_code`
- `lumina.preorders.currency_code` → `currency_code`
- `lumina.quotes_by_part.currency_code` → `currency_code`
- `lumina.requirement_recharge_details.currency_code` → `currency_code`
- `lumina.rfq_history.currency_code` → `currency_code`
- `lumina.rfq_quote_received.currency_code` → `currency_code`
- `lumina.sales_history.currency_code` → `currency_code`
- `lumina.sales_orders.currency_code` → `currency_code`
- `lumina.sales_prices.currency_code` → `currency_code`
- `lumina.sales_quotes_out_history.currency_code` → `currency_code`
- `lumina.sales_request_quote_header.currency_code` → `currency_code`
- `lumina.shipment.currency_code` → `currency_code`
- `lumina.strip_report_header_1.currency_code` → `currency_code`
- `lumina.transaction_log_icarus.currency_code` → `currency_code`
- `lumina.transaction_log_icarus_8134.currency_code` → `currency_code`
- `lumina.work_schedule_defect_4.currency_code` → `currency_code`

### lumina.customer_contract_rates

**References (Outgoing):**

- `cost_code` → `lumina.cost_codes.id`
- `contract_id` → `lumina.customer_contract_rates.contract_id`
- `time_category_id` → `lumina.maint_cost_time_category_set.category_set_id`

**Referenced By (Incoming):**

- `lumina.access_dim_sales_info.customer_code` → `contract_id`
- `lumina.account_location_header_9.customer_number` → `contract_id`
- `lumina.customer_contract_rates.contract_id` → `contract_id`
- `lumina.customer_contract_stop_incl.contract_id` → `contract_id`
- `lumina.customer_contracts.contract_id` → `contract_id`
- `lumina.maint_cost_time_categories.contract_id` → `contract_id`
- `lumina.time_categories.contract_id` → `contract_id`
- `lumina.works_order_contracts.contract_id` → `contract_id`

### lumina.customer_contract_stop_incl

**References (Outgoing):**

- `cost_code` → `lumina.cost_codes.id`
- `contract_id` → `lumina.customer_contract_rates.contract_id`
- `time_category_id` → `lumina.maint_cost_time_category_set.category_set_id`

### lumina.customer_contracts

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `contract_id` → `lumina.customer_contract_rates.contract_id`
- `markup_code` → `lumina.freight_cost_markups.freight_cost_markup_id`

### lumina.customer_sales_order_xref

**References (Outgoing):**

- `customer_sales_order_number` → `lumina.customer_sales_order_xref.customer_sales_order_number`
- `sales_order_number` → `lumina.customer_sales_order_xref.customer_sales_order_number`

**Referenced By (Incoming):**

- `lumina.access_dim_sales_info.sales_order_number` → `customer_sales_order_number`
- `lumina.customer_sales_order_xref.customer_sales_order_number` → `customer_sales_order_number`
- `lumina.customer_sales_order_xref.sales_order_number` → `customer_sales_order_number`
- `lumina.requirements.sales_order_number` → `customer_sales_order_number`
- `lumina.sales_invoices_xref.sales_order_number` → `customer_sales_order_number`
- `lumina.sales_order_dispatches.sales_order_number` → `customer_sales_order_number`
- `lumina.sales_order_lines.sales_order_number` → `customer_sales_order_number`
- `lumina.sales_order_notes.sales_order_number` → `customer_sales_order_number`
- `lumina.sales_order_payments.sales_order_number` → `customer_sales_order_number`
- `lumina.sales_orders.sales_order_number` → `customer_sales_order_number`
- `lumina.sales_orders_by_part.sales_order_number` → `customer_sales_order_number`
- `lumina.sales_request_quote_detail.sales_order_number` → `customer_sales_order_number`

### lumina.customs_status_codes

**References (Outgoing):**

- `reference_number` → `lumina.accounts_references.accounts_reference`

**Referenced By (Incoming):**

- `lumina.shipment_item_customs.customs_status_code` → `customs_status`

### lumina.customs_tariff_codes

**References (Outgoing):**

- `customs_tariff_code` → `lumina.customs_tariff_codes.customs_tariff_code`

**Referenced By (Incoming):**

- `lumina.customs_tariff_codes.customs_tariff_code` → `customs_tariff_code`
- `lumina.customs_tariff_codes_territory.customs_tariff_code` → `customs_tariff_code`
- `lumina.part_customs_tariff_territory.customs_tariff_code` → `customs_tariff_code`
- `lumina.parts_customs_tariff_codes.customs_tariff_code` → `customs_tariff_code`

### lumina.customs_tariff_codes_territory

**References (Outgoing):**

- `customs_tariff_code` → `lumina.customs_tariff_codes.customs_tariff_code`

### lumina.daily_loans_out

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.dataset_locks_by_lock_type

**References (Outgoing):**

- `user_id` → `lumina.dataset_locks_by_user.user_id`

### lumina.dataset_locks_by_user

**References (Outgoing):**

- `user_id` → `lumina.dataset_locks_by_user.user_id`

**Referenced By (Incoming):**

- `lumina.add_extension_permissions.user_id` → `user_id`
- `lumina.amp_revision_history.user_id` → `user_id`
- `lumina.amp_revisions.user_id` → `user_id`
- `lumina.amp_workcards_by_section.user_id` → `user_id`
- `lumina.audit_trail.user_id` → `user_id`
- `lumina.batch_history.user_id` → `user_id`
- `lumina.dataset_locks_by_lock_type.user_id` → `user_id`
- `lumina.dataset_locks_by_user.user_id` → `user_id`
- `lumina.float_history.user_id` → `user_id`
- `lumina.mel_revision_history.user_id` → `user_id`
- `lumina.mel_revisions.user_id` → `user_id`
- `lumina.part_number_amendment_history.user_id` → `user_id`
- `lumina.rdi_history.user_id` → `user_id`
- `lumina.repetitive_defect_narrative.user_id` → `user_id`
- `lumina.sales_order_payments.user_id` → `user_id`
- `lumina.sales_request_quote_header.user_id` → `user_id`
- `lumina.transaction_log_lasers.user_id` → `user_id`
- `lumina.transaction_log_trecs.user_id` → `user_id`
- `lumina.user_warehouse_access.user_id` → `user_id`
- `lumina.warranty_claims.user_id` → `user_id`
- `lumina.wcr_boeing_tb_revision.user_id` → `user_id`

### lumina.default_labour_rates

**References (Outgoing):**

- `cost_code` → `lumina.cost_codes.id`
- `window_id` → `lumina.default_labour_windows.window_id`
- `time_category_id` → `lumina.maint_cost_time_category_set.category_set_id`

### lumina.default_labour_windows

**References (Outgoing):**

- `window_id` → `lumina.default_labour_windows.window_id`

**Referenced By (Incoming):**

- `lumina.default_labour_rates.window_id` → `window_id`
- `lumina.default_labour_windows.window_id` → `window_id`

### lumina.defect_extensions

**References (Outgoing):**

- `extension_id` → `lumina.add_extension_permissions.user_id`
- `defect_id` → `lumina.defect_extensions.defect_id`

**Referenced By (Incoming):**

- `lumina.defect_extensions.defect_id` → `defect_id`
- `lumina.defect_stage_employees.defect_id` → `defect_id`
- `lumina.engineering_support_history.defect_number` → `defect_id`
- `lumina.maint_historic_defects.defect_id` → `defect_id`
- `lumina.nrc_defect_details.defect_id` → `defect_id`
- `lumina.nrc_defect_notes.defect_number` → `defect_id`
- `lumina.nrc_print_history.defect_number` → `defect_id`
- `lumina.nrc_rectification_notes.defect_number` → `defect_id`
- `lumina.nrc_requirements_actions.defect_number` → `defect_id`
- `lumina.nrc_status_history.defect_number` → `defect_id`
- `lumina.nrc_xref_to_scheduled_workcard.defect_number` → `defect_id`
- `lumina.oeim_invoice_snap_sfdc_book.defect_code` → `defect_id`
- `lumina.osys_defect_act_to_defect_id.defect_id` → `defect_id`
- `lumina.osys_defect_to_defect_id.defect_number` → `defect_id`
- `lumina.osys_defect_to_defect_id.defect_id` → `defect_id`
- `lumina.osys_defect_to_tech_log_line.defect_number` → `defect_id`
- `lumina.requirements.defect_number` → `defect_id`
- `lumina.requirements.defect_id` → `defect_id`
- `lumina.sfdc_bookings.defect_code` → `defect_id`
- `lumina.sfdc_deleted_bookings.defect_code` → `defect_id`
- `lumina.sfdc_open_bookings.defect_code` → `defect_id`
- `lumina.sold_hours_history.defect_number` → `defect_id`
- `lumina.structural_damage.defect_number` → `defect_id`
- `lumina.tech_log_3.defect_id` → `defect_id`
- `lumina.work_sch_def_2_lg318.defect_number` → `defect_id`
- `lumina.work_schedule_defect_1.defect_number` → `defect_id`
- `lumina.work_schedule_defect_2.defect_number` → `defect_id`
- `lumina.work_schedule_defect_3.defect_number` → `defect_id`
- `lumina.work_schedule_defect_4.defect_number` → `defect_id`

### lumina.defect_maint_stages

**References (Outgoing):**

- `defect_stage_id` → `lumina.defect_stage_employees.defect_id`

### lumina.defect_stage_employees

**References (Outgoing):**

- `defect_id` → `lumina.defect_extensions.defect_id`
- `defect_stage_id` → `lumina.defect_stage_employees.defect_id`
- `employee_id` → `lumina.defect_stage_employees.defect_id`
- `licence_id` → `lumina.email_licence.license_id`

**Referenced By (Incoming):**

- `lumina.defect_maint_stages.defect_stage_id` → `defect_id`
- `lumina.defect_stage_employees.defect_stage_id` → `defect_id`
- `lumina.defect_stage_employees.employee_id` → `defect_id`
- `lumina.employee_experience_details.employee_number` → `defect_id`
- `lumina.employee_presence.employee_number` → `defect_id`
- `lumina.employee_presence_log.employee_number` → `defect_id`
- `lumina.employee_training_details.employee_number` → `defect_id`
- `lumina.employees.employee_number` → `defect_id`
- `lumina.employees_licences.employee_number` → `defect_id`
- `lumina.oeim_invoice_snap_employees.employee_number` → `defect_id`
- `lumina.oeim_invoice_snap_sfdc_book.employee_number` → `defect_id`
- `lumina.order_header_4.employee_number` → `defect_id`
- `lumina.preorders.employee_number` → `defect_id`
- `lumina.rp_employee_allocation_header.employee_number` → `defect_id`
- `lumina.rp_employee_calendar_addition.employee_number` → `defect_id`
- `lumina.rp_employee_calendar_pattern.employee_number` → `defect_id`
- `lumina.sfdc_activity.defect_stage_id` → `defect_id`
- `lumina.sfdc_bookings.employee_number` → `defect_id`
- `lumina.sfdc_deleted_bookings.employee_number` → `defect_id`
- `lumina.sfdc_open_bookings.employee_number` → `defect_id`
- `lumina.tool_check_out_in.employee_number` → `defect_id`
- `lumina.tool_check_out_in_duplicates.employee_number` → `defect_id`
- `lumina.wo_releases.employee_number` → `defect_id`
- `lumina.work_schedule_defect_3.employee_number` → `defect_id`

### lumina.deferred_defect_xref_to_cfd_no

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.delay_codes

**References (Outgoing):**

- `delay_code_id` → `lumina.delay_codes.delay_code_id`
- `delay_code` → `lumina.delay_codes.delay_code_id`

**Referenced By (Incoming):**

- `lumina.delay_codes.delay_code_id` → `delay_code_id`
- `lumina.delay_codes.delay_code` → `delay_code_id`
- `lumina.delays.delay_id` → `delay_code_id`
- `lumina.delays.delay_code_id` → `delay_code_id`

### lumina.delays

**References (Outgoing):**

- `report_id` → `lumina.amp_report_documents.fleet`
- `delay_id` → `lumina.delay_codes.delay_code_id`
- `delay_code_id` → `lumina.delay_codes.delay_code_id`

### lumina.delivery_note_extended_remarks

**References (Outgoing):**

- `delivery_note_number` → `lumina.delivery_note_extended_remarks.delivery_note_number`

**Referenced By (Incoming):**

- `lumina.airway_bill_references.delivery_note_number` → `delivery_note_number`
- `lumina.delivery_note_extended_remarks.delivery_note_number` → `delivery_note_number`
- `lumina.delivery_note_header_1.delivery_note_number` → `delivery_note_number`
- `lumina.delivery_note_header_2.delivery_note_number` → `delivery_note_number`
- `lumina.delivery_note_header_3.delivery_note_number` → `delivery_note_number`
- `lumina.delivery_note_header_4.delivery_note_number` → `delivery_note_number`
- `lumina.delivery_note_item_header_1.delivery_note_number` → `delivery_note_number`
- `lumina.delivery_note_item_header_2.delivery_note_number` → `delivery_note_number`
- `lumina.delivery_note_master_list.delivery_note_number` → `delivery_note_number`
- `lumina.monthly_loans_out.delivery_note_number` → `delivery_note_number`
- `lumina.order_header_3.delivery_note_number` → `delivery_note_number`
- `lumina.rotable_history.delivery_note_number` → `delivery_note_number`
- `lumina.sales_order_dispatches.delivery_note_number` → `delivery_note_number`
- `lumina.transaction_log_icarus.delivery_note_number` → `delivery_note_number`
- `lumina.transaction_log_icarus_8134.delivery_note_number` → `delivery_note_number`

### lumina.delivery_note_header_1

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `order_number` → `lumina.batch_orders.batch_number`
- `company_code` → `lumina.company_codes.company_code`
- `delivery_note_number` → `lumina.delivery_note_extended_remarks.delivery_note_number`

### lumina.delivery_note_header_2

**References (Outgoing):**

- `delivery_note_number` → `lumina.delivery_note_extended_remarks.delivery_note_number`

### lumina.delivery_note_header_3

**References (Outgoing):**

- `delivery_note_number` → `lumina.delivery_note_extended_remarks.delivery_note_number`

### lumina.delivery_note_header_4

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `delivery_note_number` → `lumina.delivery_note_extended_remarks.delivery_note_number`

### lumina.delivery_note_item_header_1

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `delivery_note_number` → `lumina.delivery_note_extended_remarks.delivery_note_number`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`

**Referenced By (Incoming):**

- `lumina.dues_register.item_number` → `delivery_note_number`
- `lumina.maint_cost_budget_adsb.item_id` → `delivery_note_number`
- `lumina.maint_cost_budget_cfds.item_id` → `delivery_note_number`
- `lumina.maint_cost_budget_costs.item_id` → `delivery_note_number`
- `lumina.maint_cost_budget_labour_ests.item_id` → `delivery_note_number`
- `lumina.maint_cost_budget_materials.item_id` → `delivery_note_number`
- `lumina.maint_cost_budget_packages.item_id` → `delivery_note_number`
- `lumina.maint_cost_budget_visits.item_id` → `delivery_note_number`
- `lumina.maint_cost_budget_workcards.item_id` → `delivery_note_number`
- `lumina.package_items.item_id` → `delivery_note_number`
- `lumina.shipment_item_demands.item_id` → `delivery_note_number`

### lumina.delivery_note_item_header_2

**References (Outgoing):**

- `pick_number` → `lumina.condition_pick_table.part_number`
- `delivery_note_number` → `lumina.delivery_note_extended_remarks.delivery_note_number`

### lumina.delivery_note_master_list

**References (Outgoing):**

- `delivery_note_number` → `lumina.delivery_note_extended_remarks.delivery_note_number`

### lumina.demand_reason_to_movement_code

**References (Outgoing):**

- `movement_code` → `lumina.component_movement_hist_life.part_number`
- `reason_id` → `lumina.demand_reason_to_movement_code.id`

**Referenced By (Incoming):**

- `lumina.demand_reason_to_movement_code.reason_id` → `id`
- `lumina.shipment_demands.reason_id` → `id`
- `lumina.shipment_item_demands.demand_id` → `id`
- `lumina.shipment_order_demands.demand_id` → `id`
- `lumina.shipment_requirement_demands.demand_id` → `id`
- `lumina.shipment_stocktransfer_demands.demand_id` → `id`
- `lumina.shipment_works_orders_demands.demand_id` → `id`

### lumina.departments

**References (Outgoing):**

- `department_id` → `lumina.departments.department_id`
- `export_code` → `lumina.export_codes.export_id`

**Referenced By (Incoming):**

- `lumina.departments.department_id` → `department_id`
- `lumina.oeim_invoice_snap_departments.department_id` → `department_id`

### lumina.dmg_rpr_action_taken_details

**References (Outgoing):**

- `action_taken_id` → `lumina.dmg_rpr_action_taken_details.action_taken_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_action_taken_details.action_taken_id` → `action_taken_id`

### lumina.dmg_rpr_attachments

**References (Outgoing):**

- `damage_id` → `lumina.dmg_rpr_damage.damage_id`
- `document_image_id` → `lumina.document_image_source.document_image_source_id`

### lumina.dmg_rpr_ca_approval_details

**References (Outgoing):**

- `ca_approval_id` → `lumina.dmg_rpr_ca_approval_details.ca_approval_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_ca_approval_details.ca_approval_id` → `ca_approval_id`

### lumina.dmg_rpr_corrosion_levels

**References (Outgoing):**

- `corrosion_level_id` → `lumina.dmg_rpr_corrosion_levels.corrosion_level_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_corrosion_levels.corrosion_level_id` → `corrosion_level_id`

### lumina.dmg_rpr_damage

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `section_id` → `lumina.amp_workcard_sections.section_id`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `damage_id` → `lumina.dmg_rpr_damage.damage_id`
- `damage_type_id` → `lumina.dmg_rpr_damage_types.damage_type_id`
- `zone_code` → `lumina.dmg_rpr_measurement_zones.measurement_zone_id`

**Referenced By (Incoming):**

- `lumina.accomp_hist_delta_1763.damage_id` → `damage_id`
- `lumina.accomplishment_history.damage_id` → `damage_id`
- `lumina.dmg_rpr_attachments.damage_id` → `damage_id`
- `lumina.dmg_rpr_damage.damage_id` → `damage_id`
- `lumina.dmg_rpr_damage_numbering.damage_id` → `damage_id`
- `lumina.dmg_rpr_damage_numbering.damage_number` → `damage_id`
- `lumina.dmg_rpr_dmg_2d_position_labels.damage_id` → `damage_id`
- `lumina.dmg_rpr_dmg_2d_positions.damage_id` → `damage_id`
- `lumina.dmg_rpr_fitted_locations.damage_id` → `damage_id`
- `lumina.dmg_rpr_inspections.damage_id` → `damage_id`
- `lumina.dmg_rpr_interim_repairs.damage_id` → `damage_id`
- `lumina.dmg_rpr_location.damage_id` → `damage_id`
- `lumina.dmg_rpr_location_measurement.damage_id` → `damage_id`
- `lumina.dmg_rpr_permanent_repairs.damage_id` → `damage_id`
- `lumina.dmg_rpr_repair_req_details.damage_id` → `damage_id`
- `lumina.dmg_rpr_time_limited_repairs.damage_id` → `damage_id`

### lumina.dmg_rpr_damage_numbering

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `damage_id` → `lumina.dmg_rpr_damage.damage_id`
- `damage_number` → `lumina.dmg_rpr_damage.damage_id`

### lumina.dmg_rpr_damage_types

**References (Outgoing):**

- `damage_type_id` → `lumina.dmg_rpr_damage_types.damage_type_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_damage.damage_type_id` → `damage_type_id`
- `lumina.dmg_rpr_damage_types.damage_type_id` → `damage_type_id`

### lumina.dmg_rpr_dmg_2d_position_labels

**References (Outgoing):**

- `damage_id` → `lumina.dmg_rpr_damage.damage_id`
- `label_id` → `lumina.dmg_rpr_dmg_2d_position_labels.label_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_dmg_2d_position_labels.label_id` → `label_id`
- `lumina.dmg_rpr_dmg_2d_positions.position_id` → `label_id`
- `lumina.dmg_rpr_location.position_id` → `label_id`

### lumina.dmg_rpr_dmg_2d_positions

**References (Outgoing):**

- `damage_id` → `lumina.dmg_rpr_damage.damage_id`
- `position_id` → `lumina.dmg_rpr_dmg_2d_position_labels.label_id`

### lumina.dmg_rpr_doc_effectivity

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `fleet_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `dmg_rpr_doc_effectivity_id` → `lumina.dmg_rpr_doc_effectivity.dmg_rpr_doc_effectivity_id`
- `sub_fleet_id` → `lumina.sub_fleet_header.sub_fleet_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_doc_effectivity.dmg_rpr_doc_effectivity_id` → `dmg_rpr_doc_effectivity_id`

### lumina.dmg_rpr_doc_subject

**References (Outgoing):**

- `subject_id` → `lumina.dmg_rpr_doc_subject.subject_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_doc_subject.subject_id` → `subject_id`
- `lumina.dmg_rpr_documents.subject_id` → `subject_id`
- `lumina.dmg_rpr_subject_sections.subject_id` → `subject_id`
- `lumina.dmg_rpr_subject_zones.subject_id` → `subject_id`

### lumina.dmg_rpr_document_order

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `fleet_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `order_number` → `lumina.batch_orders.batch_number`
- `sub_fleet_id` → `lumina.sub_fleet_header.sub_fleet_id`

### lumina.dmg_rpr_documents

**References (Outgoing):**

- `subject_id` → `lumina.dmg_rpr_doc_subject.subject_id`
- `document_image_id` → `lumina.document_image_source.document_image_source_id`

### lumina.dmg_rpr_fitted_locations

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `damage_id` → `lumina.dmg_rpr_damage.damage_id`

### lumina.dmg_rpr_idnt_inspect

**References (Outgoing):**

- `inspection_id` → `lumina.dmg_rpr_inspection_type_dtls.inspection_type_id`

### lumina.dmg_rpr_idnt_inspect_info

**References (Outgoing):**

- `inspection_id` → `lumina.dmg_rpr_inspection_type_dtls.inspection_type_id`

### lumina.dmg_rpr_inspection_type_dtls

**References (Outgoing):**

- `inspection_type_id` → `lumina.dmg_rpr_inspection_type_dtls.inspection_type_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_idnt_inspect.inspection_id` → `inspection_type_id`
- `lumina.dmg_rpr_idnt_inspect_info.inspection_id` → `inspection_type_id`
- `lumina.dmg_rpr_inspection_type_dtls.inspection_type_id` → `inspection_type_id`
- `lumina.dmg_rpr_inspections.inspection_id` → `inspection_type_id`
- `lumina.dmg_rpr_inspections.inspection_type_id` → `inspection_type_id`
- `lumina.dmg_rpr_stages.inspection_id` → `inspection_type_id`

### lumina.dmg_rpr_inspections

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `damage_id` → `lumina.dmg_rpr_damage.damage_id`
- `inspection_id` → `lumina.dmg_rpr_inspection_type_dtls.inspection_type_id`
- `inspection_type_id` → `lumina.dmg_rpr_inspection_type_dtls.inspection_type_id`
- `interim_repair_id` → `lumina.dmg_rpr_interim_repairs.interim_repair_id`
- `time_limited_repair_id` → `lumina.dmg_rpr_time_limited_repairs.time_limited_repair_id`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `paragraph_id` → `lumina.paragraph_cancels.rfc_id`
- `frequency_id` → `lumina.rfc_frequency_phase_header.rfc_id`

### lumina.dmg_rpr_interim_repairs

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `damage_id` → `lumina.dmg_rpr_damage.damage_id`
- `interim_repair_id` → `lumina.dmg_rpr_interim_repairs.interim_repair_id`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `paragraph_id` → `lumina.paragraph_cancels.rfc_id`
- `frequency_id` → `lumina.rfc_frequency_phase_header.rfc_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_inspections.interim_repair_id` → `interim_repair_id`
- `lumina.dmg_rpr_interim_repairs.interim_repair_id` → `interim_repair_id`
- `lumina.dmg_rpr_stages.interim_repair_id` → `interim_repair_id`

### lumina.dmg_rpr_location

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `damage_id` → `lumina.dmg_rpr_damage.damage_id`
- `position_id` → `lumina.dmg_rpr_dmg_2d_position_labels.label_id`
- `material_type_id` → `lumina.dmg_rpr_material_types_dtls.material_type_id`
- `surface_finish_id` → `lumina.dmg_rpr_surface_finish_details.surface_finish_id`

### lumina.dmg_rpr_location_measurement

**References (Outgoing):**

- `damage_id` → `lumina.dmg_rpr_damage.damage_id`
- `measurement_id` → `lumina.dmg_rpr_location_measurement.damage_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_location_measurement.measurement_id` → `damage_id`
- `lumina.dmg_rpr_measurement_sections.measurement_id` → `damage_id`
- `lumina.dmg_rpr_measurement_zones.measurement_id` → `damage_id`
- `lumina.dmg_rpr_measurements.measurement_id` → `damage_id`

### lumina.dmg_rpr_mat_types_fld_dtls

**References (Outgoing):**

- `material_type_id` → `lumina.dmg_rpr_material_types_dtls.material_type_id`

### lumina.dmg_rpr_material_types_dtls

**References (Outgoing):**

- `material_type_id` → `lumina.dmg_rpr_material_types_dtls.material_type_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_location.material_type_id` → `material_type_id`
- `lumina.dmg_rpr_mat_types_fld_dtls.material_type_id` → `material_type_id`
- `lumina.dmg_rpr_material_types_dtls.material_type_id` → `material_type_id`

### lumina.dmg_rpr_measurement_sections

**References (Outgoing):**

- `section_id` → `lumina.amp_workcard_sections.section_id`
- `measurement_id` → `lumina.dmg_rpr_location_measurement.damage_id`
- `measurement_section_id` → `lumina.dmg_rpr_measurement_sections.measurement_section_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_measurement_sections.measurement_section_id` → `measurement_section_id`

### lumina.dmg_rpr_measurement_zones

**References (Outgoing):**

- `measurement_id` → `lumina.dmg_rpr_location_measurement.damage_id`
- `measurement_zone_id` → `lumina.dmg_rpr_measurement_zones.measurement_zone_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_damage.zone_code` → `measurement_zone_id`
- `lumina.dmg_rpr_measurement_zones.measurement_zone_id` → `measurement_zone_id`
- `lumina.wcr_temp_base1.zone_code` → `measurement_zone_id`

### lumina.dmg_rpr_measurements

**References (Outgoing):**

- `measurement_id` → `lumina.dmg_rpr_location_measurement.damage_id`

### lumina.dmg_rpr_permanent_repairs

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `repair_id` → `lumina.consumable_repair_xref_to_part.part_number`
- `damage_id` → `lumina.dmg_rpr_damage.damage_id`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `paragraph_id` → `lumina.paragraph_cancels.rfc_id`
- `frequency_id` → `lumina.rfc_frequency_phase_header.rfc_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_stages.permanent_repair_id` → `repair_id`

### lumina.dmg_rpr_repair_req_details

**References (Outgoing):**

- `damage_id` → `lumina.dmg_rpr_damage.damage_id`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`

### lumina.dmg_rpr_section_details

**References (Outgoing):**

- `section_id` → `lumina.amp_workcard_sections.section_id`

### lumina.dmg_rpr_section_fleet_details

**References (Outgoing):**

- `section_id` → `lumina.amp_workcard_sections.section_id`

### lumina.dmg_rpr_stage_limits

**References (Outgoing):**

- `limit_id` → `lumina.amp_component_intervals_limits.component_interval_id`
- `stage_id` → `lumina.amp_component_intervals_stages.component_interval_id`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

### lumina.dmg_rpr_stages

**References (Outgoing):**

- `stage_id` → `lumina.amp_component_intervals_stages.component_interval_id`
- `inspection_id` → `lumina.dmg_rpr_inspection_type_dtls.inspection_type_id`
- `interim_repair_id` → `lumina.dmg_rpr_interim_repairs.interim_repair_id`
- `permanent_repair_id` → `lumina.dmg_rpr_permanent_repairs.repair_id`
- `time_limited_repair_id` → `lumina.dmg_rpr_time_limited_repairs.time_limited_repair_id`

### lumina.dmg_rpr_subject_sections

**References (Outgoing):**

- `section_id` → `lumina.amp_workcard_sections.section_id`
- `subject_id` → `lumina.dmg_rpr_doc_subject.subject_id`
- `subject_section_id` → `lumina.dmg_rpr_subject_sections.subject_section_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_subject_sections.subject_section_id` → `subject_section_id`

### lumina.dmg_rpr_subject_zones

**References (Outgoing):**

- `subject_id` → `lumina.dmg_rpr_doc_subject.subject_id`
- `subject_zone_id` → `lumina.dmg_rpr_subject_zones.subject_zone_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_subject_zones.subject_zone_id` → `subject_zone_id`

### lumina.dmg_rpr_surface_finish_details

**References (Outgoing):**

- `surface_finish_id` → `lumina.dmg_rpr_surface_finish_details.surface_finish_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_location.surface_finish_id` → `surface_finish_id`
- `lumina.dmg_rpr_surface_finish_details.surface_finish_id` → `surface_finish_id`

### lumina.dmg_rpr_time_limited_repairs

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `damage_id` → `lumina.dmg_rpr_damage.damage_id`
- `time_limited_repair_id` → `lumina.dmg_rpr_time_limited_repairs.time_limited_repair_id`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `paragraph_id` → `lumina.paragraph_cancels.rfc_id`
- `frequency_id` → `lumina.rfc_frequency_phase_header.rfc_id`

**Referenced By (Incoming):**

- `lumina.dmg_rpr_inspections.time_limited_repair_id` → `time_limited_repair_id`
- `lumina.dmg_rpr_stages.time_limited_repair_id` → `time_limited_repair_id`
- `lumina.dmg_rpr_time_limited_repairs.time_limited_repair_id` → `time_limited_repair_id`

### lumina.document_classes

**References (Outgoing):**

- `document_id` → `lumina.aircraft_documents.aircraft_document_id`

**Referenced By (Incoming):**

- `lumina.drn_class_codes.class_code` → `document_id`
- `lumina.drn_fleet_ata.class_code` → `document_id`
- `lumina.drn_maint_mod.class_code` → `document_id`
- `lumina.drn_maintenance_history.class_code` → `document_id`
- `lumina.drn_mod_desc_order_hist.class_code` → `document_id`
- `lumina.drn_modification_history.class_code` → `document_id`
- `lumina.drn_part_serial.class_code` → `document_id`
- `lumina.fleet_forecast_plans.class_code` → `document_id`
- `lumina.forecast_cache.class_code` → `document_id`
- `lumina.uf_forecast_cache.class_code` → `document_id`

### lumina.document_image_source

**References (Outgoing):**

- `document_image_source_id` → `lumina.document_image_source.document_image_source_id`

**Referenced By (Incoming):**

- `lumina.accomp_hist_delta_1763.document_image_id` → `document_image_source_id`
- `lumina.accomplishment_history.document_image_id` → `document_image_source_id`
- `lumina.aircraft_documents.document_image_id` → `document_image_source_id`
- `lumina.amp_report_documents.document_image_id` → `document_image_source_id`
- `lumina.cq_documents.document_image_id` → `document_image_source_id`
- `lumina.dmg_rpr_attachments.document_image_id` → `document_image_source_id`
- `lumina.dmg_rpr_documents.document_image_id` → `document_image_source_id`
- `lumina.document_image_source.document_image_source_id` → `document_image_source_id`
- `lumina.document_image_types.document_image_source_id` → `document_image_source_id`
- `lumina.document_images.document_image_id` → `document_image_source_id`
- `lumina.document_images_jn.document_image_id` → `document_image_source_id`
- `lumina.employees_licences.document_image_id` → `document_image_source_id`
- `lumina.goods_received_sheet_document.document_image_id` → `document_image_source_id`
- `lumina.nrc_documents.document_image_id` → `document_image_source_id`
- `lumina.part_serial_documents.document_image_id` → `document_image_source_id`
- `lumina.reliability_report_logo_desc.document_image_id` → `document_image_source_id`
- `lumina.requirement_source_codes.source_code` → `document_image_source_id`
- `lumina.rfc_documents.document_image_id` → `document_image_source_id`
- `lumina.shipment_documents.document_image_id` → `document_image_source_id`
- `lumina.stock_documents.document_image_id` → `document_image_source_id`
- `lumina.strip_documents.document_image_id` → `document_image_source_id`
- `lumina.tech_log_documents.document_image_id` → `document_image_source_id`
- `lumina.warranty_terms_documents.document_image_id` → `document_image_source_id`
- `lumina.weight_and_balance_documents.document_image_id` → `document_image_source_id`
- `lumina.workcard_properties.document_image_id` → `document_image_source_id`
- `lumina.works_order_documents.document_image_id` → `document_image_source_id`

### lumina.document_image_types

**References (Outgoing):**

- `document_image_source_id` → `lumina.document_image_source.document_image_source_id`

### lumina.document_images

**References (Outgoing):**

- `document_image_id` → `lumina.document_image_source.document_image_source_id`

### lumina.document_images_jn

**References (Outgoing):**

- `document_image_id` → `lumina.document_image_source.document_image_source_id`

### lumina.drn_class_codes

**References (Outgoing):**

- `class_code` → `lumina.document_classes.document_id`

### lumina.drn_component_mods_history

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `report_id` → `lumina.amp_report_documents.fleet`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.drn_components_nsbl_history

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

### lumina.drn_cycles

**References (Outgoing):**

- `cycle_number` → `lumina.accum_cycles_static_data.parent_part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

**Referenced By (Incoming):**

- `lumina.drn_maint_mod.drn_cycle_number` → `fleet`

### lumina.drn_fleet_ata

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `class_code` → `lumina.document_classes.document_id`

### lumina.drn_life_limits

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

### lumina.drn_maint_mod

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `class_code` → `lumina.document_classes.document_id`
- `drn_cycle_number` → `lumina.drn_cycles.fleet`

### lumina.drn_maint_mod_notes

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.drn_maintenance_history

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `report_id` → `lumina.amp_report_documents.fleet`
- `class_code` → `lumina.document_classes.document_id`

### lumina.drn_maintenance_history_notes

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.drn_mod_desc_order_hist

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `class_code` → `lumina.document_classes.document_id`

### lumina.drn_modification_history

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `report_id` → `lumina.amp_report_documents.fleet`
- `class_code` → `lumina.document_classes.document_id`

### lumina.drn_modification_history_notes

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.drn_part_serial

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `class_code` → `lumina.document_classes.document_id`

### lumina.dues_register

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `item_number` → `lumina.delivery_note_item_header_1.delivery_note_number`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`

### lumina.dummy_part_numbers

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.easa_trace

**References (Outgoing):**

- `trace_id` → `lumina.easa_trace.trace_id`

**Referenced By (Incoming):**

- `lumina.easa_trace.trace_id` → `trace_id`
- `lumina.sabre_trace.trace_id` → `trace_id`

### lumina.economic_blocks

**References (Outgoing):**

- `block_code` → `lumina.block_countries.block_code`

### lumina.email_licence

**Referenced By (Incoming):**

- `lumina.defect_stage_employees.licence_id` → `license_id`
- `lumina.employees_licences.licence_id` → `license_id`
- `lumina.licence_categories.licence_id` → `license_id`
- `lumina.sfdc_activity.licence_id` → `license_id`
- `lumina.works_orders.licence_id` → `license_id`

### lumina.email_notification

**References (Outgoing):**

- `category_id` → `lumina.maint_cost_time_category_set.category_set_id`

**Referenced By (Incoming):**

- `lumina.security_user_notifications.notification_id` → `id`

### lumina.email_notification_categories

**References (Outgoing):**

- `category_id` → `lumina.maint_cost_time_category_set.category_set_id`

**Referenced By (Incoming):**

- `lumina.measurement_alerts_aircraft.email_notification_cat_id` → `category_id`
- `lumina.measurement_alerts_fleet.email_notification_cat_id` → `category_id`

### lumina.email_template

**References (Outgoing):**

- `template_id` → `lumina.email_template.template_id`

**Referenced By (Incoming):**

- `lumina.email_template.template_id` → `template_id`
- `lumina.jasper_workcard_templates.template_id` → `template_id`

### lumina.employee_experience_details

**References (Outgoing):**

- `employee_number` → `lumina.defect_stage_employees.defect_id`
- `experience_id` → `lumina.employee_experience_details.experience_id`

**Referenced By (Incoming):**

- `lumina.employee_experience_details.experience_id` → `experience_id`

### lumina.employee_presence

**References (Outgoing):**

- `employee_number` → `lumina.defect_stage_employees.defect_id`

### lumina.employee_presence_log

**References (Outgoing):**

- `task_number` → `lumina.amp_datmig_comp_task_lookup.fleet`
- `employee_number` → `lumina.defect_stage_employees.defect_id`

### lumina.employee_training_details

**References (Outgoing):**

- `employee_number` → `lumina.defect_stage_employees.defect_id`
- `training_id` → `lumina.employee_training_details.employee_number`

**Referenced By (Incoming):**

- `lumina.employee_training_details.training_id` → `employee_number`
- `lumina.training_details.training_id` → `employee_number`

### lumina.employees

**References (Outgoing):**

- `employee_number` → `lumina.defect_stage_employees.defect_id`
- `trade_code` → `lumina.trades.trade_code`

### lumina.employees_licences

**References (Outgoing):**

- `employee_number` → `lumina.defect_stage_employees.defect_id`
- `document_image_id` → `lumina.document_image_source.document_image_source_id`
- `licence_id` → `lumina.email_licence.license_id`
- `scope_type_id` → `lumina.scope_type_rating.scope_type_id`

### lumina.end_use_codes

**References (Outgoing):**

- `end_use_code` → `lumina.end_use_codes.end_use_code`

**Referenced By (Incoming):**

- `lumina.account_location_header_9.end_use_number` → `end_use_code`
- `lumina.end_use_codes.end_use_code` → `end_use_code`
- `lumina.sales_invoice_genled_xref.end_use_code` → `end_use_code`
- `lumina.stock_group_additional_data.end_use_code` → `end_use_code`

### lumina.engineering_support_history

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `defect_number` → `lumina.defect_extensions.defect_id`
- `engineering_support_history_id` → `lumina.engineering_support_history.engineering_support_history_id`

**Referenced By (Incoming):**

- `lumina.engineering_support_history.engineering_support_history_id` → `engineering_support_history_id`

### lumina.engineering_support_status

**Referenced By (Incoming):**

- `lumina.work_schedule_defect_4.engineering_support_status_id` → `engineering_status_id`

### lumina.esign_off_nrc

**References (Outgoing):**

- `document_id` → `lumina.aircraft_documents.aircraft_document_id`
- `nrc_number` → `lumina.cq_quote_nrc_access_panels.quote_id`

### lumina.export_codes

**References (Outgoing):**

- `export_id` → `lumina.export_codes.export_id`
- `export_code` → `lumina.export_codes.export_id`

**Referenced By (Incoming):**

- `lumina.departments.export_code` → `export_id`
- `lumina.export_codes.export_id` → `export_id`
- `lumina.export_codes.export_code` → `export_id`
- `lumina.oeim_invoice_snap_departments.export_code` → `export_id`
- `lumina.oeim_invoice_snap_vat_codes.export_id` → `export_id`
- `lumina.vat_codes.export_id` → `export_id`

### lumina.extended_part_descriptions

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.extensions

**References (Outgoing):**

- `extension_id` → `lumina.add_extension_permissions.user_id`

### lumina.fixed_charges

**References (Outgoing):**

- `cost_code` → `lumina.cost_codes.id`

### lumina.fleet_assembles

**References (Outgoing):**

- `fleet_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`

### lumina.fleet_chap_part_header_1

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `alternate_part_number` → `lumina.alternate_parts.part_number`

### lumina.fleet_chap_part_header_2

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.fleet_chap_part_header_3

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.fleet_chapter_part_aircraft

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.fleet_forecast_plans

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `plan_id` → `lumina.amp_planning_notes.fleet_code`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `class_code` → `lumina.document_classes.document_id`

### lumina.fleet_forecast_plans_amp

**References (Outgoing):**

- `package_codes` → `lumina.amp_packages.fleet`
- `plan_id` → `lumina.amp_planning_notes.fleet_code`
- `visit_codes` → `lumina.amp_visits.fleet`
- `workcard_numbers` → `lumina.amp_workcards_by_package.fleet`

### lumina.fleet_forecast_plans_drn

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `plan_id` → `lumina.amp_planning_notes.fleet_code`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.fleet_forecast_plans_rfc

**References (Outgoing):**

- `plan_id` → `lumina.amp_planning_notes.fleet_code`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`

**Referenced By (Incoming):**

- `lumina.accomp_bkup.rfc_id` → `plan_id`
- `lumina.accomp_hist_delta_1763.rfc_id` → `plan_id`
- `lumina.accomp_hist_lost_sched.rfc_id` → `plan_id`
- `lumina.accomplishment_history.rfc_id` → `plan_id`
- `lumina.dmg_rpr_inspections.rfc_id` → `plan_id`
- `lumina.dmg_rpr_interim_repairs.rfc_id` → `plan_id`
- `lumina.dmg_rpr_permanent_repairs.rfc_id` → `plan_id`
- `lumina.dmg_rpr_time_limited_repairs.rfc_id` → `plan_id`
- `lumina.fleet_forecast_plans_rfc.rfc_id` → `plan_id`
- `lumina.forecast_cache.rfc_id` → `plan_id`
- `lumina.maint_cost_budget_adsb.rfc_id` → `plan_id`
- `lumina.paragraph_cancels.rfc_id` → `plan_id`
- `lumina.planners_notes_xref.rfc_id` → `plan_id`
- `lumina.rfc_aircraft.rfc_id` → `plan_id`
- `lumina.rfc_components.rfc_id` → `plan_id`
- `lumina.rfc_documents.rfc_id` → `plan_id`
- `lumina.rfc_effectivity_ata.rfc_id` → `plan_id`
- `lumina.rfc_effectivity_fleet.rfc_id` → `plan_id`
- `lumina.rfc_effectivity_part.rfc_id` → `plan_id`
- `lumina.rfc_evaluation_history.rfc_id` → `plan_id`
- `lumina.rfc_frequency_phase_header.rfc_id` → `plan_id`
- `lumina.rfc_frequency_phase_limits.rfc_id` → `plan_id`
- `lumina.rfc_frequency_phases.rfc_id` → `plan_id`
- `lumina.rfc_header.rfc_id` → `plan_id`
- `lumina.rfc_header_publications.rfc_id` → `plan_id`
- `lumina.rfc_paragraphs.rfc_id` → `plan_id`
- `lumina.rfc_print_history_log.rfc_id` → `plan_id`
- `lumina.rfc_relationships.rfc_id` → `plan_id`
- `lumina.rfc_transaction_log.rfc_id` → `plan_id`
- `lumina.schedule_forecast_xref.rfc_id` → `plan_id`
- `lumina.schedule_source.rfc_id` → `plan_id`
- `lumina.temp_rfc_paragraphs.rfc_id` → `plan_id`
- `lumina.uf_forecast_cache.rfc_id` → `plan_id`

### lumina.fleet_header_2

**References (Outgoing):**

- `mel_revision_number` → `lumina.mel_revision_history.history_id`

### lumina.fleet_statistics

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`

### lumina.float_history

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `user_id` → `lumina.dataset_locks_by_user.user_id`

### lumina.flown_sectors

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `flight_number` → `lumina.aircraft_flight_hours_1.aircraft_code`
- `report_id` → `lumina.amp_report_documents.fleet`
- `sector_id` → `lumina.flown_sectors.aircraft_code`

**Referenced By (Incoming):**

- `lumina.flown_sectors.sector_id` → `aircraft_code`
- `lumina.flown_sectors_bkp.sector_id` → `aircraft_code`
- `lumina.flown_sectors_con_680.sector_id` → `aircraft_code`
- `lumina.flown_sectors_delta1817.sector_id` → `aircraft_code`
- `lumina.sectors.sector_id` → `aircraft_code`

### lumina.flown_sectors_bkp

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `flight_number` → `lumina.aircraft_flight_hours_1.aircraft_code`
- `report_id` → `lumina.amp_report_documents.fleet`
- `sector_id` → `lumina.flown_sectors.aircraft_code`

### lumina.flown_sectors_con_680

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `flight_number` → `lumina.aircraft_flight_hours_1.aircraft_code`
- `report_id` → `lumina.amp_report_documents.fleet`
- `sector_id` → `lumina.flown_sectors.aircraft_code`

### lumina.flown_sectors_delta1817

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `flight_number` → `lumina.aircraft_flight_hours_1.aircraft_code`
- `report_id` → `lumina.amp_report_documents.fleet`
- `sector_id` → `lumina.flown_sectors.aircraft_code`

### lumina.forecast_cache

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `alert_number` → `lumina.alert_colors.alert_type_id`
- `workcard_code` → `lumina.amp_access_panels_by_workcard.fleet`
- `visit_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `workcard_interval_id` → `lumina.amp_workcard_intervals.workcard_interval_id`
- `component_life_limit_id` → `lumina.component_life_limits.component_life_limit_id`
- `works_order_number` → `lumina.credit_works_order_cards.credit_note_no`
- `class_code` → `lumina.document_classes.document_id`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`

### lumina.forecast_cache_ac_details

**References (Outgoing):**

- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.forecast_cache_revisions

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `fleet_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.forecast_filter_groups

**References (Outgoing):**

- `group_id` → `lumina.forecast_filter_groups.group_id`

**Referenced By (Incoming):**

- `lumina.forecast_filter_groups.group_id` → `group_id`
- `lumina.forecast_filters.filter_id` → `group_id`
- `lumina.forecast_filters.group_id` → `group_id`
- `lumina.security_group_perm_attribute.group_id` → `group_id`
- `lumina.security_group_permissions.group_id` → `group_id`
- `lumina.security_group_policies.group_id` → `group_id`
- `lumina.security_groups.group_id` → `group_id`
- `lumina.security_user_groups.group_id` → `group_id`
- `lumina.workcard_documents_filter.filter_id` → `group_id`

### lumina.forecast_filters

**References (Outgoing):**

- `filter_id` → `lumina.forecast_filter_groups.group_id`
- `group_id` → `lumina.forecast_filter_groups.group_id`

### lumina.forecast_parameters

**References (Outgoing):**

- `param_id` → `lumina.forecast_parameters.param_id`

**Referenced By (Incoming):**

- `lumina.forecast_parameters.param_id` → `param_id`

### lumina.forecast_variation_details

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`

**Referenced By (Incoming):**

- `lumina.variations.variation_id` → `aircraft_short_reg`
- `lumina.variations_xref.variation_id` → `aircraft_short_reg`
- `lumina.variations_xref_overrides.variation_number` → `aircraft_short_reg`

### lumina.form_number

**References (Outgoing):**

- `form_number` → `lumina.company_form_attachments.attachment_id`
- `form_number_id` → `lumina.form_number.form_number_id`

**Referenced By (Incoming):**

- `lumina.form_number.form_number_id` → `form_number_id`
- `lumina.workcard_form_number.form_number_id` → `form_number_id`

### lumina.forward_schedule_summary_vals

**References (Outgoing):**

- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

### lumina.freight_cost_markups

**References (Outgoing):**

- `freight_cost_markup_id` → `lumina.freight_cost_markups.freight_cost_markup_id`

**Referenced By (Incoming):**

- `lumina.customer_contracts.markup_code` → `freight_cost_markup_id`
- `lumina.freight_cost_markups.freight_cost_markup_id` → `freight_cost_markup_id`
- `lumina.freight_costs.freight_cost_id` → `freight_cost_markup_id`
- `lumina.markups.markup_code` → `freight_cost_markup_id`
- `lumina.parts_freight_tiered_markups.freight_cost_markup_id` → `freight_cost_markup_id`
- `lumina.tiered_markup_range.markup_code` → `freight_cost_markup_id`
- `lumina.works_order_contracts.markup_code` → `freight_cost_markup_id`
- `lumina.works_order_markup_header.markup_code` → `freight_cost_markup_id`
- `lumina.works_order_markup_table.markup_code` → `freight_cost_markup_id`

### lumina.freight_costs

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`
- `freight_cost_id` → `lumina.freight_cost_markups.freight_cost_markup_id`
- `shipment_item_id` → `lumina.shipment_item.shipment_item_id`

### lumina.future_flights

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.gl_global_codes

**References (Outgoing):**

- `gl_id` → `lumina.gl_global_codes.gl_id`

**Referenced By (Incoming):**

- `lumina.gl_global_codes.gl_id` → `gl_id`

### lumina.goods_received_sheet_document

**References (Outgoing):**

- `batch_number` → `lumina.batch_file_header.key`
- `document_image_id` → `lumina.document_image_source.document_image_source_id`

**Referenced By (Incoming):**

- `lumina.batch_record_1.goods_received_number` → `batch_number`
- `lumina.batch_record_1_gu4240.goods_received_number` → `batch_number`
- `lumina.invoice_lines.goods_received_number` → `batch_number`
- `lumina.order_goods_received.goods_received_number` → `batch_number`
- `lumina.ordr_goods_bkp.goods_received_number` → `batch_number`

### lumina.hazardous_materials

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.ie96_historic

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`
- `bin_number` → `lumina.bins.bin_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `inv_number` → `lumina.invoice_categories.invoice_category`
- `price_type_code` → `lumina.price_types.price_type_code`

### lumina.inherited_acquisition_costs

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.invoice_categories

**Referenced By (Incoming):**

- `lumina.access_dim_accounts_info.invoice_number` → `invoice_category`
- `lumina.ie96_historic.inv_number` → `invoice_category`
- `lumina.invoice_line_notes.invoice_number` → `invoice_category`
- `lumina.invoice_lines.invoice_number` → `invoice_category`
- `lumina.invoice_trail_entries.invoice_number` → `invoice_category`
- `lumina.invoices.invoice_number` → `invoice_category`
- `lumina.maint_cost_mro_wo_invoices.invoice_id` → `invoice_category`
- `lumina.maintenance_cost_invoices.invoice_id` → `invoice_category`
- `lumina.oeim_invoice.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_cards.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_fixed_charges.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_inclusive_hrs.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_materials.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_packages.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_snap_con_rates.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_snap_cost_codes.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_snap_currencies.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_snap_departments.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_snap_employees.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_snap_part_master.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_snap_pay_types.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_snap_pm_bkup.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_snap_public_hol.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_snap_serl_master.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_snap_sfdc_book.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_snap_time_cats.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_snap_time_crits.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_snap_users.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_snap_vat_codes.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_warranty.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_warranty_refunds.invoice_number` → `invoice_category`
- `lumina.oeim_invoice_works_orders.invoice_number` → `invoice_category`
- `lumina.oeim_quote_dismissed.invoice_number` → `invoice_category`
- `lumina.order_goods_received_invoices.invoice_number` → `invoice_category`
- `lumina.order_history.invoice_number` → `invoice_category`
- `lumina.sales_history.invoice_number` → `invoice_category`
- `lumina.sales_invoices_xref.invoice_number` → `invoice_category`

### lumina.invoice_line_notes

**References (Outgoing):**

- `invoice_number` → `lumina.invoice_categories.invoice_category`

**Referenced By (Incoming):**

- `lumina.aircraft_header_1.line_number` → `invoice_number`

### lumina.invoice_lines

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `vat_code` → `lumina.amp_workcard_activations.workcard_activation_id`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`
- `currency_code` → `lumina.currency_codes.currency_code`
- `goods_received_number` → `lumina.goods_received_sheet_document.batch_number`
- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.invoice_system_header

**References (Outgoing):**

- `key_id` → `lumina.osys_key_to_reportid.osyskey`

### lumina.invoice_trail_entries

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `currency_code` → `lumina.currency_codes.currency_code`
- `invoice_number` → `lumina.invoice_categories.invoice_category`
- `invoice_trail_id` → `lumina.invoice_trail_entries.invoice_trail_id`

**Referenced By (Incoming):**

- `lumina.invoice_trail_entries.invoice_trail_id` → `invoice_trail_id`

### lumina.invoices

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `currency_code` → `lumina.currency_codes.currency_code`
- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.jasper_workcard_templates

**References (Outgoing):**

- `template_id` → `lumina.email_template.template_id`

### lumina.job_references

**Referenced By (Incoming):**

- `lumina.work_schedule_header_2.job_number` → `job_reference`

### lumina.lasers_system_header

**References (Outgoing):**

- `key_id` → `lumina.osys_key_to_reportid.osyskey`

### lumina.latest_repair_values

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `currency_code` → `lumina.currency_codes.currency_code`

### lumina.ldt

**References (Outgoing):**

- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

### lumina.le80_defect_temp

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.licence_categories

**References (Outgoing):**

- `licence_id` → `lumina.email_licence.license_id`

### lumina.life_code_entry

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `report_id` → `lumina.amp_report_documents.fleet`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

### lumina.life_code_entry_backup

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `report_id` → `lumina.amp_report_documents.fleet`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

### lumina.life_code_entry_dbf1065

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `report_id` → `lumina.amp_report_documents.fleet`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

### lumina.life_code_levels

**References (Outgoing):**

- `life_code` → `lumina.aircraft_life.aircraft_code`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

**Referenced By (Incoming):**

- `lumina.accomp_hist_lost_sched_val.life_code_level_id` → `life_code_level_id`
- `lumina.accomp_values_bkup.life_code_level_id` → `life_code_level_id`
- `lumina.accomplishment_history_values.life_code_level_id` → `life_code_level_id`
- `lumina.aircraft_life.life_code_level_id` → `life_code_level_id`
- `lumina.aircraft_life_dbf1065.life_code_level_id` → `life_code_level_id`
- `lumina.amp_component_intervals_limits.life_code_level_id` → `life_code_level_id`
- `lumina.amp_wc_in_limits_bak.life_code_level_id` → `life_code_level_id`
- `lumina.amp_workcard_intervals_limits.life_code_level_id` → `life_code_level_id`
- `lumina.amp_workcard_lcl_applicability.life_code_level_id` → `life_code_level_id`
- `lumina.completion_life_values.life_code_level_id` → `life_code_level_id`
- `lumina.component_life.life_code_level_id` → `life_code_level_id`
- `lumina.component_movement_hist_life.life_code_level_id` → `life_code_level_id`
- `lumina.dmg_rpr_stage_limits.life_code_level_id` → `life_code_level_id`
- `lumina.drn_components_nsbl_history.life_code_level_id` → `life_code_level_id`
- `lumina.drn_life_limits.life_code_level_id` → `life_code_level_id`
- `lumina.forward_schedule_summary_vals.life_code_level_id` → `life_code_level_id`
- `lumina.ldt.life_code_level_id` → `life_code_level_id`
- `lumina.life_code_entry.life_code_level_id` → `life_code_level_id`
- `lumina.life_code_entry_backup.life_code_level_id` → `life_code_level_id`
- `lumina.life_code_entry_dbf1065.life_code_level_id` → `life_code_level_id`
- `lumina.life_code_levels.life_code_level_id` → `life_code_level_id`
- `lumina.measurement_alerts_aircraft.life_code_level_id` → `life_code_level_id`
- `lumina.measurement_alerts_fleet.life_code_level_id` → `life_code_level_id`
- `lumina.rfc_frequency_phase_limits.life_code_level_id` → `life_code_level_id`
- `lumina.variations_xref_overrides.life_code_level_id` → `life_code_level_id`

### lumina.life_codes

**References (Outgoing):**

- `life_code` → `lumina.aircraft_life.aircraft_code`

### lumina.lmc_base_data_defs

**Referenced By (Incoming):**

- `lumina.lmc_base_data_reported_wc.lmc_base_data_id` → `bd_def_id`

### lumina.lmc_base_data_options

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `opt_id` → `lumina.lmc_base_data_options.opt_id`

**Referenced By (Incoming):**

- `lumina.lmc_base_data_options.opt_id` → `opt_id`
- `lumina.transaction_log_mavis.option_number` → `opt_id`

### lumina.lmc_base_data_reported_wc

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `lmc_base_data_id` → `lumina.lmc_base_data_defs.bd_def_id`

### lumina.loaned_units

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `order_number` → `lumina.batch_orders.batch_number`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.long_serial_number_xref

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `long_serial_number` → `lumina.long_serial_number_xref.part_number`

**Referenced By (Incoming):**

- `lumina.long_serial_number_xref.long_serial_number` → `part_number`
- `lumina.oeim_invoice_snap_serl_master.long_serial_number` → `part_number`
- `lumina.rotable_batch_locations.long_serial_number` → `part_number`
- `lumina.short_long_serials.long_serial_number` → `part_number`

### lumina.maint_accomplishment_costs

**References (Outgoing):**

- `accomplishment_id` → `lumina.accomplishment_history.accomplishment_id`
- `maint_cost_id` → `lumina.maint_cost_budget_adsb.budget_id`

### lumina.maint_associated_cost_aircraft

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `associated_cost_id` → `lumina.maint_associated_cost_aircraft.associated_cost_id`
- `category_id` → `lumina.maint_cost_time_category_set.category_set_id`

**Referenced By (Incoming):**

- `lumina.maint_associated_cost_aircraft.associated_cost_id` → `associated_cost_id`
- `lumina.maint_associated_costs.associated_cost_id` → `associated_cost_id`

### lumina.maint_associated_costs

**References (Outgoing):**

- `currency_code` → `lumina.currency_codes.currency_code`
- `associated_cost_id` → `lumina.maint_associated_cost_aircraft.associated_cost_id`

### lumina.maint_card_pref_cost_cats

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`

### lumina.maint_cost_budget_adsb

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `workcard_id` → `lumina.amp_access_panels_by_workcard.fleet`
- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `item_id` → `lumina.delivery_note_item_header_1.delivery_note_number`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `budget_id` → `lumina.maint_cost_budget_adsb.budget_id`
- `frequency_id` → `lumina.rfc_frequency_phase_header.rfc_id`
- `phase_number` → `lumina.rfc_frequency_phase_header.rfc_id`

**Referenced By (Incoming):**

- `lumina.maint_accomplishment_costs.maint_cost_id` → `budget_id`
- `lumina.maint_cost_budget_adsb.budget_id` → `budget_id`
- `lumina.maint_cost_budget_aircraft.budget_id` → `budget_id`
- `lumina.maint_cost_budget_cfds.budget_id` → `budget_id`
- `lumina.maint_cost_budget_costs.budget_id` → `budget_id`
- `lumina.maint_cost_budget_defects.budget_id` → `budget_id`
- `lumina.maint_cost_budget_labour_ests.budget_id` → `budget_id`
- `lumina.maint_cost_budget_materials.budget_id` → `budget_id`
- `lumina.maint_cost_budget_packages.budget_id` → `budget_id`
- `lumina.maint_cost_budget_visits.budget_id` → `budget_id`
- `lumina.maint_cost_budget_workcards.budget_id` → `budget_id`
- `lumina.maint_hist_associated_costs.maint_cost_id` → `budget_id`
- `lumina.maint_labour_costs.maint_cost_id` → `budget_id`
- `lumina.maint_material_costs.maint_cost_id` → `budget_id`
- `lumina.maint_nrc_costs.maint_cost_id` → `budget_id`
- `lumina.maint_works_order_costs.maint_cost_id` → `budget_id`
- `lumina.maintenance_cost_budgets.budget_id` → `budget_id`

### lumina.maint_cost_budget_aircraft

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `budget_id` → `lumina.maint_cost_budget_adsb.budget_id`

### lumina.maint_cost_budget_cfds

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `item_id` → `lumina.delivery_note_item_header_1.delivery_note_number`
- `budget_id` → `lumina.maint_cost_budget_adsb.budget_id`

### lumina.maint_cost_budget_costs

**References (Outgoing):**

- `item_id` → `lumina.delivery_note_item_header_1.delivery_note_number`
- `budget_id` → `lumina.maint_cost_budget_adsb.budget_id`
- `budget_cost_id` → `lumina.maint_cost_budget_costs.budget_cost_id`
- `cost_type_id` → `lumina.maintenance_cost_types.cost_id`

**Referenced By (Incoming):**

- `lumina.maint_cost_budget_costs.budget_cost_id` → `budget_cost_id`
- `lumina.maint_cost_budget_defects.budget_cost_id` → `budget_cost_id`

### lumina.maint_cost_budget_defects

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `budget_id` → `lumina.maint_cost_budget_adsb.budget_id`
- `budget_cost_id` → `lumina.maint_cost_budget_costs.budget_cost_id`

### lumina.maint_cost_budget_labour_ests

**References (Outgoing):**

- `item_id` → `lumina.delivery_note_item_header_1.delivery_note_number`
- `budget_id` → `lumina.maint_cost_budget_adsb.budget_id`
- `labour_est_id` → `lumina.maint_cost_budget_labour_ests.budget_id`

**Referenced By (Incoming):**

- `lumina.maint_cost_budget_labour_ests.labour_est_id` → `budget_id`

### lumina.maint_cost_budget_materials

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `material_id` → `lumina.amp_material_effectivity.workcard_material_id`
- `item_id` → `lumina.delivery_note_item_header_1.delivery_note_number`
- `budget_id` → `lumina.maint_cost_budget_adsb.budget_id`

### lumina.maint_cost_budget_packages

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `package_code` → `lumina.amp_package_notes.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `item_id` → `lumina.delivery_note_item_header_1.delivery_note_number`
- `budget_id` → `lumina.maint_cost_budget_adsb.budget_id`

### lumina.maint_cost_budget_visits

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `visit_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `item_id` → `lumina.delivery_note_item_header_1.delivery_note_number`
- `budget_id` → `lumina.maint_cost_budget_adsb.budget_id`

### lumina.maint_cost_budget_workcards

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `workcard_id` → `lumina.amp_access_panels_by_workcard.fleet`
- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `cost_code` → `lumina.cost_codes.id`
- `item_id` → `lumina.delivery_note_item_header_1.delivery_note_number`
- `budget_id` → `lumina.maint_cost_budget_adsb.budget_id`
- `package_item_id` → `lumina.package_items.package_items_id`
- `trade_code` → `lumina.trades.trade_code`

### lumina.maint_cost_hourly_rate_set

**References (Outgoing):**

- `hourly_rate_set_id` → `lumina.maint_cost_hourly_rate_set.hourly_rate_set_id`
- `category_set_id` → `lumina.maint_cost_time_category_set.category_set_id`

**Referenced By (Incoming):**

- `lumina.maint_cost_hourly_rate_set.hourly_rate_set_id` → `hourly_rate_set_id`
- `lumina.maint_cost_hourly_rates.hourly_rate_set_id` → `hourly_rate_set_id`

### lumina.maint_cost_hourly_rates

**References (Outgoing):**

- `cost_code` → `lumina.cost_codes.id`
- `hourly_rate_set_id` → `lumina.maint_cost_hourly_rate_set.hourly_rate_set_id`
- `time_category_id` → `lumina.maint_cost_time_category_set.category_set_id`
- `trade_code` → `lumina.trades.trade_code`

### lumina.maint_cost_mro_wo_invoices

**References (Outgoing):**

- `invoice_id` → `lumina.invoice_categories.invoice_category`

### lumina.maint_cost_mro_wo_quotes

**References (Outgoing):**

- `quote_id` → `lumina.cq_quote_cards.quote_id`

### lumina.maint_cost_time_categories

**References (Outgoing):**

- `contract_id` → `lumina.customer_contract_rates.contract_id`
- `time_category_id` → `lumina.maint_cost_time_category_set.category_set_id`
- `category_set_id` → `lumina.maint_cost_time_category_set.category_set_id`

### lumina.maint_cost_time_category_set

**References (Outgoing):**

- `category_set_id` → `lumina.maint_cost_time_category_set.category_set_id`

**Referenced By (Incoming):**

- `lumina.customer_contract_rates.time_category_id` → `category_set_id`
- `lumina.customer_contract_stop_incl.time_category_id` → `category_set_id`
- `lumina.default_labour_rates.time_category_id` → `category_set_id`
- `lumina.email_notification.category_id` → `category_set_id`
- `lumina.email_notification_categories.category_id` → `category_set_id`
- `lumina.maint_associated_cost_aircraft.category_id` → `category_set_id`
- `lumina.maint_cost_hourly_rate_set.category_set_id` → `category_set_id`
- `lumina.maint_cost_hourly_rates.time_category_id` → `category_set_id`
- `lumina.maint_cost_time_categories.time_category_id` → `category_set_id`
- `lumina.maint_cost_time_categories.category_set_id` → `category_set_id`
- `lumina.maint_cost_time_category_set.category_set_id` → `category_set_id`
- `lumina.maintenance_cat_excl_subchap.category_id` → `category_set_id`
- `lumina.maintenance_cat_incl_chapter.category_id` → `category_set_id`
- `lumina.maintenance_cat_incl_parts.category_id` → `category_set_id`
- `lumina.maintenance_cost_cat_fleet.category_id` → `category_set_id`
- `lumina.maintenance_cost_categories.category_id` → `category_set_id`
- `lumina.oeim_invoice_inclusive_hrs.time_category_id` → `category_set_id`
- `lumina.oeim_invoice_snap_con_rates.time_category_id` → `category_set_id`
- `lumina.oeim_invoice_snap_time_cats.time_category_id` → `category_set_id`
- `lumina.planners_notes.category_id` → `category_set_id`
- `lumina.planners_notes_categories.category_id` → `category_set_id`
- `lumina.time_categories.time_category_id` → `category_set_id`

### lumina.maint_hist_associated_costs

**References (Outgoing):**

- `maint_cost_id` → `lumina.maint_cost_budget_adsb.budget_id`
- `cost_type_id` → `lumina.maintenance_cost_types.cost_id`

### lumina.maint_historic_defects

**References (Outgoing):**

- `defect_id` → `lumina.defect_extensions.defect_id`

### lumina.maint_labour_costs

**References (Outgoing):**

- `maint_cost_id` → `lumina.maint_cost_budget_adsb.budget_id`

### lumina.maint_material_costs

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `maint_cost_id` → `lumina.maint_cost_budget_adsb.budget_id`
- `material_cost_id` → `lumina.maint_material_costs.material_cost_id`

**Referenced By (Incoming):**

- `lumina.maint_material_costs.material_cost_id` → `material_cost_id`

### lumina.maint_nrc_costs

**References (Outgoing):**

- `nrc_number` → `lumina.cq_quote_nrc_access_panels.quote_id`
- `maint_cost_id` → `lumina.maint_cost_budget_adsb.budget_id`

### lumina.maint_pack_pref_cost_cats

**References (Outgoing):**

- `package_code` → `lumina.amp_package_notes.fleet`

### lumina.maint_works_order_costs

**References (Outgoing):**

- `maint_cost_id` → `lumina.maint_cost_budget_adsb.budget_id`

### lumina.maintenance_cat_excl_subchap

**References (Outgoing):**

- `category_id` → `lumina.maint_cost_time_category_set.category_set_id`

### lumina.maintenance_cat_incl_chapter

**References (Outgoing):**

- `category_id` → `lumina.maint_cost_time_category_set.category_set_id`

### lumina.maintenance_cat_incl_parts

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `category_id` → `lumina.maint_cost_time_category_set.category_set_id`

### lumina.maintenance_cost_budgets

**References (Outgoing):**

- `budget_id` → `lumina.maint_cost_budget_adsb.budget_id`

### lumina.maintenance_cost_cat_fleet

**References (Outgoing):**

- `category_id` → `lumina.maint_cost_time_category_set.category_set_id`

### lumina.maintenance_cost_categories

**References (Outgoing):**

- `category_id` → `lumina.maint_cost_time_category_set.category_set_id`

### lumina.maintenance_cost_entry

**References (Outgoing):**

- `entry_id` → `lumina.batches_by_customs_entry.customs_entry_number`
- `cost_id` → `lumina.cost_codes.id`

### lumina.maintenance_cost_invoices

**References (Outgoing):**

- `currency_code` → `lumina.currency_codes.currency_code`
- `invoice_id` → `lumina.invoice_categories.invoice_category`

### lumina.maintenance_cost_quotes

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `quote_id` → `lumina.cq_quote_cards.quote_id`
- `currency_code` → `lumina.currency_codes.currency_code`

### lumina.maintenance_cost_types

**References (Outgoing):**

- `cost_id` → `lumina.cost_codes.id`

**Referenced By (Incoming):**

- `lumina.maint_cost_budget_costs.cost_type_id` → `cost_id`
- `lumina.maint_hist_associated_costs.cost_type_id` → `cost_id`

### lumina.mandatory_parts

**References (Outgoing):**

- `cost_code` → `lumina.cost_codes.id`

### lumina.manufacturers_work_documents

**References (Outgoing):**

- `document_id` → `lumina.aircraft_documents.aircraft_document_id`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.marketing_codes

**References (Outgoing):**

- `marketing_code` → `lumina.marketing_codes.marketing_code`

**Referenced By (Incoming):**

- `lumina.marketing_codes.marketing_code` → `marketing_code`
- `lumina.part_number_marketing_codes.marketing_code` → `marketing_code`

### lumina.markups

**References (Outgoing):**

- `markup_code` → `lumina.freight_cost_markups.freight_cost_markup_id`

### lumina.material_pool_agreement

**References (Outgoing):**

- `currency_code` → `lumina.currency_codes.currency_code`
- `agreement_id` → `lumina.material_pool_agreement.agreement_id`

**Referenced By (Incoming):**

- `lumina.material_pool_agreement.agreement_id` → `agreement_id`
- `lumina.material_pool_agreement_ac.agreement_id` → `agreement_id`
- `lumina.material_pool_agreement_pn.agreement_id` → `agreement_id`

### lumina.material_pool_agreement_ac

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `agreement_id` → `lumina.material_pool_agreement.agreement_id`

### lumina.material_pool_agreement_pn

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `agreement_id` → `lumina.material_pool_agreement.agreement_id`

### lumina.mavis_system_header

**References (Outgoing):**

- `key_id` → `lumina.osys_key_to_reportid.osyskey`

### lumina.maximum_preload_pick_quantity

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.measurement_alerts_aircraft

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `life_code` → `lumina.aircraft_life.aircraft_code`
- `email_notification_cat_id` → `lumina.email_notification_categories.category_id`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

### lumina.measurement_alerts_fleet

**References (Outgoing):**

- `life_code` → `lumina.aircraft_life.aircraft_code`
- `email_notification_cat_id` → `lumina.email_notification_categories.category_id`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

### lumina.mel_items

**References (Outgoing):**

- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.mel_references

**References (Outgoing):**

- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.mel_revision_history

**References (Outgoing):**

- `history_id` → `lumina.accomplishment_history.accomplishment_id`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `user_id` → `lumina.dataset_locks_by_user.user_id`

**Referenced By (Incoming):**

- `lumina.fleet_header_2.mel_revision_number` → `history_id`
- `lumina.nrc_defect_details.mel_revision_number` → `history_id`
- `lumina.tech_log_3.mel_revision_number` → `history_id`

### lumina.mel_revisions

**References (Outgoing):**

- `revision_id` → `lumina.amp_revision_history.history_id`
- `user_id` → `lumina.dataset_locks_by_user.user_id`

### lumina.monthly_loans_in

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `order_number` → `lumina.batch_orders.batch_number`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.monthly_loans_out

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `delivery_note_number` → `lumina.delivery_note_extended_remarks.delivery_note_number`

### lumina.movement_codes

**References (Outgoing):**

- `movement_code` → `lumina.component_movement_hist_life.part_number`

### lumina.n_s_extended_part_descriptions

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.netline_import_index

**References (Outgoing):**

- `report_id` → `lumina.amp_report_documents.fleet`

### lumina.no_narrative_default

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.non_stock_parts

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `stock_check_code` → `lumina.random_stock_check_bins.warehouse_code`

**Referenced By (Incoming):**

- `lumina.preorder_lines.non_stock_part_number` → `part_number`
- `lumina.shipment_demands.non_stock_part_number` → `part_number`

### lumina.non_stock_parts_bkp_oases382

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `stock_check_code` → `lumina.random_stock_check_bins.warehouse_code`

### lumina.nrc_access_panels

**References (Outgoing):**

- `access_panel_code` → `lumina.amp_access_panel_desc_hdr.fleet`
- `nrc_number` → `lumina.cq_quote_nrc_access_panels.quote_id`

### lumina.nrc_defect_details

**References (Outgoing):**

- `corrosion_code` → `lumina.corrosion_categories.corrosion_code`
- `defect_id` → `lumina.defect_extensions.defect_id`
- `mel_revision_number` → `lumina.mel_revision_history.history_id`

### lumina.nrc_defect_notes

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `defect_number` → `lumina.defect_extensions.defect_id`

### lumina.nrc_documents

**References (Outgoing):**

- `document_id` → `lumina.aircraft_documents.aircraft_document_id`
- `nrc_number` → `lumina.cq_quote_nrc_access_panels.quote_id`
- `document_image_id` → `lumina.document_image_source.document_image_source_id`
- `sequence_number` → `lumina.nrc_high_sequence_control.key_id`

### lumina.nrc_high_sequence_control

**References (Outgoing):**

- `key_id` → `lumina.osys_key_to_reportid.osyskey`

**Referenced By (Incoming):**

- `lumina.amp_access_panels_by_workcard.sequence_number` → `key_id`
- `lumina.amp_documents_by_workcard.sequence_number` → `key_id`
- `lumina.amp_documents_by_workcard_bk.sequence_number` → `key_id`
- `lumina.amp_materials_required_by_wc.sequence_number` → `key_id`
- `lumina.amp_packages_by_workcard.sequence_number` → `key_id`
- `lumina.amp_visits.sequence_number` → `key_id`
- `lumina.amp_wc_aircraft_exclusions.sequence_number` → `key_id`
- `lumina.nrc_documents.sequence_number` → `key_id`
- `lumina.nrc_requirements_actions.sequence_id` → `key_id`
- `lumina.repetitive_defect_tech_logs.sequence_number` → `key_id`
- `lumina.security_audit_log_meta_data.sequence_number` → `key_id`
- `lumina.sfdc_deleted_bookings.sequence_number` → `key_id`
- `lumina.tech_log_rectification_text.sequence_number` → `key_id`
- `lumina.unknown_part_numbers.sequence_number` → `key_id`

### lumina.nrc_materials

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `nrc_number` → `lumina.cq_quote_nrc_access_panels.quote_id`

### lumina.nrc_print_history

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `defect_number` → `lumina.defect_extensions.defect_id`
- `print_history_id` → `lumina.nrc_print_history.print_history_id`

**Referenced By (Incoming):**

- `lumina.nrc_print_history.print_history_id` → `print_history_id`

### lumina.nrc_properties

**References (Outgoing):**

- `nrc_number` → `lumina.cq_quote_nrc_access_panels.quote_id`

### lumina.nrc_rectification_notes

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `defect_number` → `lumina.defect_extensions.defect_id`

### lumina.nrc_requirements_actions

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `defect_number` → `lumina.defect_extensions.defect_id`
- `sequence_id` → `lumina.nrc_high_sequence_control.key_id`

**Referenced By (Incoming):**

- `lumina.condition_pick_table.requirement_number` → `aircraft_short_reg`
- `lumina.consumable_history.requirement_number` → `aircraft_short_reg`
- `lumina.credit_works_order_cards.requirement_number` → `aircraft_short_reg`
- `lumina.delivery_note_item_header_1.requirement_number` → `aircraft_short_reg`
- `lumina.dmg_rpr_repair_req_details.requirement_number` → `aircraft_short_reg`
- `lumina.dues_register.requirement_number` → `aircraft_short_reg`
- `lumina.oeim_credit_warranty.requirement_number` → `aircraft_short_reg`
- `lumina.oeim_invoice_materials.requirement_number` → `aircraft_short_reg`
- `lumina.oeim_invoice_warranty.requirement_number` → `aircraft_short_reg`
- `lumina.oeim_invoice_warranty_refunds.requirement_number` → `aircraft_short_reg`
- `lumina.order_line_requirement_xref.requirement_number` → `aircraft_short_reg`
- `lumina.order_requirement_allocation.requirement_number` → `aircraft_short_reg`
- `lumina.part_xref_to_pick_history.requirement_number` → `aircraft_short_reg`
- `lumina.pick_hist_7890_bkp.requirement_number` → `aircraft_short_reg`
- `lumina.pick_history.requirement_number` → `aircraft_short_reg`
- `lumina.preorder_line_requirement_xref.requirement_number` → `aircraft_short_reg`
- `lumina.requirement_planners_notes.requirement_number` → `aircraft_short_reg`
- `lumina.requirement_recharge_details.requirement_number` → `aircraft_short_reg`
- `lumina.requirement_to_rfq_xref.requirement_number` → `aircraft_short_reg`
- `lumina.requirements.requirement_number` → `aircraft_short_reg`
- `lumina.rfq_requirement_xref.requirement_number` → `aircraft_short_reg`
- `lumina.rotable_history.requirement_number` → `aircraft_short_reg`
- `lumina.sales_order_lines.requirement_number` → `aircraft_short_reg`
- `lumina.shelf_life_expiry_req_codes.requirement_code` → `aircraft_short_reg`
- `lumina.shipment_requirement_demands.requirement_number` → `aircraft_short_reg`
- `lumina.unmatched_issues_and_returns.requirement_number` → `aircraft_short_reg`
- `lumina.works_order_issues_and_returns.requirement_number` → `aircraft_short_reg`
- `lumina.works_order_issues_and_rtn_bac.requirement_number` → `aircraft_short_reg`

### lumina.nrc_status_history

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `status_code` → `lumina.amp_revision_status.revision_status_id`
- `defect_number` → `lumina.defect_extensions.defect_id`
- `status_history_id` → `lumina.nrc_status_history.status_history_id`

**Referenced By (Incoming):**

- `lumina.nrc_status_history.status_history_id` → `status_history_id`

### lumina.nrc_tools

**References (Outgoing):**

- `batch_number` → `lumina.batch_file_header.key`
- `nrc_number` → `lumina.cq_quote_nrc_access_panels.quote_id`

### lumina.nrc_workcard_narrative

**References (Outgoing):**

- `nrc_number` → `lumina.cq_quote_nrc_access_panels.quote_id`

### lumina.nrc_xref_to_scheduled_workcard

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `nrc_number` → `lumina.cq_quote_nrc_access_panels.quote_id`
- `defect_number` → `lumina.defect_extensions.defect_id`

### lumina.oases_message_log

**References (Outgoing):**

- `log_number` → `lumina.amp_data_migration_log.log_number`

### lumina.oases_reports

**References (Outgoing):**

- `report_id` → `lumina.amp_report_documents.fleet`

**Referenced By (Incoming):**

- `lumina.workpack_printing_control.oases_report_id` → `report_id`

### lumina.oeim_booking_base_data

**Referenced By (Incoming):**

- `lumina.oeim_invoice_snap_sfdc_book.booking_id` → `booking_rounding_up_mins`
- `lumina.sfdc_activity.booking_id` → `booking_rounding_up_mins`
- `lumina.sfdc_bookings.booking_id` → `booking_rounding_up_mins`

### lumina.oeim_credit_warranty

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `card_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`

### lumina.oeim_invoice

**References (Outgoing):**

- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.oeim_invoice_cards

**References (Outgoing):**

- `card_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.oeim_invoice_fixed_charges

**References (Outgoing):**

- `cost_code` → `lumina.cost_codes.id`
- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.oeim_invoice_inclusive_hrs

**References (Outgoing):**

- `card_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `invoice_number` → `lumina.invoice_categories.invoice_category`
- `time_category_id` → `lumina.maint_cost_time_category_set.category_set_id`

### lumina.oeim_invoice_materials

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `card_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `invoice_number` → `lumina.invoice_categories.invoice_category`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`

### lumina.oeim_invoice_packages

**References (Outgoing):**

- `package_code` → `lumina.amp_package_notes.fleet`
- `cost_code` → `lumina.cost_codes.id`
- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.oeim_invoice_snap_con_rates

**References (Outgoing):**

- `cost_code` → `lumina.cost_codes.id`
- `invoice_number` → `lumina.invoice_categories.invoice_category`
- `time_category_id` → `lumina.maint_cost_time_category_set.category_set_id`

### lumina.oeim_invoice_snap_cost_codes

**References (Outgoing):**

- `cost_code` → `lumina.cost_codes.id`
- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.oeim_invoice_snap_currencies

**References (Outgoing):**

- `currency_code` → `lumina.currency_codes.currency_code`
- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.oeim_invoice_snap_departments

**References (Outgoing):**

- `department_id` → `lumina.departments.department_id`
- `export_code` → `lumina.export_codes.export_id`
- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.oeim_invoice_snap_employees

**References (Outgoing):**

- `employee_number` → `lumina.defect_stage_employees.defect_id`
- `invoice_number` → `lumina.invoice_categories.invoice_category`
- `trade_code` → `lumina.trades.trade_code`

### lumina.oeim_invoice_snap_part_master

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.oeim_invoice_snap_pay_types

**References (Outgoing):**

- `invoice_number` → `lumina.invoice_categories.invoice_category`
- `payment_code` → `lumina.payment_types.payment_code`

### lumina.oeim_invoice_snap_pm_bkup

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.oeim_invoice_snap_public_hol

**References (Outgoing):**

- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.oeim_invoice_snap_serl_master

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `invoice_number` → `lumina.invoice_categories.invoice_category`
- `long_serial_number` → `lumina.long_serial_number_xref.part_number`

### lumina.oeim_invoice_snap_sfdc_book

**References (Outgoing):**

- `task_number` → `lumina.amp_datmig_comp_task_lookup.fleet`
- `defect_code` → `lumina.defect_extensions.defect_id`
- `employee_number` → `lumina.defect_stage_employees.defect_id`
- `invoice_number` → `lumina.invoice_categories.invoice_category`
- `booking_id` → `lumina.oeim_booking_base_data.booking_rounding_up_mins`

### lumina.oeim_invoice_snap_time_cats

**References (Outgoing):**

- `invoice_number` → `lumina.invoice_categories.invoice_category`
- `time_category_id` → `lumina.maint_cost_time_category_set.category_set_id`

### lumina.oeim_invoice_snap_time_crits

**References (Outgoing):**

- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.oeim_invoice_snap_users

**References (Outgoing):**

- `oases_id` → `lumina.cfd_categorires_bkpoases405.cfd_category`
- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.oeim_invoice_snap_vat_codes

**References (Outgoing):**

- `vat_code` → `lumina.amp_workcard_activations.workcard_activation_id`
- `export_id` → `lumina.export_codes.export_id`
- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.oeim_invoice_warranty

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `card_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `invoice_number` → `lumina.invoice_categories.invoice_category`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`

### lumina.oeim_invoice_warranty_refunds

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `card_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `invoice_number` → `lumina.invoice_categories.invoice_category`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`

### lumina.oeim_invoice_works_orders

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.oeim_quote_dismissed

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.oeim_transaction_log_details

**References (Outgoing):**

- `detail_number` → `lumina.aircraft_lease_details.aircraft_code`
- `log_number` → `lumina.amp_data_migration_log.log_number`

### lumina.oeim_transaction_log_header

**References (Outgoing):**

- `log_number` → `lumina.amp_data_migration_log.log_number`

### lumina.ord_po_unit_conv_delta1827

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`

### lumina.order_change_history

**References (Outgoing):**

- `history_id` → `lumina.accomplishment_history.accomplishment_id`
- `order_number` → `lumina.batch_orders.batch_number`
- `preorder_id` → `lumina.preorder_line_requirement_xref.preorder_id`

### lumina.order_customs_info

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`

### lumina.order_delivery_note_remarks

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`

### lumina.order_email_chasing

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`

### lumina.order_goods_received

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `order_number` → `lumina.batch_orders.batch_number`
- `goods_received_number` → `lumina.goods_received_sheet_document.batch_number`

### lumina.order_goods_received_invoices

**References (Outgoing):**

- `vat_code` → `lumina.amp_workcard_activations.workcard_activation_id`
- `order_number` → `lumina.batch_orders.batch_number`
- `currency_code` → `lumina.currency_codes.currency_code`
- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.order_header_1

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `order_number` → `lumina.batch_orders.batch_number`
- `company_code` → `lumina.company_codes.company_code`
- `currency_code` → `lumina.currency_codes.currency_code`
- `release_code` → `lumina.release_codes.release_code`

### lumina.order_header_2

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`
- `works_order_number` → `lumina.credit_works_order_cards.credit_note_no`

### lumina.order_header_3

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`
- `delivery_note_number` → `lumina.delivery_note_extended_remarks.delivery_note_number`

### lumina.order_header_4

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`
- `employee_number` → `lumina.defect_stage_employees.defect_id`

### lumina.order_history

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `condition_code` → `lumina.condition_codes.condition_code`
- `currency_code` → `lumina.currency_codes.currency_code`
- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.order_line_additional_info

**References (Outgoing):**

- `airway_bill_number` → `lumina.airway_bill_references.awb_id`
- `order_number` → `lumina.batch_orders.batch_number`
- `condition_code` → `lumina.condition_codes.condition_code`
- `release_code` → `lumina.release_codes.release_code`

**Referenced By (Incoming):**

- `lumina.rp_employee_calendar_addition.addition_id` → `order_number`

### lumina.order_line_additional_info_2

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`

### lumina.order_line_notes

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`

### lumina.order_line_quotes_data

**References (Outgoing):**

- `vat_code` → `lumina.amp_workcard_activations.workcard_activation_id`
- `order_number` → `lumina.batch_orders.batch_number`
- `currency_code` → `lumina.currency_codes.currency_code`

### lumina.order_line_requirement_xref

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`

### lumina.order_line_weight_dimension

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`
- `dimension_id` → `lumina.order_line_weight_dimension.dimension_id`

**Referenced By (Incoming):**

- `lumina.order_line_weight_dimension.dimension_id` → `dimension_id`

### lumina.order_lines

**References (Outgoing):**

- `vat_code` → `lumina.amp_workcard_activations.workcard_activation_id`
- `order_number` → `lumina.batch_orders.batch_number`
- `bin_number` → `lumina.bins.bin_number`
- `movement_code` → `lumina.component_movement_hist_life.part_number`
- `strip_report_number` → `lumina.strip_report_findings_text.strip_report_number`

### lumina.order_numbers_by_supplier

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `order_number` → `lumina.batch_orders.batch_number`

### lumina.order_print_date

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`

### lumina.order_purchase_unit_conversion

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`

### lumina.order_requirement_allocation

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`

**Referenced By (Incoming):**

- `lumina.rp_employee_allocation.allocation_id` → `order_number`

### lumina.order_standard_text_blocks

**References (Outgoing):**

- `block_number` → `lumina.block_countries.block_code`

### lumina.order_supplier_approval

**References (Outgoing):**

- `supplier_approval_number` → `lumina.account_supplier_approvals.account_code`
- `order_number` → `lumina.batch_orders.batch_number`

### lumina.order_text

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`

### lumina.order_workshop_works_orders

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`

### lumina.orders_by_due_date

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`

### lumina.orders_to_part_number_xref

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `order_number` → `lumina.batch_orders.batch_number`

### lumina.ordr_goods_bkp

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `order_number` → `lumina.batch_orders.batch_number`
- `goods_received_number` → `lumina.goods_received_sheet_document.batch_number`

### lumina.original_purchase_values

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `currency_code` → `lumina.currency_codes.currency_code`

### lumina.osys_defect_act_to_defect_id

**References (Outgoing):**

- `defect_id` → `lumina.defect_extensions.defect_id`

### lumina.osys_defect_to_defect_id

**References (Outgoing):**

- `defect_number` → `lumina.defect_extensions.defect_id`
- `defect_id` → `lumina.defect_extensions.defect_id`

### lumina.osys_defect_to_tech_log_line

**References (Outgoing):**

- `defect_number` → `lumina.defect_extensions.defect_id`

### lumina.osys_key_to_reportid

**References (Outgoing):**

- `report_id` → `lumina.amp_report_documents.fleet`

**Referenced By (Incoming):**

- `lumina.account_system_header.key_id` → `osyskey`
- `lumina.invoice_system_header.key_id` → `osyskey`
- `lumina.lasers_system_header.key_id` → `osyskey`
- `lumina.mavis_system_header.key_id` → `osyskey`
- `lumina.nrc_high_sequence_control.key_id` → `osyskey`
- `lumina.rd_xref_to_tech_logs.key_id` → `osyskey`
- `lumina.sales_order_parameters.key_id` → `osyskey`
- `lumina.system_header_icarus.key_id` → `osyskey`
- `lumina.test_table.key_id` → `osyskey`
- `lumina.transaction_header_mavis.key_id` → `osyskey`
- `lumina.transaction_header_trex_lasers.key_id` → `osyskey`
- `lumina.workcard_default_status.key_id` → `osyskey`

### lumina.outstation_codes

**References (Outgoing):**

- `outstation_code` → `lumina.outstation_codes.outstation_code`

**Referenced By (Incoming):**

- `lumina.outstation_codes.outstation_code` → `outstation_code`

### lumina.package

**References (Outgoing):**

- `package_id` → `lumina.amp_package_notes.fleet`
- `shipment_id` → `lumina.shipment.shipment_id`

### lumina.package_items

**References (Outgoing):**

- `package_id` → `lumina.amp_package_notes.fleet`
- `item_id` → `lumina.delivery_note_item_header_1.delivery_note_number`
- `package_items_id` → `lumina.package_items.package_items_id`

**Referenced By (Incoming):**

- `lumina.maint_cost_budget_workcards.package_item_id` → `package_items_id`
- `lumina.package_items.package_items_id` → `package_items_id`

### lumina.paragraph_cancels

**References (Outgoing):**

- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `paragraph_id` → `lumina.paragraph_cancels.rfc_id`

**Referenced By (Incoming):**

- `lumina.accomp_bkup.paragraph_id` → `rfc_id`
- `lumina.accomp_hist_delta_1763.paragraph_id` → `rfc_id`
- `lumina.accomp_hist_lost_sched.paragraph_id` → `rfc_id`
- `lumina.accomplishment_history.paragraph_id` → `rfc_id`
- `lumina.dmg_rpr_inspections.paragraph_id` → `rfc_id`
- `lumina.dmg_rpr_interim_repairs.paragraph_id` → `rfc_id`
- `lumina.dmg_rpr_permanent_repairs.paragraph_id` → `rfc_id`
- `lumina.dmg_rpr_time_limited_repairs.paragraph_id` → `rfc_id`
- `lumina.paragraph_cancels.paragraph_id` → `rfc_id`
- `lumina.rfc_aircraft.paragraph_id` → `rfc_id`
- `lumina.rfc_components.paragraph_id` → `rfc_id`
- `lumina.rfc_frequency_phase_header.paragraph_id` → `rfc_id`
- `lumina.rfc_frequency_phase_limits.paragraph_id` → `rfc_id`
- `lumina.rfc_frequency_phases.paragraph_id` → `rfc_id`
- `lumina.rfc_paragraphs.paragraph_id` → `rfc_id`
- `lumina.temp_rfc_paragraphs.paragraph_id` → `rfc_id`
- `lumina.uf_forecast_cache.paragraph_id` → `rfc_id`

### lumina.part_applicability_codes

**References (Outgoing):**

- `applicability_code` → `lumina.amp_workcard_lcl_applicability.life_code_level_id`

### lumina.part_change_warning_chapters

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.part_change_warnings

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.part_customs_tariff_territory

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `customs_tariff_code` → `lumina.customs_tariff_codes.customs_tariff_code`

### lumina.part_master

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `stock_check_code` → `lumina.random_stock_check_bins.warehouse_code`

### lumina.part_master_bkp_oases382

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `stock_check_code` → `lumina.random_stock_check_bins.warehouse_code`

### lumina.part_number_amendment_history

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `user_id` → `lumina.dataset_locks_by_user.user_id`

### lumina.part_number_chapters

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.part_number_essentiality_codes

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `essentiality_code` → `lumina.part_number_essentiality_codes.part_number`

**Referenced By (Incoming):**

- `lumina.part_number_essentiality_codes.essentiality_code` → `part_number`

### lumina.part_number_marketing_codes

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `marketing_code` → `lumina.marketing_codes.marketing_code`

### lumina.part_number_order_retention

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.part_number_owner_float_levels

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.part_number_properties

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.part_number_properties_serials

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.part_number_shelf_life_details

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `component_life_limit_id` → `lumina.component_life_limits.component_life_limit_id`

### lumina.part_number_technical_notes

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.part_number_vat_codes

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `vat_code` → `lumina.amp_workcard_activations.workcard_activation_id`

### lumina.part_serial_documents

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `document_image_id` → `lumina.document_image_source.document_image_source_id`
- `part_serial_document_id` → `lumina.part_serial_documents.part_serial_document_id`

**Referenced By (Incoming):**

- `lumina.part_serial_documents.part_serial_document_id` → `part_serial_document_id`

### lumina.part_serial_master_list

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.part_xref_to_pick_history

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `pick_number` → `lumina.condition_pick_table.part_number`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`

### lumina.parts_customs_tariff_codes

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `customs_tariff_code` → `lumina.customs_tariff_codes.customs_tariff_code`

### lumina.parts_freight_tiered_markups

**References (Outgoing):**

- `freight_cost_markup_id` → `lumina.freight_cost_markups.freight_cost_markup_id`

### lumina.parts_received_without_cost

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `order_number` → `lumina.batch_orders.batch_number`

### lumina.parts_requiring_export_licence

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.payment_types

**References (Outgoing):**

- `payment_code` → `lumina.payment_types.payment_code`

**Referenced By (Incoming):**

- `lumina.oeim_invoice_snap_pay_types.payment_code` → `payment_code`
- `lumina.payment_types.payment_code` → `payment_code`

### lumina.pdc_import_index

**References (Outgoing):**

- `report_id` → `lumina.amp_report_documents.fleet`

### lumina.pick_hist_7890_bkp

**References (Outgoing):**

- `alternate_part_number` → `lumina.alternate_parts.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `pick_number` → `lumina.condition_pick_table.part_number`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`

### lumina.pick_history

**References (Outgoing):**

- `alternate_part_number` → `lumina.alternate_parts.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `pick_number` → `lumina.condition_pick_table.part_number`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`

### lumina.pirep_index_data

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.planners_notes

**References (Outgoing):**

- `status_id` → `lumina.amp_revision_status.revision_status_id`
- `category_id` → `lumina.maint_cost_time_category_set.category_set_id`
- `notes_xref_id` → `lumina.planners_notes_xref.category_xref_id`

**Referenced By (Incoming):**

- `lumina.requirements.planner_id` → `notes_xref_id`

### lumina.planners_notes_categories

**References (Outgoing):**

- `category_id` → `lumina.maint_cost_time_category_set.category_set_id`

**Referenced By (Incoming):**

- `lumina.variations.planners_notes_cat_id` → `category_id`

### lumina.planners_notes_statuses

**References (Outgoing):**

- `status_id` → `lumina.amp_revision_status.revision_status_id`

### lumina.planners_notes_xref

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `alert_number` → `lumina.alert_colors.alert_type_id`
- `visit_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `workcard_interval_id` → `lumina.amp_workcard_intervals.workcard_interval_id`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`

**Referenced By (Incoming):**

- `lumina.planners_notes.notes_xref_id` → `category_xref_id`
- `lumina.variations_xref.planners_notes_xref_id` → `category_xref_id`

### lumina.prefered_bins

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.preferred_suppliers_by_part

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.preorder_line_requirement_xref

**References (Outgoing):**

- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`
- `preorder_id` → `lumina.preorder_line_requirement_xref.preorder_id`

**Referenced By (Incoming):**

- `lumina.order_change_history.preorder_id` → `preorder_id`
- `lumina.preorder_line_requirement_xref.preorder_id` → `preorder_id`
- `lumina.preorder_line_stock_info.preorder_id` → `preorder_id`
- `lumina.preorder_lines.preorder_id` → `preorder_id`
- `lumina.preorders.preorder_id` → `preorder_id`
- `lumina.sap_order_header.preorder_id` → `preorder_id`
- `lumina.sap_order_line.preorder_id` → `preorder_id`

### lumina.preorder_line_stock_info

**References (Outgoing):**

- `batch_number` → `lumina.batch_file_header.key`
- `bin_number` → `lumina.bins.bin_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `movement_code` → `lumina.component_movement_hist_life.part_number`
- `preorder_id` → `lumina.preorder_line_requirement_xref.preorder_id`

### lumina.preorder_lines

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `vat_code` → `lumina.amp_workcard_activations.workcard_activation_id`
- `condition_code` → `lumina.condition_codes.condition_code`
- `non_stock_part_number` → `lumina.non_stock_parts.part_number`
- `preorder_id` → `lumina.preorder_line_requirement_xref.preorder_id`
- `release_code` → `lumina.release_codes.release_code`

### lumina.preorders

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `company_code` → `lumina.company_codes.company_code`
- `currency_code` → `lumina.currency_codes.currency_code`
- `employee_number` → `lumina.defect_stage_employees.defect_id`
- `preorder_id` → `lumina.preorder_line_requirement_xref.preorder_id`

### lumina.price_codes

**References (Outgoing):**

- `price_code` → `lumina.price_codes.price_code`

**Referenced By (Incoming):**

- `lumina.price_codes.price_code` → `price_code`

### lumina.price_types

**References (Outgoing):**

- `price_type_code` → `lumina.price_types.price_type_code`

**Referenced By (Incoming):**

- `lumina.ie96_historic.price_type_code` → `price_type_code`
- `lumina.price_types.price_type_code` → `price_type_code`
- `lumina.sales_prices.price_type_code` → `price_type_code`

### lumina.public_holidays

**Referenced By (Incoming):**

- `lumina.rp_block_resource_days.day_id` → `holiday_date`
- `lumina.rp_block_resource_days.day_number` → `holiday_date`

### lumina.purchase_demand_by_part

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.quote_email_chasing

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`

### lumina.quotes_by_part

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `currency_code` → `lumina.currency_codes.currency_code`

### lumina.quotes_for_part_by_account

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.random_stock_check_bins

**References (Outgoing):**

- `warehouse_code` → `lumina.account_available_warehouses.account_code`
- `bin_number` → `lumina.bins.bin_number`

**Referenced By (Incoming):**

- `lumina.non_stock_parts.stock_check_code` → `warehouse_code`
- `lumina.non_stock_parts_bkp_oases382.stock_check_code` → `warehouse_code`
- `lumina.part_master.stock_check_code` → `warehouse_code`
- `lumina.part_master_bkp_oases382.stock_check_code` → `warehouse_code`

### lumina.random_stock_check_date

**References (Outgoing):**

- `warehouse_code` → `lumina.account_available_warehouses.account_code`

### lumina.random_stock_check_log

**References (Outgoing):**

- `warehouse_code` → `lumina.account_available_warehouses.account_code`

### lumina.random_stock_check_parts

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `warehouse_code` → `lumina.account_available_warehouses.account_code`

### lumina.rd_xref_to_tech_logs

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `alert_number` → `lumina.alert_colors.alert_type_id`
- `status_code` → `lumina.amp_revision_status.revision_status_id`
- `key_id` → `lumina.osys_key_to_reportid.osyskey`

### lumina.rdi_history

**References (Outgoing):**

- `alert_number` → `lumina.alert_colors.alert_type_id`
- `user_id` → `lumina.dataset_locks_by_user.user_id`

**Referenced By (Incoming):**

- `lumina.rdi_to_nrc.rdi_number` → `alert_number`

### lumina.rdi_to_nrc

**References (Outgoing):**

- `nrc_number` → `lumina.cq_quote_nrc_access_panels.quote_id`
- `rdi_number` → `lumina.rdi_history.alert_number`

### lumina.release_codes

**References (Outgoing):**

- `release_code` → `lumina.release_codes.release_code`

**Referenced By (Incoming):**

- `lumina.order_header_1.release_code` → `release_code`
- `lumina.order_line_additional_info.release_code` → `release_code`
- `lumina.preorder_lines.release_code` → `release_code`
- `lumina.release_codes.release_code` → `release_code`
- `lumina.requests_for_quotes_lines.release_code` → `release_code`

### lumina.release_to_service_statement

**Referenced By (Incoming):**

- `lumina.account_location_header_6.state_code` → `release_statement`

### lumina.reliability_report_logo_desc

**References (Outgoing):**

- `document_image_id` → `lumina.document_image_source.document_image_source_id`
- `logo_desc_id` → `lumina.reliability_report_logo_desc.logo_desc_id`

**Referenced By (Incoming):**

- `lumina.reliability_report_logo_desc.logo_desc_id` → `logo_desc_id`

### lumina.removals

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.repair_approval_data

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `batch_number` → `lumina.batch_file_header.key`
- `movement_code` → `lumina.component_movement_hist_life.part_number`

### lumina.repetitive_defect_header_1

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `alert_number` → `lumina.alert_colors.alert_type_id`

### lumina.repetitive_defect_header_2

**References (Outgoing):**

- `alert_number` → `lumina.alert_colors.alert_type_id`

### lumina.repetitive_defect_narrative

**References (Outgoing):**

- `alert_number` → `lumina.alert_colors.alert_type_id`
- `user_id` → `lumina.dataset_locks_by_user.user_id`

### lumina.repetitive_defect_tech_logs

**References (Outgoing):**

- `alert_number` → `lumina.alert_colors.alert_type_id`
- `sequence_number` → `lumina.nrc_high_sequence_control.key_id`

### lumina.req_priority_desc_oases_1228

**References (Outgoing):**

- `priority_id` → `lumina.req_priority_desc_oases_1228.priority_id`

**Referenced By (Incoming):**

- `lumina.req_priority_desc_oases_1228.priority_id` → `priority_id`
- `lumina.requirement_priority_codes.priority_code` → `priority_id`
- `lumina.requirement_priority_desc.priority_id` → `priority_id`
- `lumina.requirement_priority_leadtimes.priority_code` → `priority_id`
- `lumina.requirement_priority_sla.priority_code` → `priority_id`

### lumina.requests_for_quotes

**References (Outgoing):**

- `rfq_number` → `lumina.requirement_to_rfq_xref.requirement_number`

### lumina.requests_for_quotes_lines

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `movement_code` → `lumina.component_movement_hist_life.part_number`
- `release_code` → `lumina.release_codes.release_code`
- `rfq_number` → `lumina.requirement_to_rfq_xref.requirement_number`

### lumina.requests_for_quotes_notes

**References (Outgoing):**

- `rfq_number` → `lumina.requirement_to_rfq_xref.requirement_number`

### lumina.requirement_planners_notes

**References (Outgoing):**

- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`

### lumina.requirement_priority_codes

**References (Outgoing):**

- `priority_code` → `lumina.req_priority_desc_oases_1228.priority_id`

### lumina.requirement_priority_desc

**References (Outgoing):**

- `priority_id` → `lumina.req_priority_desc_oases_1228.priority_id`

### lumina.requirement_priority_leadtimes

**References (Outgoing):**

- `priority_code` → `lumina.req_priority_desc_oases_1228.priority_id`

### lumina.requirement_priority_sla

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `priority_code` → `lumina.req_priority_desc_oases_1228.priority_id`

### lumina.requirement_recharge_details

**References (Outgoing):**

- `batch_number` → `lumina.batch_file_header.key`
- `cost_code` → `lumina.cost_codes.id`
- `currency_code` → `lumina.currency_codes.currency_code`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`
- `strip_report_number` → `lumina.strip_report_findings_text.strip_report_number`

### lumina.requirement_source_codes

**References (Outgoing):**

- `source_code` → `lumina.document_image_source.document_image_source_id`

### lumina.requirement_to_rfq_xref

**References (Outgoing):**

- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`
- `rfq_number` → `lumina.requirement_to_rfq_xref.requirement_number`

**Referenced By (Incoming):**

- `lumina.requests_for_quotes.rfq_number` → `requirement_number`
- `lumina.requests_for_quotes_lines.rfq_number` → `requirement_number`
- `lumina.requests_for_quotes_notes.rfq_number` → `requirement_number`
- `lumina.requirement_to_rfq_xref.rfq_number` → `requirement_number`
- `lumina.rfq_by_part_number.rfq_number` → `requirement_number`
- `lumina.rfq_history.rfq_number` → `requirement_number`
- `lumina.rfq_quote_received.rfq_number` → `requirement_number`
- `lumina.rfq_quote_received_notes.rfq_number` → `requirement_number`
- `lumina.rfq_requirement_xref.rfq_number` → `requirement_number`
- `lumina.rfq_supplier_details.rfq_number` → `requirement_number`
- `lumina.rfq_supplier_notes.rfq_number` → `requirement_number`
- `lumina.rfq_to_order_xref.rfq_number` → `requirement_number`
- `lumina.sales_request_quote_detail.rfq_number` → `requirement_number`

### lumina.requirements

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `alert_number` → `lumina.alert_colors.alert_type_id`
- `cfd_number` → `lumina.cfd_categories.cfd_category`
- `sales_order_number` → `lumina.customer_sales_order_xref.customer_sales_order_number`
- `defect_number` → `lumina.defect_extensions.defect_id`
- `defect_id` → `lumina.defect_extensions.defect_id`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`
- `planner_id` → `lumina.planners_notes.notes_xref_id`

### lumina.rfc_accomplishment

**References (Outgoing):**

- `accomplishment_code` → `lumina.accomplishment_history.accomplishment_id`

### lumina.rfc_aircraft

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `na_id` → `lumina.alternate_parts.part_number`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `paragraph_id` → `lumina.paragraph_cancels.rfc_id`
- `frequency_id` → `lumina.rfc_frequency_phase_header.rfc_id`

### lumina.rfc_change_origin

**References (Outgoing):**

- `change_origin_code` → `lumina.rfc_change_origin.change_origin_code`

**Referenced By (Incoming):**

- `lumina.rfc_change_origin.change_origin_code` → `change_origin_code`
- `lumina.rfc_download_origin_codes.change_origin_code` → `change_origin_code`
- `lumina.rfc_header.change_origin_code` → `change_origin_code`
- `lumina.rfc_status.change_origin_code` → `change_origin_code`

### lumina.rfc_components

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `na_id` → `lumina.alternate_parts.part_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `paragraph_id` → `lumina.paragraph_cancels.rfc_id`
- `frequency_id` → `lumina.rfc_frequency_phase_header.rfc_id`

### lumina.rfc_documents

**References (Outgoing):**

- `document_image_id` → `lumina.document_image_source.document_image_source_id`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `rfc_document_id` → `lumina.rfc_documents.rfc_document_id`

**Referenced By (Incoming):**

- `lumina.rfc_documents.rfc_document_id` → `rfc_document_id`

### lumina.rfc_download_effectivity

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `taxonomy_id` → `lumina.rfc_download_taxonomy.taxonomy_id`

### lumina.rfc_download_origin_codes

**References (Outgoing):**

- `accomplishment_code` → `lumina.accomplishment_history.accomplishment_id`
- `change_origin_code` → `lumina.rfc_change_origin.change_origin_code`
- `authority_code` → `lumina.rfc_regulating_authority.authority_code`

### lumina.rfc_download_taxonomy

**References (Outgoing):**

- `taxonomy_id` → `lumina.rfc_download_taxonomy.taxonomy_id`
- `authority_code` → `lumina.rfc_regulating_authority.authority_code`

**Referenced By (Incoming):**

- `lumina.rfc_download_effectivity.taxonomy_id` → `taxonomy_id`
- `lumina.rfc_download_taxonomy.taxonomy_id` → `taxonomy_id`

### lumina.rfc_effectivity_ata

**References (Outgoing):**

- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`

### lumina.rfc_effectivity_fleet

**References (Outgoing):**

- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`

### lumina.rfc_effectivity_part

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`

### lumina.rfc_evaluation_history

**References (Outgoing):**

- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `evaluation_history_id` → `lumina.rfc_evaluation_history.evaluation_history_id`

**Referenced By (Incoming):**

- `lumina.rfc_evaluation_history.evaluation_history_id` → `evaluation_history_id`

### lumina.rfc_evaluation_stages

**References (Outgoing):**

- `stage_code` → `lumina.amp_component_intervals_stages.component_interval_id`

### lumina.rfc_frequency_phase_header

**References (Outgoing):**

- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `paragraph_id` → `lumina.paragraph_cancels.rfc_id`
- `frequency_id` → `lumina.rfc_frequency_phase_header.rfc_id`

**Referenced By (Incoming):**

- `lumina.amp_workcard_h3_7487bkp.phase_code` → `rfc_id`
- `lumina.amp_workcard_header_3.phase_code` → `rfc_id`
- `lumina.dmg_rpr_inspections.frequency_id` → `rfc_id`
- `lumina.dmg_rpr_interim_repairs.frequency_id` → `rfc_id`
- `lumina.dmg_rpr_permanent_repairs.frequency_id` → `rfc_id`
- `lumina.dmg_rpr_time_limited_repairs.frequency_id` → `rfc_id`
- `lumina.maint_cost_budget_adsb.frequency_id` → `rfc_id`
- `lumina.maint_cost_budget_adsb.phase_number` → `rfc_id`
- `lumina.rfc_aircraft.frequency_id` → `rfc_id`
- `lumina.rfc_components.frequency_id` → `rfc_id`
- `lumina.rfc_frequency_phase_header.frequency_id` → `rfc_id`
- `lumina.rfc_frequency_phase_limits.frequency_id` → `rfc_id`
- `lumina.rfc_frequency_phases.frequency_id` → `rfc_id`
- `lumina.wcr_temp_base1.phase_code` → `rfc_id`

### lumina.rfc_frequency_phase_limits

**References (Outgoing):**

- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`
- `paragraph_id` → `lumina.paragraph_cancels.rfc_id`
- `frequency_id` → `lumina.rfc_frequency_phase_header.rfc_id`

### lumina.rfc_frequency_phases

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `paragraph_id` → `lumina.paragraph_cancels.rfc_id`
- `frequency_id` → `lumina.rfc_frequency_phase_header.rfc_id`

### lumina.rfc_header

**References (Outgoing):**

- `accomplishment_code` → `lumina.accomplishment_history.accomplishment_id`
- `section_id` → `lumina.amp_workcard_sections.section_id`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `change_origin_code` → `lumina.rfc_change_origin.change_origin_code`
- `authority_code` → `lumina.rfc_regulating_authority.authority_code`

### lumina.rfc_header_publications

**References (Outgoing):**

- `publication_code` → `lumina.amp_workcard_publications.publication_id`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`

### lumina.rfc_na_notes

**References (Outgoing):**

- `na_id` → `lumina.alternate_parts.part_number`
- `na_code` → `lumina.alternate_parts.part_number`

### lumina.rfc_paragraphs

**References (Outgoing):**

- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `paragraph_id` → `lumina.paragraph_cancels.rfc_id`

### lumina.rfc_policies

**References (Outgoing):**

- `policy_id` → `lumina.security_policy.policy_id`

### lumina.rfc_print_history_log

**References (Outgoing):**

- `log_id` → `lumina.amp_data_migration_log.log_number`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`

### lumina.rfc_publications

**References (Outgoing):**

- `publication_code` → `lumina.amp_workcard_publications.publication_id`

### lumina.rfc_regulating_authority

**References (Outgoing):**

- `authority_code` → `lumina.rfc_regulating_authority.authority_code`

**Referenced By (Incoming):**

- `lumina.consumable_history.authority_code` → `authority_code`
- `lumina.rfc_download_origin_codes.authority_code` → `authority_code`
- `lumina.rfc_download_taxonomy.authority_code` → `authority_code`
- `lumina.rfc_header.authority_code` → `authority_code`
- `lumina.rfc_regulating_authority.authority_code` → `authority_code`

### lumina.rfc_relationships

**References (Outgoing):**

- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`

### lumina.rfc_statement_sections

**References (Outgoing):**

- `section_id` → `lumina.amp_workcard_sections.section_id`
- `section_code` → `lumina.amp_workcard_sections.section_id`

### lumina.rfc_status

**References (Outgoing):**

- `permission_id` → `lumina.add_extension_permissions.user_id`
- `stage_code` → `lumina.amp_component_intervals_stages.component_interval_id`
- `change_origin_code` → `lumina.rfc_change_origin.change_origin_code`

### lumina.rfc_transaction_log

**References (Outgoing):**

- `log_id` → `lumina.amp_data_migration_log.log_number`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`

### lumina.rfq_by_part_number

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `rfq_number` → `lumina.requirement_to_rfq_xref.requirement_number`

### lumina.rfq_history

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `condition_code` → `lumina.condition_codes.condition_code`
- `currency_code` → `lumina.currency_codes.currency_code`
- `rfq_number` → `lumina.requirement_to_rfq_xref.requirement_number`

### lumina.rfq_quote_received

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `currency_code` → `lumina.currency_codes.currency_code`
- `rfq_number` → `lumina.requirement_to_rfq_xref.requirement_number`

### lumina.rfq_quote_received_notes

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `rfq_number` → `lumina.requirement_to_rfq_xref.requirement_number`

### lumina.rfq_requirement_xref

**References (Outgoing):**

- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`
- `rfq_number` → `lumina.requirement_to_rfq_xref.requirement_number`

### lumina.rfq_supplier_details

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `rfq_number` → `lumina.requirement_to_rfq_xref.requirement_number`

### lumina.rfq_supplier_notes

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `rfq_number` → `lumina.requirement_to_rfq_xref.requirement_number`

### lumina.rfq_to_order_xref

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `order_number` → `lumina.batch_orders.batch_number`
- `rfq_number` → `lumina.requirement_to_rfq_xref.requirement_number`

### lumina.rotable_batch_locations

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `batch_number` → `lumina.batch_file_header.key`
- `bin_number` → `lumina.bins.bin_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `movement_code` → `lumina.component_movement_hist_life.part_number`
- `long_serial_number` → `lumina.long_serial_number_xref.part_number`

**Referenced By (Incoming):**

- `lumina.works_order_issues_and_returns.rotable_batch_number` → `id`
- `lumina.works_order_issues_and_rtn_bac.rotable_batch_number` → `id`

### lumina.rotable_float_values

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.rotable_history

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `movement_code` → `lumina.component_movement_hist_life.part_number`
- `delivery_note_number` → `lumina.delivery_note_extended_remarks.delivery_note_number`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`

**Referenced By (Incoming):**

- `lumina.shipment_demands.rotable_history_id` → `id`

### lumina.rotables_below_re_order

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.rp_base_plan_header

**References (Outgoing):**

- `base_plan_id` → `lumina.rp_base_plan_header.base_plan_id`

**Referenced By (Incoming):**

- `lumina.rp_base_plan_header.base_plan_id` → `base_plan_id`
- `lumina.rp_wo_base_estimated_defects.base_plan_id` → `base_plan_id`
- `lumina.rp_wo_base_milestones.base_plan_id` → `base_plan_id`
- `lumina.rp_wo_base_nrc_plan.base_plan_id` → `base_plan_id`
- `lumina.rp_wo_base_workcard_plan.base_plan_id` → `base_plan_id`

### lumina.rp_basic_shift

**References (Outgoing):**

- `basic_shift_id` → `lumina.rp_basic_shift.basic_shift_id`

**Referenced By (Incoming):**

- `lumina.rp_basic_shift.basic_shift_id` → `basic_shift_id`
- `lumina.rp_block_resource.shift_id` → `basic_shift_id`
- `lumina.rp_employee_allocation_header.basic_shift_id` → `basic_shift_id`
- `lumina.rp_employee_calendar_addition.shift_id` → `basic_shift_id`
- `lumina.rp_wo_base_estimated_defects.basic_shift_id` → `basic_shift_id`
- `lumina.rp_wo_base_nrc_plan.basic_shift_id` → `basic_shift_id`
- `lumina.rp_wo_base_workcard_plan.basic_shift_id` → `basic_shift_id`
- `lumina.rp_wo_estimated_defects.basic_shift_id` → `basic_shift_id`
- `lumina.rp_wo_nrc_plan.basic_shift_id` → `basic_shift_id`
- `lumina.rp_wo_workcard_plan.basic_shift_id` → `basic_shift_id`

### lumina.rp_block_resource

**References (Outgoing):**

- `warehouse_code` → `lumina.account_available_warehouses.account_code`
- `block_id` → `lumina.block_countries.block_code`
- `shift_id` → `lumina.rp_basic_shift.basic_shift_id`
- `scope_type_id` → `lumina.scope_type_rating.scope_type_id`
- `trade_code` → `lumina.trades.trade_code`

### lumina.rp_block_resource_days

**References (Outgoing):**

- `block_id` → `lumina.block_countries.block_code`
- `day_id` → `lumina.public_holidays.holiday_date`
- `day_number` → `lumina.public_holidays.holiday_date`

### lumina.rp_calendar_addition_type

**References (Outgoing):**

- `type_id` → `lumina.aircraft_types.aircraft_type`

### lumina.rp_dependencies

**References (Outgoing):**

- `type_id` → `lumina.aircraft_types.aircraft_type`
- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `milestone_id` → `lumina.rp_milestone_history.history_id`

### lumina.rp_employee_allocation

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `nrc_number` → `lumina.cq_quote_nrc_access_panels.quote_id`
- `allocation_id` → `lumina.order_requirement_allocation.order_number`
- `allocation_header_id` → `lumina.rp_employee_allocation_header.allocation_header_id`

### lumina.rp_employee_allocation_header

**References (Outgoing):**

- `employee_number` → `lumina.defect_stage_employees.defect_id`
- `basic_shift_id` → `lumina.rp_basic_shift.basic_shift_id`
- `allocation_header_id` → `lumina.rp_employee_allocation_header.allocation_header_id`

**Referenced By (Incoming):**

- `lumina.rp_employee_allocation.allocation_header_id` → `allocation_header_id`
- `lumina.rp_employee_allocation_header.allocation_header_id` → `allocation_header_id`

### lumina.rp_employee_calendar_addition

**References (Outgoing):**

- `warehouse_code` → `lumina.account_available_warehouses.account_code`
- `type_id` → `lumina.aircraft_types.aircraft_type`
- `employee_number` → `lumina.defect_stage_employees.defect_id`
- `addition_id` → `lumina.order_line_additional_info.order_number`
- `shift_id` → `lumina.rp_basic_shift.basic_shift_id`

### lumina.rp_employee_calendar_pattern

**References (Outgoing):**

- `warehouse_code` → `lumina.account_available_warehouses.account_code`
- `employee_number` → `lumina.defect_stage_employees.defect_id`
- `shift_pattern_id` → `lumina.rp_shift_pattern.shift_pattern_id`

### lumina.rp_milestone_history

**References (Outgoing):**

- `history_id` → `lumina.accomplishment_history.accomplishment_id`
- `milestone_id` → `lumina.rp_milestone_history.history_id`

**Referenced By (Incoming):**

- `lumina.rp_dependencies.milestone_id` → `history_id`
- `lumina.rp_milestone_history.milestone_id` → `history_id`
- `lumina.rp_milestones.milestone_id` → `history_id`
- `lumina.rp_milestones.milestone_code` → `history_id`
- `lumina.rp_wo_base_milestones.milestone_id` → `history_id`
- `lumina.rp_wo_milestones.milestone_id` → `history_id`

### lumina.rp_milestones

**References (Outgoing):**

- `milestone_id` → `lumina.rp_milestone_history.history_id`
- `milestone_code` → `lumina.rp_milestone_history.history_id`

### lumina.rp_shift_pattern

**References (Outgoing):**

- `shift_pattern_id` → `lumina.rp_shift_pattern.shift_pattern_id`

**Referenced By (Incoming):**

- `lumina.rp_employee_calendar_pattern.shift_pattern_id` → `shift_pattern_id`
- `lumina.rp_shift_pattern.shift_pattern_id` → `shift_pattern_id`
- `lumina.rp_shift_pattern_header.shift_pattern_id` → `shift_pattern_id`

### lumina.rp_shift_pattern_header

**References (Outgoing):**

- `shift_pattern_id` → `lumina.rp_shift_pattern.shift_pattern_id`

### lumina.rp_weekends

**References (Outgoing):**

- `weekends_id` → `lumina.rp_weekends.weekends_id`

**Referenced By (Incoming):**

- `lumina.rp_weekends.weekends_id` → `weekends_id`

### lumina.rp_wo_base_estimated_defects

**References (Outgoing):**

- `base_plan_id` → `lumina.rp_base_plan_header.base_plan_id`
- `basic_shift_id` → `lumina.rp_basic_shift.basic_shift_id`
- `trade_code` → `lumina.trades.trade_code`

### lumina.rp_wo_base_milestones

**References (Outgoing):**

- `base_plan_id` → `lumina.rp_base_plan_header.base_plan_id`
- `milestone_id` → `lumina.rp_milestone_history.history_id`

### lumina.rp_wo_base_nrc_plan

**References (Outgoing):**

- `nrc_number` → `lumina.cq_quote_nrc_access_panels.quote_id`
- `base_plan_id` → `lumina.rp_base_plan_header.base_plan_id`
- `basic_shift_id` → `lumina.rp_basic_shift.basic_shift_id`

### lumina.rp_wo_base_workcard_plan

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `base_plan_id` → `lumina.rp_base_plan_header.base_plan_id`
- `basic_shift_id` → `lumina.rp_basic_shift.basic_shift_id`

### lumina.rp_wo_estimated_defects

**References (Outgoing):**

- `basic_shift_id` → `lumina.rp_basic_shift.basic_shift_id`
- `trade_code` → `lumina.trades.trade_code`

### lumina.rp_wo_milestones

**References (Outgoing):**

- `milestone_id` → `lumina.rp_milestone_history.history_id`

### lumina.rp_wo_nrc_plan

**References (Outgoing):**

- `nrc_number` → `lumina.cq_quote_nrc_access_panels.quote_id`
- `basic_shift_id` → `lumina.rp_basic_shift.basic_shift_id`

### lumina.rp_wo_workcard_plan

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `basic_shift_id` → `lumina.rp_basic_shift.basic_shift_id`

### lumina.sabre_flight_map

**References (Outgoing):**

- `report_id` → `lumina.amp_report_documents.fleet`

### lumina.sabre_trace

**References (Outgoing):**

- `trace_id` → `lumina.easa_trace.trace_id`

### lumina.sage_order_line_details

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`

### lumina.sales_history

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `condition_code` → `lumina.condition_codes.condition_code`
- `currency_code` → `lumina.currency_codes.currency_code`
- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.sales_invoice_genled_xref

**References (Outgoing):**

- `end_use_code` → `lumina.end_use_codes.end_use_code`

### lumina.sales_invoices_xref

**References (Outgoing):**

- `sales_order_number` → `lumina.customer_sales_order_xref.customer_sales_order_number`
- `invoice_number` → `lumina.invoice_categories.invoice_category`

### lumina.sales_notes_for_part

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.sales_order_dispatches

**References (Outgoing):**

- `batch_number` → `lumina.batch_file_header.key`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `sales_order_number` → `lumina.customer_sales_order_xref.customer_sales_order_number`
- `delivery_note_number` → `lumina.delivery_note_extended_remarks.delivery_note_number`
- `sales_order_dispatch_number` → `lumina.sales_order_dispatches.sales_order_number`

**Referenced By (Incoming):**

- `lumina.sales_order_dispatches.sales_order_dispatch_number` → `sales_order_number`
- `lumina.sales_order_payments.sales_order_dispatch_number` → `sales_order_number`

### lumina.sales_order_history

**References (Outgoing):**

- `sales_request_number` → `lumina.sales_request_quote_detail.sales_request_number`

### lumina.sales_order_lines

**References (Outgoing):**

- `sales_order_number` → `lumina.customer_sales_order_xref.customer_sales_order_number`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`
- `sales_request_number` → `lumina.sales_request_quote_detail.sales_request_number`

### lumina.sales_order_notes

**References (Outgoing):**

- `sales_order_number` → `lumina.customer_sales_order_xref.customer_sales_order_number`

### lumina.sales_order_parameters

**References (Outgoing):**

- `key_id` → `lumina.osys_key_to_reportid.osyskey`

### lumina.sales_order_payments

**References (Outgoing):**

- `sales_order_number` → `lumina.customer_sales_order_xref.customer_sales_order_number`
- `user_id` → `lumina.dataset_locks_by_user.user_id`
- `sales_order_dispatch_number` → `lumina.sales_order_dispatches.sales_order_number`

### lumina.sales_orders

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `company_code` → `lumina.company_codes.company_code`
- `currency_code` → `lumina.currency_codes.currency_code`
- `sales_order_number` → `lumina.customer_sales_order_xref.customer_sales_order_number`

### lumina.sales_orders_by_part

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `sales_order_number` → `lumina.customer_sales_order_xref.customer_sales_order_number`

### lumina.sales_prices

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `condition_code` → `lumina.condition_codes.condition_code`
- `currency_code` → `lumina.currency_codes.currency_code`
- `price_type_code` → `lumina.price_types.price_type_code`
- `transaction_type_code` → `lumina.transaction_types.transaction_type_code`

### lumina.sales_quotes_out_history

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `condition_code` → `lumina.condition_codes.condition_code`
- `currency_code` → `lumina.currency_codes.currency_code`
- `sales_request_number` → `lumina.sales_request_quote_detail.sales_request_number`

### lumina.sales_request_quote_detail

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `sales_order_number` → `lumina.customer_sales_order_xref.customer_sales_order_number`
- `rfq_number` → `lumina.requirement_to_rfq_xref.requirement_number`
- `sales_request_number` → `lumina.sales_request_quote_detail.sales_request_number`

**Referenced By (Incoming):**

- `lumina.sales_order_history.sales_request_number` → `sales_request_number`
- `lumina.sales_order_lines.sales_request_number` → `sales_request_number`
- `lumina.sales_quotes_out_history.sales_request_number` → `sales_request_number`
- `lumina.sales_request_quote_detail.sales_request_number` → `sales_request_number`
- `lumina.sales_request_quote_header.sales_request_number` → `sales_request_number`
- `lumina.sales_request_quote_notes.sales_request_number` → `sales_request_number`
- `lumina.sales_requested_unknown_parts.sales_request_number` → `sales_request_number`
- `lumina.sales_requests_by_part.sales_request_number` → `sales_request_number`
- `lumina.sales_requests_by_unknown_part.sales_request_number` → `sales_request_number`

### lumina.sales_request_quote_header

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `company_code` → `lumina.company_codes.company_code`
- `currency_code` → `lumina.currency_codes.currency_code`
- `user_id` → `lumina.dataset_locks_by_user.user_id`
- `sales_request_number` → `lumina.sales_request_quote_detail.sales_request_number`

### lumina.sales_request_quote_notes

**References (Outgoing):**

- `sales_request_number` → `lumina.sales_request_quote_detail.sales_request_number`

### lumina.sales_requested_unknown_parts

**References (Outgoing):**

- `sales_request_number` → `lumina.sales_request_quote_detail.sales_request_number`

**Referenced By (Incoming):**

- `lumina.sales_requests_by_unknown_part.unknown_part_number` → `sales_request_number`
- `lumina.unknown_part_numbers.unknown_part_number` → `sales_request_number`

### lumina.sales_requests_by_part

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `sales_request_number` → `lumina.sales_request_quote_detail.sales_request_number`

### lumina.sales_requests_by_unknown_part

**References (Outgoing):**

- `sales_request_number` → `lumina.sales_request_quote_detail.sales_request_number`
- `unknown_part_number` → `lumina.sales_requested_unknown_parts.sales_request_number`

### lumina.sample_fleets

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `fleet_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`

### lumina.sample_fleets_jn

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `fleet_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`

### lumina.sap_order_header

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`
- `preorder_id` → `lumina.preorder_line_requirement_xref.preorder_id`

### lumina.sap_order_line

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`
- `preorder_id` → `lumina.preorder_line_requirement_xref.preorder_id`

### lumina.schedule_forecast_xref

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `workcard_id` → `lumina.amp_access_panels_by_workcard.fleet`
- `visit_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `workcard_interval_id` → `lumina.amp_workcard_intervals.workcard_interval_id`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`

### lumina.schedule_source

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`

### lumina.scope_type_rating

**References (Outgoing):**

- `scope_type_id` → `lumina.scope_type_rating.scope_type_id`

**Referenced By (Incoming):**

- `lumina.employees_licences.scope_type_id` → `scope_type_id`
- `lumina.rp_block_resource.scope_type_id` → `scope_type_id`
- `lumina.scope_type_rating.scope_type_id` → `scope_type_id`

### lumina.sectors

**References (Outgoing):**

- `sector_id` → `lumina.flown_sectors.aircraft_code`

### lumina.security_audit_log_header

**References (Outgoing):**

- `permission_id` → `lumina.add_extension_permissions.user_id`
- `audit_log_id` → `lumina.security_audit_log_header.audit_log_id`

**Referenced By (Incoming):**

- `lumina.security_audit_log_header.audit_log_id` → `audit_log_id`
- `lumina.security_audit_log_meta_data.audit_log_id` → `audit_log_id`

### lumina.security_audit_log_meta_data

**References (Outgoing):**

- `sequence_number` → `lumina.nrc_high_sequence_control.key_id`
- `audit_log_id` → `lumina.security_audit_log_header.audit_log_id`

### lumina.security_group_perm_attribute

**References (Outgoing):**

- `permission_id` → `lumina.add_extension_permissions.user_id`
- `group_id` → `lumina.forecast_filter_groups.group_id`
- `attribute_id` → `lumina.security_group_perm_attribute.group_id`

**Referenced By (Incoming):**

- `lumina.security_group_perm_attribute.attribute_id` → `group_id`
- `lumina.security_permission_def_attrib.attribute_id` → `group_id`
- `lumina.security_policy_perm_attribute.attribute_id` → `group_id`
- `lumina.security_user_perm_attribute.attribute_id` → `group_id`

### lumina.security_group_permissions

**References (Outgoing):**

- `permission_id` → `lumina.add_extension_permissions.user_id`
- `group_id` → `lumina.forecast_filter_groups.group_id`

### lumina.security_group_policies

**References (Outgoing):**

- `group_id` → `lumina.forecast_filter_groups.group_id`
- `policy_id` → `lumina.security_policy.policy_id`

### lumina.security_groups

**References (Outgoing):**

- `group_id` → `lumina.forecast_filter_groups.group_id`

### lumina.security_permission_def_attrib

**References (Outgoing):**

- `permission_id` → `lumina.add_extension_permissions.user_id`
- `attribute_id` → `lumina.security_group_perm_attribute.group_id`

### lumina.security_policy

**References (Outgoing):**

- `policy_id` → `lumina.security_policy.policy_id`

**Referenced By (Incoming):**

- `lumina.cq_quote_status.policy_id` → `policy_id`
- `lumina.rfc_policies.policy_id` → `policy_id`
- `lumina.security_group_policies.policy_id` → `policy_id`
- `lumina.security_policy.policy_id` → `policy_id`
- `lumina.security_policy_perm_attribute.policy_id` → `policy_id`
- `lumina.security_policy_permissions.policy_id` → `policy_id`
- `lumina.security_user_policies.policy_id` → `policy_id`

### lumina.security_policy_perm_attribute

**References (Outgoing):**

- `permission_id` → `lumina.add_extension_permissions.user_id`
- `attribute_id` → `lumina.security_group_perm_attribute.group_id`
- `policy_id` → `lumina.security_policy.policy_id`

### lumina.security_policy_permissions

**References (Outgoing):**

- `permission_id` → `lumina.add_extension_permissions.user_id`
- `policy_id` → `lumina.security_policy.policy_id`

### lumina.security_user_effectivity

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `sub_fleet_id` → `lumina.sub_fleet_header.sub_fleet_id`

### lumina.security_user_groups

**References (Outgoing):**

- `group_id` → `lumina.forecast_filter_groups.group_id`

### lumina.security_user_notifications

**References (Outgoing):**

- `notification_id` → `lumina.email_notification.id`
- `user_notification_id` → `lumina.security_user_notifications.user_notification_id`

**Referenced By (Incoming):**

- `lumina.security_user_notifications.user_notification_id` → `user_notification_id`

### lumina.security_user_perm_attribute

**References (Outgoing):**

- `permission_id` → `lumina.add_extension_permissions.user_id`
- `attribute_id` → `lumina.security_group_perm_attribute.group_id`

### lumina.security_user_permissions

**References (Outgoing):**

- `permission_id` → `lumina.add_extension_permissions.user_id`

### lumina.security_user_permissions_bkp

**References (Outgoing):**

- `permission_id` → `lumina.add_extension_permissions.user_id`

### lumina.security_user_policies

**References (Outgoing):**

- `policy_id` → `lumina.security_policy.policy_id`

### lumina.serial_numbers_by_part

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.sfdc_activity

**References (Outgoing):**

- `activity_id` → `lumina.b737ng_activity_import_table.schedule_reference`
- `defect_stage_id` → `lumina.defect_stage_employees.defect_id`
- `licence_id` → `lumina.email_licence.license_id`
- `booking_id` → `lumina.oeim_booking_base_data.booking_rounding_up_mins`

### lumina.sfdc_bookings

**References (Outgoing):**

- `task_number` → `lumina.amp_datmig_comp_task_lookup.fleet`
- `defect_code` → `lumina.defect_extensions.defect_id`
- `employee_number` → `lumina.defect_stage_employees.defect_id`
- `booking_id` → `lumina.oeim_booking_base_data.booking_rounding_up_mins`

### lumina.sfdc_component_changes

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `component_change_id` → `lumina.sfdc_component_changes.component_change_id`

**Referenced By (Incoming):**

- `lumina.sfdc_component_changes.component_change_id` → `component_change_id`

### lumina.sfdc_deleted_bookings

**References (Outgoing):**

- `task_number` → `lumina.amp_datmig_comp_task_lookup.fleet`
- `defect_code` → `lumina.defect_extensions.defect_id`
- `employee_number` → `lumina.defect_stage_employees.defect_id`
- `sequence_number` → `lumina.nrc_high_sequence_control.key_id`

### lumina.sfdc_open_bookings

**References (Outgoing):**

- `task_number` → `lumina.amp_datmig_comp_task_lookup.fleet`
- `defect_code` → `lumina.defect_extensions.defect_id`
- `employee_number` → `lumina.defect_stage_employees.defect_id`

### lumina.shelf_li_dt_bkp_2020

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `component_life_limit_id` → `lumina.component_life_limits.component_life_limit_id`
- `shelf_life_date_id` → `lumina.shelf_life_dates.shelf_life_date_id`

### lumina.shelf_life_dates

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `component_life_limit_id` → `lumina.component_life_limits.component_life_limit_id`
- `shelf_life_date_id` → `lumina.shelf_life_dates.shelf_life_date_id`

**Referenced By (Incoming):**

- `lumina.shelf_li_dt_bkp_2020.shelf_life_date_id` → `shelf_life_date_id`
- `lumina.shelf_life_dates.shelf_life_date_id` → `shelf_life_date_id`
- `lumina.shelf_life_dates_oases6834.shelf_life_date_id` → `shelf_life_date_id`

### lumina.shelf_life_dates_oases6834

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `component_life_limit_id` → `lumina.component_life_limits.component_life_limit_id`
- `shelf_life_date_id` → `lumina.shelf_life_dates.shelf_life_date_id`

### lumina.shelf_life_expiry_req_codes

**References (Outgoing):**

- `requirement_code` → `lumina.nrc_requirements_actions.aircraft_short_reg`

### lumina.shipment

**References (Outgoing):**

- `company_code` → `lumina.company_codes.company_code`
- `currency_code` → `lumina.currency_codes.currency_code`
- `shipment_id` → `lumina.shipment.shipment_id`

**Referenced By (Incoming):**

- `lumina.airway_bill_references.shipment_id` → `shipment_id`
- `lumina.package.shipment_id` → `shipment_id`
- `lumina.shipment.shipment_id` → `shipment_id`
- `lumina.shipment_documents.shipment_id` → `shipment_id`
- `lumina.shipment_item.shipment_id` → `shipment_id`
- `lumina.shipment_status.shipment_id` → `shipment_id`

### lumina.shipment_demands

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `consumable_history_id` → `lumina.consumable_history.id`
- `reason_id` → `lumina.demand_reason_to_movement_code.id`
- `non_stock_part_number` → `lumina.non_stock_parts.part_number`
- `rotable_history_id` → `lumina.rotable_history.id`

### lumina.shipment_documents

**References (Outgoing):**

- `document_id` → `lumina.aircraft_documents.aircraft_document_id`
- `document_image_id` → `lumina.document_image_source.document_image_source_id`
- `shipment_id` → `lumina.shipment.shipment_id`

### lumina.shipment_item

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `shipment_id` → `lumina.shipment.shipment_id`
- `shipment_item_id` → `lumina.shipment_item.shipment_item_id`

**Referenced By (Incoming):**

- `lumina.freight_costs.shipment_item_id` → `shipment_item_id`
- `lumina.shipment_item.shipment_item_id` → `shipment_item_id`
- `lumina.shipment_item_customs.shipment_item_id` → `shipment_item_id`

### lumina.shipment_item_customs

**References (Outgoing):**

- `customs_entry_number` → `lumina.batches_by_customs_entry.customs_entry_number`
- `customs_status_code` → `lumina.customs_status_codes.customs_status`
- `shipment_item_id` → `lumina.shipment_item.shipment_item_id`

### lumina.shipment_item_demands

**References (Outgoing):**

- `item_id` → `lumina.delivery_note_item_header_1.delivery_note_number`
- `demand_id` → `lumina.demand_reason_to_movement_code.id`

### lumina.shipment_order_demands

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `order_number` → `lumina.batch_orders.batch_number`
- `demand_id` → `lumina.demand_reason_to_movement_code.id`

### lumina.shipment_requirement_demands

**References (Outgoing):**

- `pick_number` → `lumina.condition_pick_table.part_number`
- `demand_id` → `lumina.demand_reason_to_movement_code.id`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`

### lumina.shipment_status

**References (Outgoing):**

- `shipment_id` → `lumina.shipment.shipment_id`
- `shipment_status_id` → `lumina.shipment_status.shipment_status_id`
- `shipment_status_type_id` → `lumina.shipment_status_type.status_id`

**Referenced By (Incoming):**

- `lumina.shipment_status.shipment_status_id` → `shipment_status_id`

### lumina.shipment_status_type

**References (Outgoing):**

- `status_id` → `lumina.amp_revision_status.revision_status_id`

**Referenced By (Incoming):**

- `lumina.shipment_status.shipment_status_type_id` → `status_id`

### lumina.shipment_stocktransfer_demands

**References (Outgoing):**

- `demand_id` → `lumina.demand_reason_to_movement_code.id`

### lumina.shipment_works_orders_demands

**References (Outgoing):**

- `demand_id` → `lumina.demand_reason_to_movement_code.id`

### lumina.short_long_serials

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `long_serial_number` → `lumina.long_serial_number_xref.part_number`

### lumina.skill_codes

**References (Outgoing):**

- `skill_code` → `lumina.skill_codes.skill_code`

**Referenced By (Incoming):**

- `lumina.skill_codes.skill_code` → `skill_code`

### lumina.sold_hours_history

**References (Outgoing):**

- `defect_number` → `lumina.defect_extensions.defect_id`

### lumina.stock_audit_batches

**References (Outgoing):**

- `batch_number` → `lumina.batch_file_header.key`
- `bin_number` → `lumina.bins.bin_number`
- `stock_audit_id` → `lumina.stock_audit_batches.stock_audit_id`

**Referenced By (Incoming):**

- `lumina.stock_audit_batches.stock_audit_id` → `stock_audit_id`
- `lumina.stock_audit_bins.stock_audit_id` → `stock_audit_id`
- `lumina.stock_audits.stock_audit_id` → `stock_audit_id`

### lumina.stock_audit_bins

**References (Outgoing):**

- `bin_number` → `lumina.bins.bin_number`
- `stock_audit_id` → `lumina.stock_audit_batches.stock_audit_id`

### lumina.stock_audits

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `stock_audit_id` → `lumina.stock_audit_batches.stock_audit_id`

### lumina.stock_by_bin

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `bin_number` → `lumina.bins.bin_number`

### lumina.stock_documents

**References (Outgoing):**

- `batch_number` → `lumina.batch_file_header.key`
- `document_image_id` → `lumina.document_image_source.document_image_source_id`
- `stock_document_id` → `lumina.stock_documents.stock_document_id`

**Referenced By (Incoming):**

- `lumina.stock_documents.stock_document_id` → `stock_document_id`

### lumina.stock_group_additional_data

**References (Outgoing):**

- `end_use_code` → `lumina.end_use_codes.end_use_code`

### lumina.stock_groups

**References (Outgoing):**

- `vat_code` → `lumina.amp_workcard_activations.workcard_activation_id`

### lumina.stock_groups_bkp_oases382

**References (Outgoing):**

- `vat_code` → `lumina.amp_workcard_activations.workcard_activation_id`

### lumina.stock_works_order_markups

**References (Outgoing):**

- `works_order_number` → `lumina.credit_works_order_cards.credit_note_no`

### lumina.strip_documents

**References (Outgoing):**

- `document_image_id` → `lumina.document_image_source.document_image_source_id`
- `strip_document_id` → `lumina.strip_documents.strip_document_id`
- `strip_report_number` → `lumina.strip_report_findings_text.strip_report_number`

**Referenced By (Incoming):**

- `lumina.strip_documents.strip_document_id` → `strip_document_id`

### lumina.strip_report_findings_text

**References (Outgoing):**

- `strip_report_number` → `lumina.strip_report_findings_text.strip_report_number`

**Referenced By (Incoming):**

- `lumina.order_lines.strip_report_number` → `strip_report_number`
- `lumina.requirement_recharge_details.strip_report_number` → `strip_report_number`
- `lumina.strip_documents.strip_report_number` → `strip_report_number`
- `lumina.strip_report_findings_text.strip_report_number` → `strip_report_number`
- `lumina.strip_report_header_1.strip_report_number` → `strip_report_number`
- `lumina.strip_report_header_2.strip_report_number` → `strip_report_number`
- `lumina.strip_report_modification_text.strip_report_number` → `strip_report_number`

### lumina.strip_report_header_1

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `order_number` → `lumina.batch_orders.batch_number`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `works_order_number` → `lumina.credit_works_order_cards.credit_note_no`
- `currency_code` → `lumina.currency_codes.currency_code`
- `strip_report_number` → `lumina.strip_report_findings_text.strip_report_number`

### lumina.strip_report_header_2

**References (Outgoing):**

- `strip_report_number` → `lumina.strip_report_findings_text.strip_report_number`

### lumina.strip_report_modification_text

**References (Outgoing):**

- `strip_report_number` → `lumina.strip_report_findings_text.strip_report_number`

### lumina.structural_damage

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `defect_number` → `lumina.defect_extensions.defect_id`

### lumina.sub_fleet_header

**References (Outgoing):**

- `fleet_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `sub_fleet_id` → `lumina.sub_fleet_header.sub_fleet_id`

**Referenced By (Incoming):**

- `lumina.amp_access_panel_effectivity.sub_fleet_id` → `sub_fleet_id`
- `lumina.amp_accesspanel_effectivity_jn.sub_fleet_id` → `sub_fleet_id`
- `lumina.amp_material_effectivity.sub_fleet_id` → `sub_fleet_id`
- `lumina.amp_material_effectivity_jn.sub_fleet_id` → `sub_fleet_id`
- `lumina.amp_workcard_ac_effectivity.sub_fleet_id` → `sub_fleet_id`
- `lumina.amp_workcard_ac_effectivity_jn.sub_fleet_id` → `sub_fleet_id`
- `lumina.amp_workcard_intervals.sub_fleet_id` → `sub_fleet_id`
- `lumina.dmg_rpr_doc_effectivity.sub_fleet_id` → `sub_fleet_id`
- `lumina.dmg_rpr_document_order.sub_fleet_id` → `sub_fleet_id`
- `lumina.security_user_effectivity.sub_fleet_id` → `sub_fleet_id`
- `lumina.sub_fleet_header.sub_fleet_id` → `sub_fleet_id`
- `lumina.sub_fleets.sub_fleet_id` → `sub_fleet_id`
- `lumina.sub_fleets_jn.sub_fleet_id` → `sub_fleet_id`

### lumina.sub_fleets

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `sub_fleet_id` → `lumina.sub_fleet_header.sub_fleet_id`

### lumina.sub_fleets_jn

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `sub_fleet_id` → `lumina.sub_fleet_header.sub_fleet_id`

### lumina.supplier_loan_contract_rates

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.system_header_icarus

**References (Outgoing):**

- `key_id` → `lumina.osys_key_to_reportid.osyskey`

### lumina.talend_jobs

**References (Outgoing):**

- `talend_job_id` → `lumina.talend_jobs.talend_job_id`

**Referenced By (Incoming):**

- `lumina.talend_jobs.talend_job_id` → `talend_job_id`

### lumina.task_activity_link

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `visit_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.taskcard_wo_order_line

**References (Outgoing):**

- `order_number` → `lumina.batch_orders.batch_number`

### lumina.tech_log_1

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.tech_log_2

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `alert_number` → `lumina.alert_colors.alert_type_id`
- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`

### lumina.tech_log_3

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `report_id` → `lumina.amp_report_documents.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `corrosion_code` → `lumina.corrosion_categories.corrosion_code`
- `defect_id` → `lumina.defect_extensions.defect_id`
- `mel_revision_number` → `lumina.mel_revision_history.history_id`

### lumina.tech_log_defect_text

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.tech_log_documents

**References (Outgoing):**

- `report_id` → `lumina.amp_report_documents.fleet`
- `document_image_id` → `lumina.document_image_source.document_image_source_id`

### lumina.tech_log_nrc_xref

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.tech_log_rectification_text

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `sequence_number` → `lumina.nrc_high_sequence_control.key_id`

### lumina.tech_log_workcard_link

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`

### lumina.temp_rfc_paragraphs

**References (Outgoing):**

- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `paragraph_id` → `lumina.paragraph_cancels.rfc_id`

### lumina.test_table

**References (Outgoing):**

- `key_id` → `lumina.osys_key_to_reportid.osyskey`

### lumina.third_party_account_id

**References (Outgoing):**

- `account_id` → `lumina.access_dim_accounts_info.info_id`
- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.tiered_markup_range

**References (Outgoing):**

- `markup_code` → `lumina.freight_cost_markups.freight_cost_markup_id`

### lumina.time_categories

**References (Outgoing):**

- `contract_id` → `lumina.customer_contract_rates.contract_id`
- `time_category_id` → `lumina.maint_cost_time_category_set.category_set_id`

### lumina.tool_check_out_in

**References (Outgoing):**

- `task_number` → `lumina.amp_datmig_comp_task_lookup.fleet`
- `batch_number` → `lumina.batch_file_header.key`
- `employee_number` → `lumina.defect_stage_employees.defect_id`

### lumina.tool_check_out_in_duplicates

**References (Outgoing):**

- `task_number` → `lumina.amp_datmig_comp_task_lookup.fleet`
- `batch_number` → `lumina.batch_file_header.key`
- `employee_number` → `lumina.defect_stage_employees.defect_id`

### lumina.trades

**References (Outgoing):**

- `trade_code` → `lumina.trades.trade_code`

**Referenced By (Incoming):**

- `lumina.employees.trade_code` → `trade_code`
- `lumina.maint_cost_budget_workcards.trade_code` → `trade_code`
- `lumina.maint_cost_hourly_rates.trade_code` → `trade_code`
- `lumina.oeim_invoice_snap_employees.trade_code` → `trade_code`
- `lumina.rp_block_resource.trade_code` → `trade_code`
- `lumina.rp_wo_base_estimated_defects.trade_code` → `trade_code`
- `lumina.rp_wo_estimated_defects.trade_code` → `trade_code`
- `lumina.trades.trade_code` → `trade_code`
- `lumina.wcr_temp_base1.trade_code` → `trade_code`
- `lumina.work_schedule_trades.trade_code` → `trade_code`
- `lumina.work_schedule_workcards.trade_code` → `trade_code`
- `lumina.work_schedule_zones.trade_code` → `trade_code`
- `lumina.workcard_forms.trade_code` → `trade_code`

### lumina.training_details

**References (Outgoing):**

- `training_id` → `lumina.employee_training_details.employee_number`

### lumina.transaction_header_mavis

**References (Outgoing):**

- `key_id` → `lumina.osys_key_to_reportid.osyskey`

### lumina.transaction_header_trex_lasers

**References (Outgoing):**

- `key_id` → `lumina.osys_key_to_reportid.osyskey`

### lumina.transaction_log_icarus

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `warehouse_code` → `lumina.account_available_warehouses.account_code`
- `vat_code` → `lumina.amp_workcard_activations.workcard_activation_id`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`
- `bin_number` → `lumina.bins.bin_number`
- `company_code` → `lumina.company_codes.company_code`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `movement_code` → `lumina.component_movement_hist_life.part_number`
- `works_order_number` → `lumina.credit_works_order_cards.credit_note_no`
- `currency_code` → `lumina.currency_codes.currency_code`
- `delivery_note_number` → `lumina.delivery_note_extended_remarks.delivery_note_number`

### lumina.transaction_log_icarus_8134

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `warehouse_code` → `lumina.account_available_warehouses.account_code`
- `vat_code` → `lumina.amp_workcard_activations.workcard_activation_id`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`
- `bin_number` → `lumina.bins.bin_number`
- `company_code` → `lumina.company_codes.company_code`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `movement_code` → `lumina.component_movement_hist_life.part_number`
- `works_order_number` → `lumina.credit_works_order_cards.credit_note_no`
- `currency_code` → `lumina.currency_codes.currency_code`
- `delivery_note_number` → `lumina.delivery_note_extended_remarks.delivery_note_number`

### lumina.transaction_log_lasers

**References (Outgoing):**

- `log_number` → `lumina.amp_data_migration_log.log_number`
- `user_id` → `lumina.dataset_locks_by_user.user_id`

### lumina.transaction_log_mavis

**References (Outgoing):**

- `log_number` → `lumina.amp_data_migration_log.log_number`
- `option_number` → `lumina.lmc_base_data_options.opt_id`

### lumina.transaction_log_trecs

**References (Outgoing):**

- `log_number` → `lumina.amp_data_migration_log.log_number`
- `user_id` → `lumina.dataset_locks_by_user.user_id`

### lumina.transaction_types

**References (Outgoing):**

- `transaction_type_code` → `lumina.transaction_types.transaction_type_code`

**Referenced By (Incoming):**

- `lumina.sales_prices.transaction_type_code` → `transaction_type_code`
- `lumina.transaction_types.transaction_type_code` → `transaction_type_code`

### lumina.uf_forecast_cache

**References (Outgoing):**

- `ac_code` → `lumina.access_dim_accounts_info.info_id`
- `alert_number` → `lumina.alert_colors.alert_type_id`
- `na_id` → `lumina.alternate_parts.part_number`
- `workcard_id` → `lumina.amp_access_panels_by_workcard.fleet`
- `interval_id` → `lumina.amp_component_intervals.component_interval_id`
- `fleet_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `visit_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `class_code` → `lumina.document_classes.document_id`
- `rfc_id` → `lumina.fleet_forecast_plans_rfc.plan_id`
- `paragraph_id` → `lumina.paragraph_cancels.rfc_id`

### lumina.unit_owners

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.unknown_part_numbers

**References (Outgoing):**

- `sequence_number` → `lumina.nrc_high_sequence_control.key_id`
- `unknown_part_number` → `lumina.sales_requested_unknown_parts.sales_request_number`

### lumina.unmatched_issues_and_returns

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`

### lumina.unsatified_service_exchanges

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `order_number` → `lumina.batch_orders.batch_number`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.uom_conversion_at_part_level

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

### lumina.user_warehouse_access

**References (Outgoing):**

- `warehouse_code` → `lumina.account_available_warehouses.account_code`
- `user_id` → `lumina.dataset_locks_by_user.user_id`

### lumina.variations

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `variation_id` → `lumina.forecast_variation_details.aircraft_short_reg`
- `planners_notes_cat_id` → `lumina.planners_notes_categories.category_id`

### lumina.variations_xref

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `visit_code` → `lumina.amp_datmig_fleet_visit_pack.fleet`
- `package_code` → `lumina.amp_package_notes.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `workcard_interval_id` → `lumina.amp_workcard_intervals.workcard_interval_id`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `variation_id` → `lumina.forecast_variation_details.aircraft_short_reg`
- `planners_notes_xref_id` → `lumina.planners_notes_xref.category_xref_id`

### lumina.variations_xref_overrides

**References (Outgoing):**

- `variation_number` → `lumina.forecast_variation_details.aircraft_short_reg`
- `life_code_level_id` → `lumina.life_code_levels.life_code_level_id`

### lumina.vat_codes

**References (Outgoing):**

- `vat_code` → `lumina.amp_workcard_activations.workcard_activation_id`
- `export_id` → `lumina.export_codes.export_id`

### lumina.warehouse_distribution

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `warehouse_code` → `lumina.account_available_warehouses.account_code`

### lumina.warehouse_header_1

**References (Outgoing):**

- `warehouse_code` → `lumina.account_available_warehouses.account_code`

### lumina.warehouse_header_2

**References (Outgoing):**

- `warehouse_code` → `lumina.account_available_warehouses.account_code`
- `airport_id` → `lumina.airport_codes.icao_code`

### lumina.warehouse_lmc_email_address

**References (Outgoing):**

- `warehouse_code` → `lumina.account_available_warehouses.account_code`

### lumina.warehouse_replenishment_data

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `warehouse_code` → `lumina.account_available_warehouses.account_code`

### lumina.warranty_claims

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `batch_number` → `lumina.batch_file_header.key`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `user_id` → `lumina.dataset_locks_by_user.user_id`
- `warranty_claim_id` → `lumina.warranty_claims.warranty_claim_id`
- `warranty_terms_id` → `lumina.warranty_terms.warranty_terms_id`

**Referenced By (Incoming):**

- `lumina.warranty_claims.warranty_claim_id` → `warranty_claim_id`

### lumina.warranty_exclusions

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `exclusion_id` → `lumina.aircraft_exclusions.aircraft_exclusion_id`
- `serial_number` → `lumina.completion_part_serial.part_number`

### lumina.warranty_terms

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `condition_code` → `lumina.condition_codes.condition_code`
- `warranty_terms_id` → `lumina.warranty_terms.warranty_terms_id`

**Referenced By (Incoming):**

- `lumina.warranty_claims.warranty_terms_id` → `warranty_terms_id`
- `lumina.warranty_terms.warranty_terms_id` → `warranty_terms_id`
- `lumina.warranty_terms_documents.warranty_terms_id` → `warranty_terms_id`

### lumina.warranty_terms_documents

**References (Outgoing):**

- `document_image_id` → `lumina.document_image_source.document_image_source_id`
- `warranty_terms_id` → `lumina.warranty_terms.warranty_terms_id`

### lumina.wcr_boeing_tb_revision

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `save_id` → `lumina.amp_workcard_saved_reports.saved_report_id`
- `user_id` → `lumina.dataset_locks_by_user.user_id`

### lumina.wcr_msg_log

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.wcr_temp_access_panels

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `task_number` → `lumina.amp_datmig_comp_task_lookup.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.wcr_temp_base1

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `document_id` → `lumina.aircraft_documents.aircraft_document_id`
- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `workcard_id` → `lumina.amp_access_panels_by_workcard.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`
- `zone_code` → `lumina.dmg_rpr_measurement_zones.measurement_zone_id`
- `phase_code` → `lumina.rfc_frequency_phase_header.rfc_id`
- `trade_code` → `lumina.trades.trade_code`

### lumina.wcr_temp_narratives

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `task_number` → `lumina.amp_datmig_comp_task_lookup.fleet`
- `revision_id` → `lumina.amp_revision_history.history_id`

### lumina.weight_and_balance_documents

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `document_id` → `lumina.aircraft_documents.aircraft_document_id`
- `document_image_id` → `lumina.document_image_source.document_image_source_id`

### lumina.wo_auto_amended_contacts

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`

### lumina.wo_releases

**References (Outgoing):**

- `employee_number` → `lumina.defect_stage_employees.defect_id`

### lumina.work_sch_def_2_lg318

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `defect_number` → `lumina.defect_extensions.defect_id`

### lumina.work_schedule_defect_1

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `nrc_number` → `lumina.cq_quote_nrc_access_panels.quote_id`
- `defect_number` → `lumina.defect_extensions.defect_id`

### lumina.work_schedule_defect_2

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `defect_number` → `lumina.defect_extensions.defect_id`

### lumina.work_schedule_defect_3

**References (Outgoing):**

- `approval_number` → `lumina.account_supplier_approvals.account_code`
- `flight_number` → `lumina.aircraft_flight_hours_1.aircraft_code`
- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `defect_number` → `lumina.defect_extensions.defect_id`
- `employee_number` → `lumina.defect_stage_employees.defect_id`

### lumina.work_schedule_defect_4

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `currency_code` → `lumina.currency_codes.currency_code`
- `defect_number` → `lumina.defect_extensions.defect_id`
- `engineering_support_status_id` → `lumina.engineering_support_status.engineering_status_id`

### lumina.work_schedule_header_2

**References (Outgoing):**

- `works_order_number` → `lumina.credit_works_order_cards.credit_note_no`
- `job_number` → `lumina.job_references.job_reference`

### lumina.work_schedule_header_3

**References (Outgoing):**

- `works_order_sub_status_id` → `lumina.works_order_sub_status.works_order_sub_status_id`

### lumina.work_schedule_ms_codes

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`

### lumina.work_schedule_trades

**References (Outgoing):**

- `trade_code` → `lumina.trades.trade_code`

### lumina.work_schedule_workcards

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `trade_code` → `lumina.trades.trade_code`

### lumina.work_schedule_zones

**References (Outgoing):**

- `trade_code` → `lumina.trades.trade_code`

### lumina.workcard_accomplishments

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`

### lumina.workcard_activations

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `workcard_activation_id` → `lumina.amp_workcard_activations.workcard_activation_id`

### lumina.workcard_cancellations

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `workcard_cancellation_id` → `lumina.amp_workcard_cancellations.workcard_cancellation_id`

### lumina.workcard_default_status

**References (Outgoing):**

- `key_id` → `lumina.osys_key_to_reportid.osyskey`

### lumina.workcard_documents_filter

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `filter_id` → `lumina.forecast_filter_groups.group_id`

### lumina.workcard_form_number

**References (Outgoing):**

- `aircraft_code` → `lumina.aircraft_assembles.aircraft_code`
- `form_number_id` → `lumina.form_number.form_number_id`

### lumina.workcard_forms

**References (Outgoing):**

- `workcard_number` → `lumina.amp_access_panels_by_workcard.fleet`
- `trade_code` → `lumina.trades.trade_code`

### lumina.workcard_properties

**References (Outgoing):**

- `document_image_id` → `lumina.document_image_source.document_image_source_id`

### lumina.workcard_status_codes

**References (Outgoing):**

- `status_code` → `lumina.amp_revision_status.revision_status_id`

### lumina.workpack_printing_control

**References (Outgoing):**

- `oases_report_id` → `lumina.oases_reports.report_id`

### lumina.works_order_contracts

**References (Outgoing):**

- `contract_id` → `lumina.customer_contract_rates.contract_id`
- `markup_code` → `lumina.freight_cost_markups.freight_cost_markup_id`

### lumina.works_order_documents

**References (Outgoing):**

- `document_image_id` → `lumina.document_image_source.document_image_source_id`

### lumina.works_order_issues_and_returns

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `bin_number` → `lumina.bins.bin_number`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`
- `rotable_batch_number` → `lumina.rotable_batch_locations.id`

### lumina.works_order_issues_and_rtn_bac

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `bin_number` → `lumina.bins.bin_number`
- `requirement_number` → `lumina.nrc_requirements_actions.aircraft_short_reg`
- `rotable_batch_number` → `lumina.rotable_batch_locations.id`

### lumina.works_order_markup_header

**References (Outgoing):**

- `markup_code` → `lumina.freight_cost_markups.freight_cost_markup_id`

### lumina.works_order_markup_table

**References (Outgoing):**

- `markup_code` → `lumina.freight_cost_markups.freight_cost_markup_id`

### lumina.works_order_sub_status

**References (Outgoing):**

- `status_code` → `lumina.amp_revision_status.revision_status_id`
- `works_order_sub_status_id` → `lumina.works_order_sub_status.works_order_sub_status_id`

**Referenced By (Incoming):**

- `lumina.work_schedule_header_3.works_order_sub_status_id` → `works_order_sub_status_id`
- `lumina.works_order_sub_status.works_order_sub_status_id` → `works_order_sub_status_id`

### lumina.works_orders

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`
- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `order_number` → `lumina.batch_orders.batch_number`
- `company_code` → `lumina.company_codes.company_code`
- `serial_number` → `lumina.completion_part_serial.part_number`
- `movement_code` → `lumina.component_movement_hist_life.part_number`
- `licence_id` → `lumina.email_licence.license_id`

### lumina.works_orders_by_account

**References (Outgoing):**

- `account_code` → `lumina.access_dim_accounts_info.info_id`
- `company_code` → `lumina.company_codes.company_code`

### lumina.works_orders_by_part_number

**References (Outgoing):**

- `part_number` → `lumina.PART_NUMBER_CHAPTERS_DJ-82.part_number`

---

## Relationship Matrix

Visual representation of table relationships:

```
                                 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29

 0: PART_NUMBER_CHAPTERS_DJ-82
 1: aircraft_assembles
 2: amp_access_panels_by_workcard
 3: completion_part_serial
 4: amp_revision_history
 5: access_dim_accounts_info
 6: batch_orders
 7: batch_file_header
 8: invoice_categories
 9: currency_codes
10: fleet_forecast_plans_rfc
11: amp_datmig_fleet_visit_pack
12: amp_package_notes
13: accomplishment_history
14: defect_extensions
15: nrc_requirements_actions
16: defect_stage_employees
17: amp_report_documents
18: document_image_source
19: life_code_levels
20: maint_cost_budget_adsb
21: maint_cost_time_category_set
22: dataset_locks_by_user
23: dmg_rpr_damage
24: account_available_warehouses
25: cost_codes
26: amp_workcard_activations
27: cq_quote_nrc_access_panels
28: paragraph_cancels
29: rfc_frequency_phase_header

Matrix Legend: → = references, ← = referenced by, ↔ = bidirectional

 0 PART_NUMBER_CHAPTERS_DJ-82    ●  ·  · ←  ·  ·  ·  ·  ·  ·  ·  ·  · ←  ·  ·  ·  ·  ·  ·  ·  ·  · ←  ·  ·  ·  ·  ·  ·
 1 aircraft_assembles             · ●  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ←  ·  ·  ·  ·  ·  · ←  ·  ·  ·  ·  ·  ·  ·  ·  ·
 2 amp_access_panels_by_workcard  ·  · ●  · →  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ←  ·  ·  ·  · ←  ·  ·  ·  ·  · ←  ·  ·  ·
 3 completion_part_serial        →  ·  · ●  ·  ·  ·  ·  ·  ·  ·  ·  · ←  ·  ·  ·  ·  ·  ·  ·  ·  · ←  ·  ·  ·  ·  ·  ·
 4 amp_revision_history           ·  · ←  · ●  ·  ·  ·  ·  ·  ·  · ← ↔  ·  ·  · ←  ·  · ←  · →  ·  ·  · ←  ·  ·  ·
 5 access_dim_accounts_info       ·  ·  ·  ·  · ●  ·  · →  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ←  · →  ·  ·  ·
 6 batch_orders                   ·  ·  ·  ·  ·  · ● →  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
 7 batch_file_header              ·  ·  ·  ·  ·  · ← ●  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
 8 invoice_categories             ·  ·  ·  ·  · ←  ·  · ●  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
 9 currency_codes                 ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
10 fleet_forecast_plans_rfc       ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·  · ←  ·  ·  ·  ·  ·  · ←  ·  ·  ·  ·  ·  ·  · ← ←
11 amp_datmig_fleet_visit_pack    ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●  · ←  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
12 amp_package_notes              ·  ·  ·  · →  ·  ·  ·  ·  ·  ·  · ● ←  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
13 accomplishment_history        → →  · → ↔  ·  ·  ·  ·  · → → → ●  ·  ·  · → →  ·  ·  ·  · →  ·  ·  ·  · →  ·
14 defect_extensions              ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ● ← ←  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
15 nrc_requirements_actions       ·  · →  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · → ●  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
16 defect_stage_employees         ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · →  · ●  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
17 amp_report_documents           ·  ·  ·  · →  ·  ·  ·  ·  ·  ·  ·  · ←  ·  ·  · ● →  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
18 document_image_source          ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ←  ·  ·  · ← ●  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
19 life_code_levels               ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
20 maint_cost_budget_adsb         · → →  · →  ·  ·  ·  ·  · →  ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·  ·  ·  ·  ·  ·  ·  · →
21 maint_cost_time_category_set   ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·  ·  ·  ·  ·  ·  ·  ·
22 dataset_locks_by_user          ·  ·  ·  · ←  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·  ·  ·  ·  ·  ·  ·
23 dmg_rpr_damage                →  ·  · →  ·  ·  ·  ·  ·  ·  ·  ·  · ←  ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·  ·  ·  ·  ·  ·
24 account_available_warehouses   ·  ·  ·  ·  · →  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·  ·  ·  ·  ·
25 cost_codes                     ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·  ·  ·  ·
26 amp_workcard_activations       ·  · →  · → ←  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·  ·  ·
27 cq_quote_nrc_access_panels     ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ●  ·  ·
28 paragraph_cancels              ·  ·  ·  ·  ·  ·  ·  ·  ·  · →  ·  · ←  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · ● ←
29 rfc_frequency_phase_header     ·  ·  ·  ·  ·  ·  ·  ·  ·  · →  ·  ·  ·  ·  ·  ·  ·  ·  · ←  ·  ·  ·  ·  ·  ·  · → ●
```

---


---

## Relationship Changes

### Relationships Added in Target Schema

- `access_dim_accounts_info.account_id` → `access_dim_accounts_info`
- `access_dim_accounts_info.info_id` → `access_dim_accounts_info`
- `access_dim_accounts_info.invoice_number` → `invoice_categories`
- `access_dim_accounts_info.vat_code` → `amp_workcard_activations`
- `access_dim_sales_info.audit_number` → `amp_audit_notes`
- `access_dim_sales_info.customer_code` → `customer_contract_rates`
- `access_dim_sales_info.info_id` → `access_dim_accounts_info`
- `access_dim_sales_info.sales_order_number` → `customer_sales_order_xref`
- `access_dim_sales_info.vat_code` → `amp_workcard_activations`
- `accomp_bkup.accomplishment_id` → `accomplishment_history`
- `accomp_bkup.aircraft_code` → `aircraft_assembles`
- `accomp_bkup.package_code` → `amp_package_notes`
- `accomp_bkup.paragraph_id` → `paragraph_cancels`
- `accomp_bkup.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `accomp_bkup.report_id` → `amp_report_documents`
- `accomp_bkup.revision_id` → `amp_revision_history`
- `accomp_bkup.rfc_id` → `fleet_forecast_plans_rfc`
- `accomp_bkup.serial_number` → `completion_part_serial`
- `accomp_bkup.visit_code` → `amp_datmig_fleet_visit_pack`
- `accomp_hist_delta_1763.accomplishment_id` → `accomplishment_history`
- `accomp_hist_delta_1763.aircraft_code` → `aircraft_assembles`
- `accomp_hist_delta_1763.damage_id` → `dmg_rpr_damage`
- `accomp_hist_delta_1763.document_image_id` → `document_image_source`
- `accomp_hist_delta_1763.package_code` → `amp_package_notes`
- `accomp_hist_delta_1763.paragraph_id` → `paragraph_cancels`
- `accomp_hist_delta_1763.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `accomp_hist_delta_1763.report_id` → `amp_report_documents`
- `accomp_hist_delta_1763.revision_id` → `amp_revision_history`
- `accomp_hist_delta_1763.rfc_id` → `fleet_forecast_plans_rfc`
- `accomp_hist_delta_1763.serial_number` → `completion_part_serial`
- `accomp_hist_delta_1763.visit_code` → `amp_datmig_fleet_visit_pack`
- `accomp_hist_lost_sched.accomplishment_id` → `accomplishment_history`
- `accomp_hist_lost_sched.aircraft_code` → `aircraft_assembles`
- `accomp_hist_lost_sched.package_code` → `amp_package_notes`
- `accomp_hist_lost_sched.paragraph_id` → `paragraph_cancels`
- `accomp_hist_lost_sched.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `accomp_hist_lost_sched.report_id` → `amp_report_documents`
- `accomp_hist_lost_sched.revision_id` → `amp_revision_history`
- `accomp_hist_lost_sched.rfc_id` → `fleet_forecast_plans_rfc`
- `accomp_hist_lost_sched.serial_number` → `completion_part_serial`
- `accomp_hist_lost_sched.visit_code` → `amp_datmig_fleet_visit_pack`
- `accomp_hist_lost_sched_val.accomplishment_id` → `accomplishment_history`
- `accomp_hist_lost_sched_val.life_code_level_id` → `life_code_levels`
- `accomp_values_bkup.accomplishment_id` → `accomplishment_history`
- `accomp_values_bkup.life_code_level_id` → `life_code_levels`
- `accomplishment_history.accomplishment_id` → `accomplishment_history`
- `accomplishment_history.aircraft_code` → `aircraft_assembles`
- `accomplishment_history.damage_id` → `dmg_rpr_damage`
- `accomplishment_history.document_image_id` → `document_image_source`
- `accomplishment_history.package_code` → `amp_package_notes`
- `accomplishment_history.paragraph_id` → `paragraph_cancels`
- `accomplishment_history.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `accomplishment_history.report_id` → `amp_report_documents`
- `accomplishment_history.revision_id` → `amp_revision_history`
- `accomplishment_history.rfc_id` → `fleet_forecast_plans_rfc`
- `accomplishment_history.serial_number` → `completion_part_serial`
- `accomplishment_history.visit_code` → `amp_datmig_fleet_visit_pack`
- `accomplishment_history_values.accomplishment_id` → `accomplishment_history`
- `accomplishment_history_values.life_code_level_id` → `life_code_levels`
- `account_ata_spec_2000_xref.account_code` → `access_dim_accounts_info`
- `account_available_warehouses.account_code` → `access_dim_accounts_info`
- `account_available_warehouses.warehouse_code` → `account_available_warehouses`
- `account_location_notes.account_code` → `access_dim_accounts_info`
- `account_system_header.key_id` → `osys_key_to_reportid`
- `accs_var_corrections_bkp.accomplishment_id` → `accomplishment_history`
- `accum_cycles_static_data.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `add_extension_permissions.user_id` → `dataset_locks_by_user`
- `aircraft_build_chapters.aircraft_code` → `aircraft_assembles`
- `aircraft_documents.aircraft_code` → `aircraft_assembles`
- `aircraft_documents.aircraft_document_id` → `aircraft_documents`
- `aircraft_documents.document_image_id` → `document_image_source`
- `aircraft_flight_hours_1.aircraft_code` → `aircraft_assembles`
- `aircraft_flight_hours_2.aircraft_code` → `aircraft_assembles`
- `aircraft_life.aircraft_code` → `aircraft_assembles`
- `aircraft_life.life_code_level_id` → `life_code_levels`
- `aircraft_life_dbf1065.aircraft_code` → `aircraft_assembles`
- `aircraft_life_dbf1065.life_code_level_id` → `life_code_levels`
- `aircraft_major_checks.aircraft_code` → `aircraft_assembles`
- `aircraft_major_checks.package_code` → `amp_package_notes`
- `aircraft_major_checks.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `aircraft_major_checks.serial_number` → `completion_part_serial`
- `aircraft_major_checks.visit_code` → `amp_datmig_fleet_visit_pack`
- `aircraft_statistics.workcard_number` → `amp_access_panels_by_workcard`
- `aircraft_subchapter_statistics.aircraft_code` → `aircraft_assembles`
- `aircraft_weight_7487bkp.aircraft_code` → `aircraft_assembles`
- `aircraft_weight_conf.conf_id` → `aircraft_weight_conf`
- `aircraft_weight_conf_entries.conf_id` → `aircraft_weight_conf`
- `aircraft_weight_conf_xref.aircraft_code` → `aircraft_assembles`
- `aircraft_weight_conf_xref.conf_id` → `aircraft_weight_conf`
- `airway_bill_references.account_code` → `access_dim_accounts_info`
- `airway_bill_references.delivery_note_number` → `delivery_note_extended_remarks`
- `airway_bill_references.order_number` → `batch_orders`
- `airway_bill_references.shipment_id` → `shipment`
- `alternate_parts.alternate_part_number` → `alternate_parts`
- `alternate_parts.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `amp_acc_panel_desc_osd_33348.access_panel_code` → `amp_access_panel_desc_hdr`
- `amp_acc_panel_desc_osd_33348.revision_id` → `amp_revision_history`
- `amp_access_panel_desc_hdr.revision_id` → `amp_revision_history`
- `amp_access_panel_descriptions.revision_id` → `amp_revision_history`
- `amp_access_panel_effectivity.access_panel_code` → `amp_access_panel_desc_hdr`
- `amp_access_panel_effectivity.aircraft_code` → `aircraft_assembles`
- `amp_access_panel_effectivity.fleet_code` → `amp_datmig_fleet_visit_pack`
- `amp_access_panel_effectivity.revision_id` → `amp_revision_history`
- `amp_access_panel_effectivity.sub_fleet_id` → `sub_fleet_header`
- `amp_access_panel_notes.revision_id` → `amp_revision_history`
- `amp_access_panels_by_workcard.revision_id` → `amp_revision_history`
- `amp_accesspanel_effectivity_jn.access_panel_code` → `amp_access_panel_desc_hdr`
- `amp_accesspanel_effectivity_jn.aircraft_code` → `aircraft_assembles`
- `amp_accesspanel_effectivity_jn.fleet_code` → `amp_datmig_fleet_visit_pack`
- `amp_accesspanel_effectivity_jn.revision_id` → `amp_revision_history`
- `amp_accesspanel_effectivity_jn.sub_fleet_id` → `sub_fleet_header`
- `amp_audit_notes.fleet_code` → `amp_datmig_fleet_visit_pack`
- `amp_audit_notes.package_code` → `amp_package_notes`
- `amp_audit_notes.revision_id` → `amp_revision_history`
- `amp_audit_notes.visit_code` → `amp_datmig_fleet_visit_pack`
- `amp_audit_notes.workcard_number` → `amp_access_panels_by_workcard`
- `amp_comments.revision_id` → `amp_revision_history`
- `amp_component_intervals.revision_id` → `amp_revision_history`
- `amp_component_reset_on_compl.component_interval_id` → `amp_component_intervals`
- `amp_component_reset_on_compl.component_life_limit_id` → `component_life_limits`
- `amp_data_migration_log.log_number` → `amp_data_migration_log`
- `amp_datmig_accomplishments.aircraft_code` → `aircraft_assembles`
- `amp_datmig_accomplishments.package_code` → `amp_package_notes`
- `amp_datmig_accomplishments.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `amp_datmig_accomplishments.serial_number` → `completion_part_serial`
- `amp_datmig_accomplishments.visit_code` → `amp_datmig_fleet_visit_pack`
- `amp_datmig_comp_task_lookup.package_code` → `amp_package_notes`
- `amp_datmig_llp.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `amp_datmig_llp.serial_number` → `completion_part_serial`
- `amp_document_effectivity_bk.aircraft_code` → `aircraft_assembles`
- `amp_document_effectivity_bk.document_id` → `aircraft_documents`
- `amp_document_effectivity_bk.workcard_id` → `amp_access_panels_by_workcard`
- `amp_documents_by_workcard.revision_id` → `amp_revision_history`
- `amp_documents_by_workcard_bk.document_id` → `aircraft_documents`
- `amp_documents_by_workcard_bk.revision_id` → `amp_revision_history`
- `amp_documents_by_workcard_bk.sequence_number` → `nrc_high_sequence_control`
- `amp_documents_by_workcard_bk.workcard_id` → `amp_access_panels_by_workcard`
- `amp_documents_by_workcard_bk.workcard_number` → `amp_access_panels_by_workcard`
- `amp_manufacturers_documents.document_id` → `aircraft_documents`
- `amp_manufacturers_documents.revision_id` → `amp_revision_history`
- `amp_material_effectivity.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `amp_material_effectivity.sub_fleet_id` → `sub_fleet_header`
- `amp_material_effectivity.workcard_id` → `amp_access_panels_by_workcard`
- `amp_material_effectivity_jn.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `amp_material_effectivity_jn.sub_fleet_id` → `sub_fleet_header`
- `amp_material_effectivity_jn.workcard_id` → `amp_access_panels_by_workcard`
- `amp_materials_required_by_wc.revision_id` → `amp_revision_history`
- `amp_package_notes.revision_id` → `amp_revision_history`
- `amp_packages.revision_id` → `amp_revision_history`
- `amp_packages_by_visit.package_code` → `amp_package_notes`
- `amp_packages_by_visit.revision_id` → `amp_revision_history`
- `amp_packages_by_visit.visit_code` → `amp_datmig_fleet_visit_pack`
- `amp_packages_by_workcard.revision_id` → `amp_revision_history`
- `amp_planning_notes.fleet_code` → `amp_datmig_fleet_visit_pack`
- `amp_planning_notes.package_code` → `amp_package_notes`
- `amp_planning_notes.revision_id` → `amp_revision_history`
- `amp_planning_notes.visit_code` → `amp_datmig_fleet_visit_pack`
- `amp_planning_notes.workcard_number` → `amp_access_panels_by_workcard`
- `amp_report_documents.document_image_id` → `document_image_source`
- `amp_report_documents.revision_id` → `amp_revision_history`
- `amp_revision_history.history_id` → `accomplishment_history`
- `amp_revision_history.revision_id` → `amp_revision_history`
- `amp_revision_history.user_id` → `dataset_locks_by_user`
- `amp_revision_status.revision_status_id` → `amp_revision_status`
- `amp_revisions.revision_id` → `amp_revision_history`
- `amp_visit_notes.revision_id` → `amp_revision_history`
- `amp_visits.revision_id` → `amp_revision_history`
- `amp_wc_aircraft_exclusions.revision_id` → `amp_revision_history`
- `amp_wc_in_limits_bak.life_code_level_id` → `life_code_levels`
- `amp_wc_in_limits_bak.workcard_interval_id` → `amp_workcard_intervals`
- `amp_wc_in_stages_bak.workcard_interval_id` → `amp_workcard_intervals`
- `amp_wcard_extended_desc_41.revision_id` → `amp_revision_history`
- `amp_wcard_extended_desc_41.workcard_number` → `amp_access_panels_by_workcard`
- `amp_workcard_ac_effectivity.aircraft_code` → `aircraft_assembles`
- `amp_workcard_ac_effectivity.sub_fleet_id` → `sub_fleet_header`
- `amp_workcard_ac_effectivity.workcard_id` → `amp_access_panels_by_workcard`
- `amp_workcard_ac_effectivity_jn.aircraft_code` → `aircraft_assembles`
- `amp_workcard_ac_effectivity_jn.sub_fleet_id` → `sub_fleet_header`
- `amp_workcard_ac_effectivity_jn.workcard_id` → `amp_access_panels_by_workcard`
- `amp_workcard_accomplishments.revision_id` → `amp_revision_history`
- `amp_workcard_accomplishments.workcard_number` → `amp_access_panels_by_workcard`
- `amp_workcard_activations.revision_id` → `amp_revision_history`
- `amp_workcard_call_workcard.revision_id` → `amp_revision_history`
- `amp_workcard_cancellations.revision_id` → `amp_revision_history`
- `amp_workcard_cancellations.workcard_cancellation_id` → `amp_workcard_cancellations`
- `amp_workcard_cancellations.workcard_number` → `amp_access_panels_by_workcard`
- `amp_workcard_extended_desc.revision_id` → `amp_revision_history`
- `amp_workcard_h3_7487bkp.phase_code` → `rfc_frequency_phase_header`
- `amp_workcard_h3_7487bkp.revision_id` → `amp_revision_history`
- `amp_workcard_header_1.revision_id` → `amp_revision_history`
- `amp_workcard_header_1_43216.revision_id` → `amp_revision_history`
- `amp_workcard_header_1_43216.workcard_id` → `amp_access_panels_by_workcard`
- `amp_workcard_header_1_43216.workcard_number` → `amp_access_panels_by_workcard`
- `amp_workcard_header_2.revision_id` → `amp_revision_history`
- `amp_workcard_header_3.revision_id` → `amp_revision_history`
- `amp_workcard_header_4.revision_id` → `amp_revision_history`
- `amp_workcard_header_5.revision_id` → `amp_revision_history`
- `amp_workcard_header_5.revision_number` → `amp_revision_history`
- `amp_workcard_header_properties.revision_id` → `amp_revision_history`
- `amp_workcard_intervals.aircraft_code` → `aircraft_assembles`
- `amp_workcard_intervals.component_life_limit_id` → `component_life_limits`
- `amp_workcard_intervals.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `amp_workcard_intervals.serial_number` → `completion_part_serial`
- `amp_workcard_intervals.sub_fleet_id` → `sub_fleet_header`
- `amp_workcard_intervals.workcard_id` → `amp_access_panels_by_workcard`
- `amp_workcard_intervals.workcard_interval_id` → `amp_workcard_intervals`
- `amp_workcard_intervals_limits.workcard_interval_id` → `amp_workcard_intervals`
- `amp_workcard_intervals_stages.workcard_interval_id` → `amp_workcard_intervals`
- `amp_workcard_lcl_applicability.life_code_level_id` → `life_code_levels`
- `amp_workcard_lcl_applicability.revision_id` → `amp_revision_history`
- `amp_workcard_lcl_applicability.workcard_number` → `amp_access_panels_by_workcard`
- `amp_workcard_narrative.revision_id` → `amp_revision_history`
- `amp_workcard_not_with_workcard.revision_id` → `amp_revision_history`
- `amp_workcard_previously_acc_by.revision_id` → `amp_revision_history`
- `amp_workcard_publications.publication_code` → `amp_workcard_publications`
- `amp_workcard_publications.publication_id` → `amp_workcard_publications`
- `amp_workcard_publications.workcard_id` → `amp_access_panels_by_workcard`
- `amp_workcard_saved_reports.saved_report_id` → `amp_workcard_saved_reports`
- `amp_workcard_saved_reports_hdr.saved_report_id` → `amp_workcard_saved_reports`
- `amp_workcards_by_package.revision_id` → `amp_revision_history`
- `amp_workcards_by_section.revision_id` → `amp_revision_history`
- `assemble_thrust_life_code.aircraft_code` → `aircraft_assembles`
- `assemble_thrust_life_code.fleet_code` → `amp_datmig_fleet_visit_pack`
- `assemble_thrust_life_code.life_code` → `aircraft_life`
- `assemble_thrust_life_code.life_code_id` → `assemble_thrust_life_code`
- `assembly_model_header.model_id` → `assembly_model_header`
- `assembly_model_nodes.model_id` → `assembly_model_header`
- `assembly_model_nodes.node_id` → `assembly_model_nodes`
- `audit_trail.audit_id` → `amp_audit_notes`
- `audit_trail.user_id` → `dataset_locks_by_user`
- `audit_trail_ids.audit_id` → `amp_audit_notes`
- `audit_trail_meta_data.audit_id` → `amp_audit_notes`
- `audit_trail_meta_data.meta_id` → `audit_trail_meta_data`
- `bar_codes.bar_code` → `bar_codes`
- `bar_codes.workcard_number` → `amp_access_panels_by_workcard`
- `bar_codes.works_order_number` → `credit_works_order_cards`
- `batch_history.batch_number` → `batch_file_header`
- `batch_history.user_id` → `dataset_locks_by_user`
- `batch_notes.batch_number` → `batch_file_header`
- `batch_notes.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `batch_notes.serial_number` → `completion_part_serial`
- `batch_notes_gu4240.batch_number` → `batch_file_header`
- `batch_notes_gu4240.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `batch_notes_gu4240.serial_number` → `completion_part_serial`
- `batch_orders.batch_number` → `batch_file_header`
- `batch_orders.order_number` → `batch_orders`
- `batch_record_1_gu4240.batch_number` → `batch_file_header`
- `batch_record_1_gu4240.currency_code` → `currency_codes`
- `batch_record_1_gu4240.goods_received_number` → `goods_received_sheet_document`
- `batch_record_1_gu4240.order_number` → `batch_orders`
- `batch_record_1_gu4240.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `batch_record_1_gu4240.serial_number` → `completion_part_serial`
- `batch_record_2.batch_number` → `batch_file_header`
- `batch_record_2.currency_code` → `currency_codes`
- `batch_record_2.customs_entry_number` → `batches_by_customs_entry`
- `batch_record_camo.batch_number` → `batch_file_header`
- `batches_by_airway_bill.airway_bill_number` → `airway_bill_references`
- `batches_by_airway_bill.batch_number` → `batch_file_header`
- `batches_by_customs_entry.batch_number` → `batch_file_header`
- `batches_by_customs_entry.customs_entry_number` → `batches_by_customs_entry`
- `bkp_mobile_permissions.permission_id` → `add_extension_permissions`
- `bulk_batch_header.bulk_batch_number` → `bulk_batch_header`
- `cfd_xref_to_tech_log.aircraft_code` → `aircraft_assembles`
- `company_codes.company_code` → `company_codes`
- `company_form_attachments.attachment_id` → `company_form_attachments`
- `company_form_attachments.company_form_id` → `company_form_attachments`
- `company_form_details.company_code` → `company_codes`
- `company_form_details.company_form_id` → `company_form_attachments`
- `company_form_details.form_number` → `company_form_attachments`
- `completion_fleet_ata_pos.aircraft_code` → `aircraft_assembles`
- `completion_life_values.aircraft_code` → `aircraft_assembles`
- `completion_life_values.life_code_level_id` → `life_code_levels`
- `completion_life_values.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `completion_life_values.serial_number` → `completion_part_serial`
- `completion_maint_mod.aircraft_code` → `aircraft_assembles`
- `completion_maint_mod.report_id` → `amp_report_documents`
- `completion_part_serial.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `completion_part_serial.serial_number` → `completion_part_serial`
- `component_mods_history_by_part.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `component_movement_history.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `component_movement_history.serial_number` → `completion_part_serial`
- `component_movt_hist_ext_8661.aircraft_code` → `aircraft_assembles`
- `component_movt_hist_ext_8661.batch_number` → `batch_file_header`
- `component_movt_hist_ext_8661.component_life_limit_id` → `component_life_limits`
- `component_movt_hist_ext_8661.history_id` → `accomplishment_history`
- `component_movt_hist_ext_8661.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `component_movt_hist_ext_8661.report_id` → `amp_report_documents`
- `component_movt_hist_ext_8661.serial_number` → `completion_part_serial`
- `components_bkp_dj95.aircraft_code` → `aircraft_assembles`
- `components_bkp_dj95.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `components_bkp_dj95.serial_number` → `completion_part_serial`
- `components_bkp_dj97.aircraft_code` → `aircraft_assembles`
- `components_bkp_dj97.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `components_bkp_dj97.serial_number` → `completion_part_serial`
- `components_oases971.aircraft_code` → `aircraft_assembles`
- `components_oases971.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `components_oases971.serial_number` → `completion_part_serial`
- `condition_pick_table.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `condition_pick_table.pick_number` → `condition_pick_table`
- `condition_pick_table.requirement_number` → `nrc_requirements_actions`
- `condition_pick_table.warehouse_code` → `account_available_warehouses`
- `consumable_repair_xref_to_part.batch_number` → `batch_file_header`
- `consumable_repair_xref_to_part.order_number` → `batch_orders`
- `consumable_repair_xref_to_part.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `contacts_xref.account_code` → `access_dim_accounts_info`
- `cq_documents.document_image_id` → `document_image_source`
- `cq_documents.quote_id` → `cq_quote_cards`
- `cq_quote_nrc_access_panels.access_panel_code` → `amp_access_panel_desc_hdr`
- `cq_quote_nrc_access_panels.quote_id` → `cq_quote_cards`
- `cq_quote_nrc_access_panels.quote_nrc_id` → `cq_quote_nrc_access_panels`
- `cq_quote_status_contacts.status_id` → `amp_revision_status`
- `crs_signature_text.aircraft_code` → `aircraft_assembles`
- `crs_signature_text.crs_text_id` → `crs_text`
- `crs_text.crs_text_id` → `crs_text`
- `customer_sales_order_xref.customer_sales_order_number` → `customer_sales_order_xref`
- `customer_sales_order_xref.sales_order_number` → `customer_sales_order_xref`
- `customs_tariff_codes_territory.customs_tariff_code` → `customs_tariff_codes`
- `daily_loans_out.account_code` → `access_dim_accounts_info`
- `daily_loans_out.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `daily_loans_out.serial_number` → `completion_part_serial`
- `dataset_locks_by_lock_type.user_id` → `dataset_locks_by_user`
- `dataset_locks_by_user.user_id` → `dataset_locks_by_user`
- `defect_extensions.defect_id` → `defect_extensions`
- `defect_extensions.extension_id` → `add_extension_permissions`
- `deferred_defect_xref_to_cfd_no.aircraft_code` → `aircraft_assembles`
- `delivery_note_extended_remarks.delivery_note_number` → `delivery_note_extended_remarks`
- `delivery_note_header_1.account_code` → `access_dim_accounts_info`
- `delivery_note_header_1.company_code` → `company_codes`
- `delivery_note_header_1.delivery_note_number` → `delivery_note_extended_remarks`
- `delivery_note_header_1.order_number` → `batch_orders`
- `delivery_note_header_2.delivery_note_number` → `delivery_note_extended_remarks`
- `delivery_note_header_3.delivery_note_number` → `delivery_note_extended_remarks`
- `delivery_note_header_4.account_code` → `access_dim_accounts_info`
- `delivery_note_header_4.delivery_note_number` → `delivery_note_extended_remarks`
- `delivery_note_master_list.delivery_note_number` → `delivery_note_extended_remarks`
- `demand_reason_to_movement_code.movement_code` → `component_movement_hist_life`
- `demand_reason_to_movement_code.reason_id` → `demand_reason_to_movement_code`
- `departments.department_id` → `departments`
- `departments.export_code` → `export_codes`
- `dmg_rpr_action_taken_details.action_taken_id` → `dmg_rpr_action_taken_details`
- `dmg_rpr_attachments.damage_id` → `dmg_rpr_damage`
- `dmg_rpr_attachments.document_image_id` → `document_image_source`
- `dmg_rpr_ca_approval_details.ca_approval_id` → `dmg_rpr_ca_approval_details`
- `dmg_rpr_corrosion_levels.corrosion_level_id` → `dmg_rpr_corrosion_levels`
- `dmg_rpr_damage.damage_id` → `dmg_rpr_damage`
- `dmg_rpr_damage.damage_type_id` → `dmg_rpr_damage_types`
- `dmg_rpr_damage.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `dmg_rpr_damage.section_id` → `amp_workcard_sections`
- `dmg_rpr_damage.serial_number` → `completion_part_serial`
- `dmg_rpr_damage.zone_code` → `dmg_rpr_measurement_zones`
- `dmg_rpr_damage_numbering.aircraft_code` → `aircraft_assembles`
- `dmg_rpr_damage_numbering.damage_id` → `dmg_rpr_damage`
- `dmg_rpr_damage_numbering.damage_number` → `dmg_rpr_damage`
- `dmg_rpr_damage_types.damage_type_id` → `dmg_rpr_damage_types`
- `dmg_rpr_dmg_2d_position_labels.damage_id` → `dmg_rpr_damage`
- `dmg_rpr_dmg_2d_position_labels.label_id` → `dmg_rpr_dmg_2d_position_labels`
- `dmg_rpr_dmg_2d_positions.damage_id` → `dmg_rpr_damage`
- `dmg_rpr_dmg_2d_positions.position_id` → `dmg_rpr_dmg_2d_position_labels`
- `dmg_rpr_doc_effectivity.aircraft_code` → `aircraft_assembles`
- `dmg_rpr_doc_effectivity.dmg_rpr_doc_effectivity_id` → `dmg_rpr_doc_effectivity`
- `dmg_rpr_doc_effectivity.fleet_code` → `amp_datmig_fleet_visit_pack`
- `dmg_rpr_doc_effectivity.sub_fleet_id` → `sub_fleet_header`
- `dmg_rpr_doc_subject.subject_id` → `dmg_rpr_doc_subject`
- `dmg_rpr_document_order.aircraft_code` → `aircraft_assembles`
- `dmg_rpr_document_order.fleet_code` → `amp_datmig_fleet_visit_pack`
- `dmg_rpr_document_order.order_number` → `batch_orders`
- `dmg_rpr_document_order.sub_fleet_id` → `sub_fleet_header`
- `dmg_rpr_documents.document_image_id` → `document_image_source`
- `dmg_rpr_documents.subject_id` → `dmg_rpr_doc_subject`
- `dmg_rpr_fitted_locations.aircraft_code` → `aircraft_assembles`
- `dmg_rpr_fitted_locations.damage_id` → `dmg_rpr_damage`
- `dmg_rpr_fitted_locations.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `dmg_rpr_fitted_locations.serial_number` → `completion_part_serial`
- `dmg_rpr_idnt_inspect.inspection_id` → `dmg_rpr_inspection_type_dtls`
- `dmg_rpr_idnt_inspect_info.inspection_id` → `dmg_rpr_inspection_type_dtls`
- `dmg_rpr_inspection_type_dtls.inspection_type_id` → `dmg_rpr_inspection_type_dtls`
- `dmg_rpr_inspections.damage_id` → `dmg_rpr_damage`
- `dmg_rpr_inspections.frequency_id` → `rfc_frequency_phase_header`
- `dmg_rpr_inspections.inspection_id` → `dmg_rpr_inspection_type_dtls`
- `dmg_rpr_inspections.inspection_type_id` → `dmg_rpr_inspection_type_dtls`
- `dmg_rpr_inspections.interim_repair_id` → `dmg_rpr_interim_repairs`
- `dmg_rpr_inspections.paragraph_id` → `paragraph_cancels`
- `dmg_rpr_inspections.rfc_id` → `fleet_forecast_plans_rfc`
- `dmg_rpr_inspections.time_limited_repair_id` → `dmg_rpr_time_limited_repairs`
- `dmg_rpr_inspections.workcard_number` → `amp_access_panels_by_workcard`
- `dmg_rpr_interim_repairs.damage_id` → `dmg_rpr_damage`
- `dmg_rpr_interim_repairs.frequency_id` → `rfc_frequency_phase_header`
- `dmg_rpr_interim_repairs.interim_repair_id` → `dmg_rpr_interim_repairs`
- `dmg_rpr_interim_repairs.paragraph_id` → `paragraph_cancels`
- `dmg_rpr_interim_repairs.rfc_id` → `fleet_forecast_plans_rfc`
- `dmg_rpr_interim_repairs.workcard_number` → `amp_access_panels_by_workcard`
- `dmg_rpr_location.aircraft_code` → `aircraft_assembles`
- `dmg_rpr_location.damage_id` → `dmg_rpr_damage`
- `dmg_rpr_location.material_type_id` → `dmg_rpr_material_types_dtls`
- `dmg_rpr_location.position_id` → `dmg_rpr_dmg_2d_position_labels`
- `dmg_rpr_location.surface_finish_id` → `dmg_rpr_surface_finish_details`
- `dmg_rpr_location_measurement.damage_id` → `dmg_rpr_damage`
- `dmg_rpr_location_measurement.measurement_id` → `dmg_rpr_location_measurement`
- `dmg_rpr_mat_types_fld_dtls.material_type_id` → `dmg_rpr_material_types_dtls`
- `dmg_rpr_material_types_dtls.material_type_id` → `dmg_rpr_material_types_dtls`
- `dmg_rpr_measurement_sections.measurement_id` → `dmg_rpr_location_measurement`
- `dmg_rpr_measurement_sections.measurement_section_id` → `dmg_rpr_measurement_sections`
- `dmg_rpr_measurement_sections.section_id` → `amp_workcard_sections`
- `dmg_rpr_measurement_zones.measurement_id` → `dmg_rpr_location_measurement`
- `dmg_rpr_measurement_zones.measurement_zone_id` → `dmg_rpr_measurement_zones`
- `dmg_rpr_measurements.measurement_id` → `dmg_rpr_location_measurement`
- `dmg_rpr_permanent_repairs.damage_id` → `dmg_rpr_damage`
- `dmg_rpr_permanent_repairs.frequency_id` → `rfc_frequency_phase_header`
- `dmg_rpr_permanent_repairs.paragraph_id` → `paragraph_cancels`
- `dmg_rpr_permanent_repairs.repair_id` → `consumable_repair_xref_to_part`
- `dmg_rpr_permanent_repairs.rfc_id` → `fleet_forecast_plans_rfc`
- `dmg_rpr_permanent_repairs.workcard_number` → `amp_access_panels_by_workcard`
- `dmg_rpr_repair_req_details.damage_id` → `dmg_rpr_damage`
- `dmg_rpr_repair_req_details.requirement_number` → `nrc_requirements_actions`
- `dmg_rpr_section_details.section_id` → `amp_workcard_sections`
- `dmg_rpr_section_fleet_details.section_id` → `amp_workcard_sections`
- `dmg_rpr_stage_limits.life_code_level_id` → `life_code_levels`
- `dmg_rpr_stage_limits.limit_id` → `amp_component_intervals_limits`
- `dmg_rpr_stage_limits.stage_id` → `amp_component_intervals_stages`
- `dmg_rpr_stages.inspection_id` → `dmg_rpr_inspection_type_dtls`
- `dmg_rpr_stages.interim_repair_id` → `dmg_rpr_interim_repairs`
- `dmg_rpr_stages.permanent_repair_id` → `dmg_rpr_permanent_repairs`
- `dmg_rpr_stages.stage_id` → `amp_component_intervals_stages`
- `dmg_rpr_stages.time_limited_repair_id` → `dmg_rpr_time_limited_repairs`
- `dmg_rpr_subject_sections.section_id` → `amp_workcard_sections`
- `dmg_rpr_subject_sections.subject_id` → `dmg_rpr_doc_subject`
- `dmg_rpr_subject_sections.subject_section_id` → `dmg_rpr_subject_sections`
- `dmg_rpr_subject_zones.subject_id` → `dmg_rpr_doc_subject`
- `dmg_rpr_subject_zones.subject_zone_id` → `dmg_rpr_subject_zones`
- `dmg_rpr_surface_finish_details.surface_finish_id` → `dmg_rpr_surface_finish_details`
- `dmg_rpr_time_limited_repairs.damage_id` → `dmg_rpr_damage`
- `dmg_rpr_time_limited_repairs.frequency_id` → `rfc_frequency_phase_header`
- `dmg_rpr_time_limited_repairs.paragraph_id` → `paragraph_cancels`
- `dmg_rpr_time_limited_repairs.rfc_id` → `fleet_forecast_plans_rfc`
- `dmg_rpr_time_limited_repairs.time_limited_repair_id` → `dmg_rpr_time_limited_repairs`
- `dmg_rpr_time_limited_repairs.workcard_number` → `amp_access_panels_by_workcard`
- `document_classes.document_id` → `aircraft_documents`
- `document_image_source.document_image_source_id` → `document_image_source`
- `document_image_types.document_image_source_id` → `document_image_source`
- `document_images_jn.document_image_id` → `document_image_source`
- `drn_class_codes.class_code` → `document_classes`
- `drn_component_mods_history.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `drn_component_mods_history.report_id` → `amp_report_documents`
- `drn_component_mods_history.serial_number` → `completion_part_serial`
- `drn_components_nsbl_history.life_code_level_id` → `life_code_levels`
- `drn_components_nsbl_history.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `drn_components_nsbl_history.serial_number` → `completion_part_serial`
- `drn_cycles.aircraft_code` → `aircraft_assembles`
- `drn_cycles.cycle_number` → `accum_cycles_static_data`
- `drn_fleet_ata.aircraft_code` → `aircraft_assembles`
- `drn_fleet_ata.class_code` → `document_classes`
- `drn_life_limits.aircraft_code` → `aircraft_assembles`
- `drn_life_limits.life_code_level_id` → `life_code_levels`
- `drn_life_limits.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `drn_life_limits.serial_number` → `completion_part_serial`
- `drn_maint_mod.aircraft_code` → `aircraft_assembles`
- `drn_maint_mod.class_code` → `document_classes`
- `drn_maint_mod.drn_cycle_number` → `drn_cycles`
- `drn_maint_mod_notes.aircraft_code` → `aircraft_assembles`
- `drn_maintenance_history.aircraft_code` → `aircraft_assembles`
- `drn_maintenance_history.class_code` → `document_classes`
- `drn_maintenance_history.report_id` → `amp_report_documents`
- `drn_maintenance_history_notes.aircraft_code` → `aircraft_assembles`
- `drn_mod_desc_order_hist.aircraft_code` → `aircraft_assembles`
- `drn_mod_desc_order_hist.class_code` → `document_classes`
- `drn_modification_history.aircraft_code` → `aircraft_assembles`
- `drn_modification_history.class_code` → `document_classes`
- `drn_modification_history.report_id` → `amp_report_documents`
- `drn_modification_history_notes.aircraft_code` → `aircraft_assembles`
- `drn_part_serial.class_code` → `document_classes`
- `drn_part_serial.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `drn_part_serial.serial_number` → `completion_part_serial`
- `dummy_part_numbers.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `easa_trace.trace_id` → `easa_trace`
- `email_notification.category_id` → `maint_cost_time_category_set`
- `email_template.template_id` → `email_template`
- `employee_experience_details.employee_number` → `defect_stage_employees`
- `employee_experience_details.experience_id` → `employee_experience_details`
- `employee_presence.employee_number` → `defect_stage_employees`
- `employee_presence_log.employee_number` → `defect_stage_employees`
- `employee_presence_log.task_number` → `amp_datmig_comp_task_lookup`
- `employee_training_details.employee_number` → `defect_stage_employees`
- `employee_training_details.training_id` → `employee_training_details`
- `employees.trade_code` → `trades`
- `end_use_codes.end_use_code` → `end_use_codes`
- `engineering_support_history.defect_number` → `defect_extensions`
- `engineering_support_history.engineering_support_history_id` → `engineering_support_history`
- `engineering_support_history.workcard_number` → `amp_access_panels_by_workcard`
- `esign_off_nrc.document_id` → `aircraft_documents`
- `esign_off_nrc.nrc_number` → `cq_quote_nrc_access_panels`
- `export_codes.export_code` → `export_codes`
- `export_codes.export_id` → `export_codes`
- `extended_part_descriptions.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `extensions.extension_id` → `add_extension_permissions`
- `fleet_assembles.fleet_code` → `amp_datmig_fleet_visit_pack`
- `fleet_chap_part_header_1.alternate_part_number` → `alternate_parts`
- `fleet_chap_part_header_1.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `fleet_chap_part_header_2.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `fleet_chap_part_header_3.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `fleet_chapter_part_aircraft.aircraft_code` → `aircraft_assembles`
- `fleet_chapter_part_aircraft.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `fleet_forecast_plans.aircraft_code` → `aircraft_assembles`
- `fleet_forecast_plans.class_code` → `document_classes`
- `fleet_forecast_plans.plan_id` → `amp_planning_notes`
- `fleet_forecast_plans.revision_id` → `amp_revision_history`
- `fleet_forecast_plans_amp.package_codes` → `amp_packages`
- `fleet_forecast_plans_amp.plan_id` → `amp_planning_notes`
- `fleet_forecast_plans_amp.visit_codes` → `amp_visits`
- `fleet_forecast_plans_amp.workcard_numbers` → `amp_workcards_by_package`
- `fleet_forecast_plans_drn.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `fleet_forecast_plans_drn.plan_id` → `amp_planning_notes`
- `fleet_forecast_plans_drn.serial_number` → `completion_part_serial`
- `fleet_forecast_plans_rfc.plan_id` → `amp_planning_notes`
- `fleet_forecast_plans_rfc.rfc_id` → `fleet_forecast_plans_rfc`
- `fleet_statistics.workcard_number` → `amp_access_panels_by_workcard`
- `float_history.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `float_history.user_id` → `dataset_locks_by_user`
- `flown_sectors_bkp.aircraft_code` → `aircraft_assembles`
- `flown_sectors_bkp.flight_number` → `aircraft_flight_hours_1`
- `flown_sectors_bkp.report_id` → `amp_report_documents`
- `flown_sectors_bkp.sector_id` → `flown_sectors`
- `flown_sectors_con_680.aircraft_code` → `aircraft_assembles`
- `flown_sectors_con_680.flight_number` → `aircraft_flight_hours_1`
- `flown_sectors_con_680.report_id` → `amp_report_documents`
- `flown_sectors_con_680.sector_id` → `flown_sectors`
- `flown_sectors_delta1817.aircraft_code` → `aircraft_assembles`
- `flown_sectors_delta1817.flight_number` → `aircraft_flight_hours_1`
- `flown_sectors_delta1817.report_id` → `amp_report_documents`
- `flown_sectors_delta1817.sector_id` → `flown_sectors`
- `forecast_cache.aircraft_code` → `aircraft_assembles`
- `forecast_cache.alert_number` → `alert_colors`
- `forecast_cache.class_code` → `document_classes`
- `forecast_cache.component_life_limit_id` → `component_life_limits`
- `forecast_cache.package_code` → `amp_package_notes`
- `forecast_cache.revision_id` → `amp_revision_history`
- `forecast_cache.rfc_id` → `fleet_forecast_plans_rfc`
- `forecast_cache.visit_code` → `amp_datmig_fleet_visit_pack`
- `forecast_cache.workcard_code` → `amp_access_panels_by_workcard`
- `forecast_cache.workcard_interval_id` → `amp_workcard_intervals`
- `forecast_cache.works_order_number` → `credit_works_order_cards`
- `forecast_cache_ac_details.revision_id` → `amp_revision_history`
- `forecast_cache_revisions.revision_id` → `amp_revision_history`
- `forecast_filter_groups.group_id` → `forecast_filter_groups`
- `forecast_filters.filter_id` → `forecast_filter_groups`
- `forecast_filters.group_id` → `forecast_filter_groups`
- `forecast_parameters.param_id` → `forecast_parameters`
- `forecast_variation_details.workcard_number` → `amp_access_panels_by_workcard`
- `form_number.form_number` → `company_form_attachments`
- `form_number.form_number_id` → `form_number`
- `forward_schedule_summary_vals.life_code_level_id` → `life_code_levels`
- `freight_cost_markups.freight_cost_markup_id` → `freight_cost_markups`
- `freight_costs.freight_cost_id` → `freight_cost_markups`
- `freight_costs.order_number` → `batch_orders`
- `freight_costs.shipment_item_id` → `shipment_item`
- `gl_global_codes.gl_id` → `gl_global_codes`
- `goods_received_sheet_document.batch_number` → `batch_file_header`
- `goods_received_sheet_document.document_image_id` → `document_image_source`
- `hazardous_materials.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `ie96_historic.account_code` → `access_dim_accounts_info`
- `ie96_historic.batch_number` → `batch_file_header`
- `ie96_historic.bin_number` → `bins`
- `ie96_historic.inv_number` → `invoice_categories`
- `ie96_historic.order_number` → `batch_orders`
- `ie96_historic.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `ie96_historic.price_type_code` → `price_types`
- `ie96_historic.serial_number` → `completion_part_serial`
- `inherited_acquisition_costs.batch_number` → `batch_file_header`
- `inherited_acquisition_costs.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `inherited_acquisition_costs.serial_number` → `completion_part_serial`
- `invoice_line_notes.invoice_number` → `invoice_categories`
- `invoice_lines.account_code` → `access_dim_accounts_info`
- `invoice_lines.batch_number` → `batch_file_header`
- `invoice_lines.currency_code` → `currency_codes`
- `invoice_lines.goods_received_number` → `goods_received_sheet_document`
- `invoice_lines.invoice_number` → `invoice_categories`
- `invoice_lines.order_number` → `batch_orders`
- `invoice_lines.vat_code` → `amp_workcard_activations`
- `invoice_system_header.key_id` → `osys_key_to_reportid`
- `invoice_trail_entries.batch_number` → `batch_file_header`
- `invoice_trail_entries.currency_code` → `currency_codes`
- `invoice_trail_entries.invoice_number` → `invoice_categories`
- `invoice_trail_entries.invoice_trail_id` → `invoice_trail_entries`
- `invoice_trail_entries.order_number` → `batch_orders`
- `invoice_trail_entries.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `invoice_trail_entries.serial_number` → `completion_part_serial`
- `invoices.account_code` → `access_dim_accounts_info`
- `invoices.currency_code` → `currency_codes`
- `invoices.invoice_number` → `invoice_categories`
- `jasper_workcard_templates.template_id` → `email_template`
- `lasers_system_header.key_id` → `osys_key_to_reportid`
- `latest_repair_values.currency_code` → `currency_codes`
- `latest_repair_values.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `latest_repair_values.serial_number` → `completion_part_serial`
- `ldt.life_code_level_id` → `life_code_levels`
- `le80_defect_temp.aircraft_code` → `aircraft_assembles`
- `life_code_entry_backup.aircraft_code` → `aircraft_assembles`
- `life_code_entry_backup.life_code_level_id` → `life_code_levels`
- `life_code_entry_backup.report_id` → `amp_report_documents`
- `life_code_entry_dbf1065.aircraft_code` → `aircraft_assembles`
- `life_code_entry_dbf1065.life_code_level_id` → `life_code_levels`
- `life_code_entry_dbf1065.report_id` → `amp_report_documents`
- `lmc_base_data_options.aircraft_code` → `aircraft_assembles`
- `lmc_base_data_options.opt_id` → `lmc_base_data_options`
- `lmc_base_data_reported_wc.lmc_base_data_id` → `lmc_base_data_defs`
- `lmc_base_data_reported_wc.workcard_number` → `amp_access_panels_by_workcard`
- `maint_accomplishment_costs.accomplishment_id` → `accomplishment_history`
- `maint_accomplishment_costs.maint_cost_id` → `maint_cost_budget_adsb`
- `maint_associated_cost_aircraft.aircraft_code` → `aircraft_assembles`
- `maint_associated_cost_aircraft.associated_cost_id` → `maint_associated_cost_aircraft`
- `maint_associated_cost_aircraft.category_id` → `maint_cost_time_category_set`
- `maint_associated_costs.associated_cost_id` → `maint_associated_cost_aircraft`
- `maint_associated_costs.currency_code` → `currency_codes`
- `maint_card_pref_cost_cats.workcard_number` → `amp_access_panels_by_workcard`
- `maint_cost_budget_adsb.aircraft_code` → `aircraft_assembles`
- `maint_cost_budget_adsb.budget_id` → `maint_cost_budget_adsb`
- `maint_cost_budget_adsb.frequency_id` → `rfc_frequency_phase_header`
- `maint_cost_budget_adsb.item_id` → `delivery_note_item_header_1`
- `maint_cost_budget_adsb.phase_number` → `rfc_frequency_phase_header`
- `maint_cost_budget_adsb.revision_id` → `amp_revision_history`
- `maint_cost_budget_adsb.rfc_id` → `fleet_forecast_plans_rfc`
- `maint_cost_budget_adsb.workcard_id` → `amp_access_panels_by_workcard`
- `maint_cost_budget_adsb.workcard_number` → `amp_access_panels_by_workcard`
- `maint_cost_budget_aircraft.aircraft_code` → `aircraft_assembles`
- `maint_cost_budget_aircraft.budget_id` → `maint_cost_budget_adsb`
- `maint_cost_budget_cfds.aircraft_code` → `aircraft_assembles`
- `maint_cost_budget_cfds.budget_id` → `maint_cost_budget_adsb`
- `maint_cost_budget_cfds.item_id` → `delivery_note_item_header_1`
- `maint_cost_budget_costs.budget_cost_id` → `maint_cost_budget_costs`
- `maint_cost_budget_costs.budget_id` → `maint_cost_budget_adsb`
- `maint_cost_budget_costs.cost_type_id` → `maintenance_cost_types`
- `maint_cost_budget_costs.item_id` → `delivery_note_item_header_1`
- `maint_cost_budget_defects.aircraft_code` → `aircraft_assembles`
- `maint_cost_budget_defects.budget_cost_id` → `maint_cost_budget_costs`
- `maint_cost_budget_defects.budget_id` → `maint_cost_budget_adsb`
- `maint_cost_budget_labour_ests.budget_id` → `maint_cost_budget_adsb`
- `maint_cost_budget_labour_ests.item_id` → `delivery_note_item_header_1`
- `maint_cost_budget_labour_ests.labour_est_id` → `maint_cost_budget_labour_ests`
- `maint_cost_budget_materials.budget_id` → `maint_cost_budget_adsb`
- `maint_cost_budget_materials.item_id` → `delivery_note_item_header_1`
- `maint_cost_budget_materials.material_id` → `amp_material_effectivity`
- `maint_cost_budget_materials.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `maint_cost_budget_packages.aircraft_code` → `aircraft_assembles`
- `maint_cost_budget_packages.budget_id` → `maint_cost_budget_adsb`
- `maint_cost_budget_packages.item_id` → `delivery_note_item_header_1`
- `maint_cost_budget_packages.package_code` → `amp_package_notes`
- `maint_cost_budget_packages.revision_id` → `amp_revision_history`
- `maint_cost_budget_visits.aircraft_code` → `aircraft_assembles`
- `maint_cost_budget_visits.budget_id` → `maint_cost_budget_adsb`
- `maint_cost_budget_visits.item_id` → `delivery_note_item_header_1`
- `maint_cost_budget_visits.revision_id` → `amp_revision_history`
- `maint_cost_budget_visits.visit_code` → `amp_datmig_fleet_visit_pack`
- `maint_cost_budget_workcards.aircraft_code` → `aircraft_assembles`
- `maint_cost_budget_workcards.budget_id` → `maint_cost_budget_adsb`
- `maint_cost_budget_workcards.cost_code` → `cost_codes`
- `maint_cost_budget_workcards.item_id` → `delivery_note_item_header_1`
- `maint_cost_budget_workcards.package_item_id` → `package_items`
- `maint_cost_budget_workcards.revision_id` → `amp_revision_history`
- `maint_cost_budget_workcards.trade_code` → `trades`
- `maint_cost_budget_workcards.workcard_id` → `amp_access_panels_by_workcard`
- `maint_cost_budget_workcards.workcard_number` → `amp_access_panels_by_workcard`
- `maint_cost_hourly_rate_set.category_set_id` → `maint_cost_time_category_set`
- `maint_cost_hourly_rate_set.hourly_rate_set_id` → `maint_cost_hourly_rate_set`
- `maint_cost_hourly_rates.cost_code` → `cost_codes`
- `maint_cost_hourly_rates.hourly_rate_set_id` → `maint_cost_hourly_rate_set`
- `maint_cost_hourly_rates.time_category_id` → `maint_cost_time_category_set`
- `maint_cost_hourly_rates.trade_code` → `trades`
- `maint_cost_mro_wo_invoices.invoice_id` → `invoice_categories`
- `maint_cost_mro_wo_quotes.quote_id` → `cq_quote_cards`
- `maint_cost_time_categories.category_set_id` → `maint_cost_time_category_set`
- `maint_cost_time_categories.contract_id` → `customer_contract_rates`
- `maint_cost_time_categories.time_category_id` → `maint_cost_time_category_set`
- `maint_cost_time_category_set.category_set_id` → `maint_cost_time_category_set`
- `maint_hist_associated_costs.cost_type_id` → `maintenance_cost_types`
- `maint_hist_associated_costs.maint_cost_id` → `maint_cost_budget_adsb`
- `maint_historic_defects.defect_id` → `defect_extensions`
- `maint_labour_costs.maint_cost_id` → `maint_cost_budget_adsb`
- `maint_material_costs.batch_number` → `batch_file_header`
- `maint_material_costs.maint_cost_id` → `maint_cost_budget_adsb`
- `maint_material_costs.material_cost_id` → `maint_material_costs`
- `maint_material_costs.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `maint_material_costs.serial_number` → `completion_part_serial`
- `maint_nrc_costs.maint_cost_id` → `maint_cost_budget_adsb`
- `maint_nrc_costs.nrc_number` → `cq_quote_nrc_access_panels`
- `maint_pack_pref_cost_cats.package_code` → `amp_package_notes`
- `maint_works_order_costs.maint_cost_id` → `maint_cost_budget_adsb`
- `maintenance_cat_excl_subchap.category_id` → `maint_cost_time_category_set`
- `maintenance_cat_incl_chapter.category_id` → `maint_cost_time_category_set`
- `maintenance_cat_incl_parts.category_id` → `maint_cost_time_category_set`
- `maintenance_cat_incl_parts.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `maintenance_cost_budgets.budget_id` → `maint_cost_budget_adsb`
- `maintenance_cost_cat_fleet.category_id` → `maint_cost_time_category_set`
- `maintenance_cost_categories.category_id` → `maint_cost_time_category_set`
- `maintenance_cost_entry.cost_id` → `cost_codes`
- `maintenance_cost_entry.entry_id` → `batches_by_customs_entry`
- `maintenance_cost_invoices.currency_code` → `currency_codes`
- `maintenance_cost_invoices.invoice_id` → `invoice_categories`
- `maintenance_cost_quotes.account_code` → `access_dim_accounts_info`
- `maintenance_cost_quotes.currency_code` → `currency_codes`
- `maintenance_cost_quotes.quote_id` → `cq_quote_cards`
- `maintenance_cost_types.cost_id` → `cost_codes`
- `mandatory_parts.cost_code` → `cost_codes`
- `manufacturers_work_documents.document_id` → `aircraft_documents`
- `manufacturers_work_documents.revision_id` → `amp_revision_history`
- `marketing_codes.marketing_code` → `marketing_codes`
- `markups.markup_code` → `freight_cost_markups`
- `material_pool_agreement.agreement_id` → `material_pool_agreement`
- `material_pool_agreement.currency_code` → `currency_codes`
- `material_pool_agreement_ac.agreement_id` → `material_pool_agreement`
- `material_pool_agreement_ac.aircraft_code` → `aircraft_assembles`
- `material_pool_agreement_pn.agreement_id` → `material_pool_agreement`
- `material_pool_agreement_pn.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `mavis_system_header.key_id` → `osys_key_to_reportid`
- `maximum_preload_pick_quantity.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `mel_items.revision_id` → `amp_revision_history`
- `mel_references.revision_id` → `amp_revision_history`
- `mel_revision_history.history_id` → `accomplishment_history`
- `mel_revision_history.revision_id` → `amp_revision_history`
- `mel_revision_history.user_id` → `dataset_locks_by_user`
- `mel_revisions.revision_id` → `amp_revision_history`
- `monthly_loans_in.order_number` → `batch_orders`
- `monthly_loans_in.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `monthly_loans_in.serial_number` → `completion_part_serial`
- `monthly_loans_out.delivery_note_number` → `delivery_note_extended_remarks`
- `monthly_loans_out.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `monthly_loans_out.serial_number` → `completion_part_serial`
- `n_s_extended_part_descriptions.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `netline_import_index.report_id` → `amp_report_documents`
- `no_narrative_default.aircraft_code` → `aircraft_assembles`
- `non_stock_parts_bkp_oases382.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `non_stock_parts_bkp_oases382.stock_check_code` → `random_stock_check_bins`
- `nrc_defect_notes.defect_number` → `defect_extensions`
- `nrc_defect_notes.workcard_number` → `amp_access_panels_by_workcard`
- `nrc_high_sequence_control.key_id` → `osys_key_to_reportid`
- `nrc_print_history.defect_number` → `defect_extensions`
- `nrc_print_history.print_history_id` → `nrc_print_history`
- `nrc_print_history.workcard_number` → `amp_access_panels_by_workcard`
- `nrc_properties.nrc_number` → `cq_quote_nrc_access_panels`
- `nrc_rectification_notes.defect_number` → `defect_extensions`
- `nrc_rectification_notes.workcard_number` → `amp_access_panels_by_workcard`
- `nrc_status_history.defect_number` → `defect_extensions`
- `nrc_status_history.status_code` → `amp_revision_status`
- `nrc_status_history.status_history_id` → `nrc_status_history`
- `nrc_status_history.workcard_number` → `amp_access_panels_by_workcard`
- `nrc_workcard_narrative.nrc_number` → `cq_quote_nrc_access_panels`
- `nrc_xref_to_scheduled_workcard.defect_number` → `defect_extensions`
- `nrc_xref_to_scheduled_workcard.nrc_number` → `cq_quote_nrc_access_panels`
- `nrc_xref_to_scheduled_workcard.workcard_number` → `amp_access_panels_by_workcard`
- `oases_message_log.log_number` → `amp_data_migration_log`
- `oases_reports.report_id` → `amp_report_documents`
- `oeim_invoice.invoice_number` → `invoice_categories`
- `oeim_invoice_snap_con_rates.cost_code` → `cost_codes`
- `oeim_invoice_snap_con_rates.invoice_number` → `invoice_categories`
- `oeim_invoice_snap_con_rates.time_category_id` → `maint_cost_time_category_set`
- `oeim_invoice_snap_cost_codes.cost_code` → `cost_codes`
- `oeim_invoice_snap_cost_codes.invoice_number` → `invoice_categories`
- `oeim_invoice_snap_currencies.currency_code` → `currency_codes`
- `oeim_invoice_snap_currencies.invoice_number` → `invoice_categories`
- `oeim_invoice_snap_departments.department_id` → `departments`
- `oeim_invoice_snap_departments.export_code` → `export_codes`
- `oeim_invoice_snap_departments.invoice_number` → `invoice_categories`
- `oeim_invoice_snap_employees.employee_number` → `defect_stage_employees`
- `oeim_invoice_snap_employees.invoice_number` → `invoice_categories`
- `oeim_invoice_snap_employees.trade_code` → `trades`
- `oeim_invoice_snap_part_master.invoice_number` → `invoice_categories`
- `oeim_invoice_snap_part_master.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `oeim_invoice_snap_pay_types.invoice_number` → `invoice_categories`
- `oeim_invoice_snap_pay_types.payment_code` → `payment_types`
- `oeim_invoice_snap_pm_bkup.invoice_number` → `invoice_categories`
- `oeim_invoice_snap_pm_bkup.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `oeim_invoice_snap_public_hol.invoice_number` → `invoice_categories`
- `oeim_invoice_snap_serl_master.invoice_number` → `invoice_categories`
- `oeim_invoice_snap_serl_master.long_serial_number` → `long_serial_number_xref`
- `oeim_invoice_snap_serl_master.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `oeim_invoice_snap_serl_master.serial_number` → `completion_part_serial`
- `oeim_invoice_snap_sfdc_book.booking_id` → `oeim_booking_base_data`
- `oeim_invoice_snap_sfdc_book.defect_code` → `defect_extensions`
- `oeim_invoice_snap_sfdc_book.employee_number` → `defect_stage_employees`
- `oeim_invoice_snap_sfdc_book.invoice_number` → `invoice_categories`
- `oeim_invoice_snap_sfdc_book.task_number` → `amp_datmig_comp_task_lookup`
- `oeim_invoice_snap_time_crits.invoice_number` → `invoice_categories`
- `oeim_invoice_snap_users.invoice_number` → `invoice_categories`
- `oeim_invoice_snap_users.oases_id` → `cfd_categorires_bkpoases405`
- `oeim_invoice_snap_vat_codes.export_id` → `export_codes`
- `oeim_invoice_snap_vat_codes.invoice_number` → `invoice_categories`
- `oeim_invoice_snap_vat_codes.vat_code` → `amp_workcard_activations`
- `oeim_invoice_works_orders.account_code` → `access_dim_accounts_info`
- `oeim_invoice_works_orders.invoice_number` → `invoice_categories`
- `oeim_quote_dismissed.invoice_number` → `invoice_categories`
- `oeim_quote_dismissed.package_code` → `amp_package_notes`
- `oeim_quote_dismissed.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `oeim_quote_dismissed.workcard_number` → `amp_access_panels_by_workcard`
- `oeim_transaction_log_details.detail_number` → `aircraft_lease_details`
- `oeim_transaction_log_details.log_number` → `amp_data_migration_log`
- `oeim_transaction_log_header.log_number` → `amp_data_migration_log`
- `ord_po_unit_conv_delta1827.order_number` → `batch_orders`
- `order_change_history.history_id` → `accomplishment_history`
- `order_change_history.order_number` → `batch_orders`
- `order_change_history.preorder_id` → `preorder_line_requirement_xref`
- `order_customs_info.order_number` → `batch_orders`
- `order_delivery_note_remarks.order_number` → `batch_orders`
- `order_email_chasing.order_number` → `batch_orders`
- `order_goods_received_invoices.currency_code` → `currency_codes`
- `order_goods_received_invoices.invoice_number` → `invoice_categories`
- `order_goods_received_invoices.order_number` → `batch_orders`
- `order_goods_received_invoices.vat_code` → `amp_workcard_activations`
- `order_header_2.order_number` → `batch_orders`
- `order_header_2.works_order_number` → `credit_works_order_cards`
- `order_header_3.delivery_note_number` → `delivery_note_extended_remarks`
- `order_header_3.order_number` → `batch_orders`
- `order_header_4.employee_number` → `defect_stage_employees`
- `order_header_4.order_number` → `batch_orders`
- `order_history.batch_number` → `batch_file_header`
- `order_history.condition_code` → `condition_codes`
- `order_history.currency_code` → `currency_codes`
- `order_history.invoice_number` → `invoice_categories`
- `order_history.order_number` → `batch_orders`
- `order_history.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `order_history.serial_number` → `completion_part_serial`
- `order_line_additional_info.airway_bill_number` → `airway_bill_references`
- `order_line_additional_info.condition_code` → `condition_codes`
- `order_line_additional_info.order_number` → `batch_orders`
- `order_line_additional_info.release_code` → `release_codes`
- `order_line_additional_info_2.order_number` → `batch_orders`
- `order_line_notes.order_number` → `batch_orders`
- `order_line_quotes_data.currency_code` → `currency_codes`
- `order_line_quotes_data.order_number` → `batch_orders`
- `order_line_quotes_data.vat_code` → `amp_workcard_activations`
- `order_line_requirement_xref.order_number` → `batch_orders`
- `order_line_requirement_xref.requirement_number` → `nrc_requirements_actions`
- `order_line_weight_dimension.dimension_id` → `order_line_weight_dimension`
- `order_line_weight_dimension.order_number` → `batch_orders`
- `order_numbers_by_supplier.account_code` → `access_dim_accounts_info`
- `order_numbers_by_supplier.order_number` → `batch_orders`
- `order_print_date.order_number` → `batch_orders`
- `order_purchase_unit_conversion.order_number` → `batch_orders`
- `order_standard_text_blocks.block_number` → `block_countries`
- `order_supplier_approval.order_number` → `batch_orders`
- `order_supplier_approval.supplier_approval_number` → `account_supplier_approvals`
- `order_text.order_number` → `batch_orders`
- `order_workshop_works_orders.order_number` → `batch_orders`
- `orders_by_due_date.order_number` → `batch_orders`
- `orders_to_part_number_xref.order_number` → `batch_orders`
- `orders_to_part_number_xref.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `ordr_goods_bkp.goods_received_number` → `goods_received_sheet_document`
- `ordr_goods_bkp.order_number` → `batch_orders`
- `ordr_goods_bkp.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `osys_defect_act_to_defect_id.defect_id` → `defect_extensions`
- `osys_defect_to_defect_id.defect_id` → `defect_extensions`
- `osys_defect_to_defect_id.defect_number` → `defect_extensions`
- `osys_defect_to_tech_log_line.defect_number` → `defect_extensions`
- `osys_key_to_reportid.report_id` → `amp_report_documents`
- `outstation_codes.outstation_code` → `outstation_codes`
- `package.package_id` → `amp_package_notes`
- `package.shipment_id` → `shipment`
- `package_items.item_id` → `delivery_note_item_header_1`
- `package_items.package_id` → `amp_package_notes`
- `package_items.package_items_id` → `package_items`
- `paragraph_cancels.paragraph_id` → `paragraph_cancels`
- `paragraph_cancels.rfc_id` → `fleet_forecast_plans_rfc`
- `part_applicability_codes.applicability_code` → `amp_workcard_lcl_applicability`
- `part_change_warning_chapters.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_change_warnings.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_customs_tariff_territory.customs_tariff_code` → `customs_tariff_codes`
- `part_customs_tariff_territory.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_master_bkp_oases382.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_master_bkp_oases382.stock_check_code` → `random_stock_check_bins`
- `part_number_amendment_history.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_number_amendment_history.user_id` → `dataset_locks_by_user`
- `part_number_chapters.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_number_essentiality_codes.essentiality_code` → `part_number_essentiality_codes`
- `part_number_essentiality_codes.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_number_marketing_codes.marketing_code` → `marketing_codes`
- `part_number_marketing_codes.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_number_order_retention.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_number_shelf_life_details.component_life_limit_id` → `component_life_limits`
- `part_number_shelf_life_details.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_number_technical_notes.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_number_vat_codes.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_number_vat_codes.vat_code` → `amp_workcard_activations`
- `part_serial_documents.document_image_id` → `document_image_source`
- `part_serial_documents.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_serial_documents.part_serial_document_id` → `part_serial_documents`
- `part_serial_documents.serial_number` → `completion_part_serial`
- `part_serial_master_list.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_xref_to_pick_history.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_xref_to_pick_history.pick_number` → `condition_pick_table`
- `part_xref_to_pick_history.requirement_number` → `nrc_requirements_actions`
- `parts_customs_tariff_codes.customs_tariff_code` → `customs_tariff_codes`
- `parts_customs_tariff_codes.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `parts_freight_tiered_markups.freight_cost_markup_id` → `freight_cost_markups`
- `parts_received_without_cost.order_number` → `batch_orders`
- `parts_received_without_cost.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `parts_requiring_export_licence.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `pick_hist_7890_bkp.alternate_part_number` → `alternate_parts`
- `pick_hist_7890_bkp.batch_number` → `batch_file_header`
- `pick_hist_7890_bkp.order_number` → `batch_orders`
- `pick_hist_7890_bkp.pick_number` → `condition_pick_table`
- `pick_hist_7890_bkp.requirement_number` → `nrc_requirements_actions`
- `pick_hist_7890_bkp.serial_number` → `completion_part_serial`
- `pick_history.alternate_part_number` → `alternate_parts`
- `pick_history.batch_number` → `batch_file_header`
- `pick_history.order_number` → `batch_orders`
- `pick_history.pick_number` → `condition_pick_table`
- `pick_history.requirement_number` → `nrc_requirements_actions`
- `pick_history.serial_number` → `completion_part_serial`
- `pirep_index_data.aircraft_code` → `aircraft_assembles`
- `planners_notes.category_id` → `maint_cost_time_category_set`
- `planners_notes.notes_xref_id` → `planners_notes_xref`
- `planners_notes.status_id` → `amp_revision_status`
- `planners_notes_statuses.status_id` → `amp_revision_status`
- `planners_notes_xref.aircraft_code` → `aircraft_assembles`
- `planners_notes_xref.alert_number` → `alert_colors`
- `planners_notes_xref.package_code` → `amp_package_notes`
- `planners_notes_xref.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `planners_notes_xref.revision_id` → `amp_revision_history`
- `planners_notes_xref.rfc_id` → `fleet_forecast_plans_rfc`
- `planners_notes_xref.serial_number` → `completion_part_serial`
- `planners_notes_xref.visit_code` → `amp_datmig_fleet_visit_pack`
- `planners_notes_xref.workcard_interval_id` → `amp_workcard_intervals`
- `preorder_line_requirement_xref.preorder_id` → `preorder_line_requirement_xref`
- `preorder_line_requirement_xref.requirement_number` → `nrc_requirements_actions`
- `preorder_line_stock_info.batch_number` → `batch_file_header`
- `preorder_line_stock_info.bin_number` → `bins`
- `preorder_line_stock_info.movement_code` → `component_movement_hist_life`
- `preorder_line_stock_info.preorder_id` → `preorder_line_requirement_xref`
- `preorder_line_stock_info.serial_number` → `completion_part_serial`
- `preorder_lines.condition_code` → `condition_codes`
- `preorder_lines.non_stock_part_number` → `non_stock_parts`
- `preorder_lines.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `preorder_lines.preorder_id` → `preorder_line_requirement_xref`
- `preorder_lines.release_code` → `release_codes`
- `preorder_lines.vat_code` → `amp_workcard_activations`
- `preorders.account_code` → `access_dim_accounts_info`
- `preorders.company_code` → `company_codes`
- `preorders.currency_code` → `currency_codes`
- `preorders.employee_number` → `defect_stage_employees`
- `preorders.preorder_id` → `preorder_line_requirement_xref`
- `price_codes.price_code` → `price_codes`
- `purchase_demand_by_part.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `quote_email_chasing.order_number` → `batch_orders`
- `quotes_by_part.account_code` → `access_dim_accounts_info`
- `quotes_by_part.currency_code` → `currency_codes`
- `quotes_by_part.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `quotes_for_part_by_account.account_code` → `access_dim_accounts_info`
- `quotes_for_part_by_account.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `random_stock_check_bins.bin_number` → `bins`
- `random_stock_check_bins.warehouse_code` → `account_available_warehouses`
- `random_stock_check_date.warehouse_code` → `account_available_warehouses`
- `random_stock_check_log.warehouse_code` → `account_available_warehouses`
- `random_stock_check_parts.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `random_stock_check_parts.warehouse_code` → `account_available_warehouses`
- `rd_xref_to_tech_logs.aircraft_code` → `aircraft_assembles`
- `rd_xref_to_tech_logs.alert_number` → `alert_colors`
- `rd_xref_to_tech_logs.key_id` → `osys_key_to_reportid`
- `rd_xref_to_tech_logs.status_code` → `amp_revision_status`
- `rdi_history.alert_number` → `alert_colors`
- `rdi_history.user_id` → `dataset_locks_by_user`
- `rdi_to_nrc.nrc_number` → `cq_quote_nrc_access_panels`
- `rdi_to_nrc.rdi_number` → `rdi_history`
- `release_codes.release_code` → `release_codes`
- `reliability_report_logo_desc.document_image_id` → `document_image_source`
- `reliability_report_logo_desc.logo_desc_id` → `reliability_report_logo_desc`
- `repair_approval_data.account_code` → `access_dim_accounts_info`
- `repair_approval_data.batch_number` → `batch_file_header`
- `repair_approval_data.movement_code` → `component_movement_hist_life`
- `repetitive_defect_header_1.aircraft_code` → `aircraft_assembles`
- `repetitive_defect_header_1.alert_number` → `alert_colors`
- `repetitive_defect_header_2.alert_number` → `alert_colors`
- `repetitive_defect_narrative.alert_number` → `alert_colors`
- `repetitive_defect_narrative.user_id` → `dataset_locks_by_user`
- `repetitive_defect_tech_logs.alert_number` → `alert_colors`
- `repetitive_defect_tech_logs.sequence_number` → `nrc_high_sequence_control`
- `req_priority_desc_oases_1228.priority_id` → `req_priority_desc_oases_1228`
- `requests_for_quotes.rfq_number` → `requirement_to_rfq_xref`
- `requests_for_quotes_lines.movement_code` → `component_movement_hist_life`
- `requests_for_quotes_lines.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `requests_for_quotes_lines.release_code` → `release_codes`
- `requests_for_quotes_lines.rfq_number` → `requirement_to_rfq_xref`
- `requests_for_quotes_notes.rfq_number` → `requirement_to_rfq_xref`
- `requirement_planners_notes.requirement_number` → `nrc_requirements_actions`
- `requirement_priority_desc.priority_id` → `req_priority_desc_oases_1228`
- `requirement_priority_leadtimes.priority_code` → `req_priority_desc_oases_1228`
- `requirement_priority_sla.account_code` → `access_dim_accounts_info`
- `requirement_priority_sla.priority_code` → `req_priority_desc_oases_1228`
- `requirement_recharge_details.batch_number` → `batch_file_header`
- `requirement_recharge_details.cost_code` → `cost_codes`
- `requirement_recharge_details.currency_code` → `currency_codes`
- `requirement_recharge_details.requirement_number` → `nrc_requirements_actions`
- `requirement_recharge_details.strip_report_number` → `strip_report_findings_text`
- `requirement_source_codes.source_code` → `document_image_source`
- `rfc_documents.document_image_id` → `document_image_source`
- `rfc_documents.rfc_document_id` → `rfc_documents`
- `rfc_documents.rfc_id` → `fleet_forecast_plans_rfc`
- `rfc_download_effectivity.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `rfc_download_effectivity.taxonomy_id` → `rfc_download_taxonomy`
- `rfc_download_origin_codes.accomplishment_code` → `accomplishment_history`
- `rfc_download_origin_codes.authority_code` → `rfc_regulating_authority`
- `rfc_download_origin_codes.change_origin_code` → `rfc_change_origin`
- `rfc_download_taxonomy.authority_code` → `rfc_regulating_authority`
- `rfc_download_taxonomy.taxonomy_id` → `rfc_download_taxonomy`
- `rfc_evaluation_history.evaluation_history_id` → `rfc_evaluation_history`
- `rfc_evaluation_history.rfc_id` → `fleet_forecast_plans_rfc`
- `rfc_header_publications.publication_code` → `amp_workcard_publications`
- `rfc_header_publications.rfc_id` → `fleet_forecast_plans_rfc`
- `rfc_print_history_log.log_id` → `amp_data_migration_log`
- `rfc_print_history_log.rfc_id` → `fleet_forecast_plans_rfc`
- `rfc_publications.publication_code` → `amp_workcard_publications`
- `rfc_statement_sections.section_code` → `amp_workcard_sections`
- `rfc_statement_sections.section_id` → `amp_workcard_sections`
- `rfc_transaction_log.log_id` → `amp_data_migration_log`
- `rfc_transaction_log.rfc_id` → `fleet_forecast_plans_rfc`
- `rfq_by_part_number.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `rfq_by_part_number.rfq_number` → `requirement_to_rfq_xref`
- `rfq_quote_received.account_code` → `access_dim_accounts_info`
- `rfq_quote_received.currency_code` → `currency_codes`
- `rfq_quote_received.rfq_number` → `requirement_to_rfq_xref`
- `rfq_requirement_xref.requirement_number` → `nrc_requirements_actions`
- `rfq_requirement_xref.rfq_number` → `requirement_to_rfq_xref`
- `rfq_supplier_notes.account_code` → `access_dim_accounts_info`
- `rfq_supplier_notes.rfq_number` → `requirement_to_rfq_xref`
- `rotable_float_values.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `rotables_below_re_order.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `rp_base_plan_header.base_plan_id` → `rp_base_plan_header`
- `rp_block_resource.block_id` → `block_countries`
- `rp_block_resource.scope_type_id` → `scope_type_rating`
- `rp_block_resource.shift_id` → `rp_basic_shift`
- `rp_block_resource.trade_code` → `trades`
- `rp_block_resource.warehouse_code` → `account_available_warehouses`
- `rp_block_resource_days.block_id` → `block_countries`
- `rp_block_resource_days.day_id` → `public_holidays`
- `rp_block_resource_days.day_number` → `public_holidays`
- `rp_dependencies.milestone_id` → `rp_milestone_history`
- `rp_dependencies.revision_id` → `amp_revision_history`
- `rp_dependencies.type_id` → `aircraft_types`
- `rp_dependencies.workcard_number` → `amp_access_panels_by_workcard`
- `rp_employee_allocation.allocation_header_id` → `rp_employee_allocation_header`
- `rp_employee_allocation.allocation_id` → `order_requirement_allocation`
- `rp_employee_allocation.nrc_number` → `cq_quote_nrc_access_panels`
- `rp_employee_allocation.workcard_number` → `amp_access_panels_by_workcard`
- `rp_employee_allocation_header.allocation_header_id` → `rp_employee_allocation_header`
- `rp_employee_allocation_header.basic_shift_id` → `rp_basic_shift`
- `rp_employee_allocation_header.employee_number` → `defect_stage_employees`
- `rp_milestone_history.history_id` → `accomplishment_history`
- `rp_milestone_history.milestone_id` → `rp_milestone_history`
- `rp_milestones.milestone_code` → `rp_milestone_history`
- `rp_milestones.milestone_id` → `rp_milestone_history`
- `rp_weekends.weekends_id` → `rp_weekends`
- `rp_wo_base_estimated_defects.base_plan_id` → `rp_base_plan_header`
- `rp_wo_base_estimated_defects.basic_shift_id` → `rp_basic_shift`
- `rp_wo_base_estimated_defects.trade_code` → `trades`
- `rp_wo_base_milestones.base_plan_id` → `rp_base_plan_header`
- `rp_wo_base_milestones.milestone_id` → `rp_milestone_history`
- `rp_wo_base_nrc_plan.base_plan_id` → `rp_base_plan_header`
- `rp_wo_base_nrc_plan.basic_shift_id` → `rp_basic_shift`
- `rp_wo_base_nrc_plan.nrc_number` → `cq_quote_nrc_access_panels`
- `rp_wo_base_workcard_plan.base_plan_id` → `rp_base_plan_header`
- `rp_wo_base_workcard_plan.basic_shift_id` → `rp_basic_shift`
- `rp_wo_base_workcard_plan.workcard_number` → `amp_access_panels_by_workcard`
- `rp_wo_estimated_defects.trade_code` → `trades`
- `rp_wo_milestones.milestone_id` → `rp_milestone_history`
- `sabre_flight_map.report_id` → `amp_report_documents`
- `sabre_trace.trace_id` → `easa_trace`
- `sage_order_line_details.order_number` → `batch_orders`
- `sales_invoice_genled_xref.end_use_code` → `end_use_codes`
- `sales_invoices_xref.invoice_number` → `invoice_categories`
- `sales_invoices_xref.sales_order_number` → `customer_sales_order_xref`
- `sales_order_history.sales_request_number` → `sales_request_quote_detail`
- `sales_order_notes.sales_order_number` → `customer_sales_order_xref`
- `sales_order_parameters.key_id` → `osys_key_to_reportid`
- `sales_order_payments.sales_order_dispatch_number` → `sales_order_dispatches`
- `sales_order_payments.sales_order_number` → `customer_sales_order_xref`
- `sales_order_payments.user_id` → `dataset_locks_by_user`
- `sales_orders.account_code` → `access_dim_accounts_info`
- `sales_orders.company_code` → `company_codes`
- `sales_orders.currency_code` → `currency_codes`
- `sales_orders.sales_order_number` → `customer_sales_order_xref`
- `sales_orders_by_part.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `sales_orders_by_part.sales_order_number` → `customer_sales_order_xref`
- `sales_prices.transaction_type_code` → `transaction_types`
- `sales_quotes_out_history.account_code` → `access_dim_accounts_info`
- `sales_quotes_out_history.condition_code` → `condition_codes`
- `sales_quotes_out_history.currency_code` → `currency_codes`
- `sales_quotes_out_history.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `sales_quotes_out_history.sales_request_number` → `sales_request_quote_detail`
- `sales_request_quote_header.account_code` → `access_dim_accounts_info`
- `sales_request_quote_header.company_code` → `company_codes`
- `sales_request_quote_header.currency_code` → `currency_codes`
- `sales_request_quote_header.sales_request_number` → `sales_request_quote_detail`
- `sales_request_quote_header.user_id` → `dataset_locks_by_user`
- `sales_request_quote_notes.sales_request_number` → `sales_request_quote_detail`
- `sales_requested_unknown_parts.sales_request_number` → `sales_request_quote_detail`
- `sales_requests_by_part.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `sales_requests_by_part.sales_request_number` → `sales_request_quote_detail`
- `sales_requests_by_unknown_part.sales_request_number` → `sales_request_quote_detail`
- `sales_requests_by_unknown_part.unknown_part_number` → `sales_requested_unknown_parts`
- `sample_fleets_jn.aircraft_code` → `aircraft_assembles`
- `sample_fleets_jn.fleet_code` → `amp_datmig_fleet_visit_pack`
- `sap_order_header.order_number` → `batch_orders`
- `sap_order_header.preorder_id` → `preorder_line_requirement_xref`
- `sap_order_line.order_number` → `batch_orders`
- `sap_order_line.preorder_id` → `preorder_line_requirement_xref`
- `schedule_forecast_xref.aircraft_code` → `aircraft_assembles`
- `schedule_forecast_xref.package_code` → `amp_package_notes`
- `schedule_forecast_xref.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `schedule_forecast_xref.rfc_id` → `fleet_forecast_plans_rfc`
- `schedule_forecast_xref.serial_number` → `completion_part_serial`
- `schedule_forecast_xref.visit_code` → `amp_datmig_fleet_visit_pack`
- `schedule_forecast_xref.workcard_id` → `amp_access_panels_by_workcard`
- `schedule_forecast_xref.workcard_interval_id` → `amp_workcard_intervals`
- `schedule_forecast_xref.workcard_number` → `amp_access_panels_by_workcard`
- `schedule_source.aircraft_code` → `aircraft_assembles`
- `schedule_source.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `schedule_source.rfc_id` → `fleet_forecast_plans_rfc`
- `schedule_source.serial_number` → `completion_part_serial`
- `security_audit_log_header.audit_log_id` → `security_audit_log_header`
- `security_audit_log_header.permission_id` → `add_extension_permissions`
- `security_audit_log_meta_data.audit_log_id` → `security_audit_log_header`
- `security_audit_log_meta_data.sequence_number` → `nrc_high_sequence_control`
- `security_group_perm_attribute.attribute_id` → `security_group_perm_attribute`
- `security_group_perm_attribute.group_id` → `forecast_filter_groups`
- `security_group_perm_attribute.permission_id` → `add_extension_permissions`
- `security_group_permissions.group_id` → `forecast_filter_groups`
- `security_group_permissions.permission_id` → `add_extension_permissions`
- `security_group_policies.group_id` → `forecast_filter_groups`
- `security_group_policies.policy_id` → `security_policy`
- `security_groups.group_id` → `forecast_filter_groups`
- `security_permission_def_attrib.attribute_id` → `security_group_perm_attribute`
- `security_permission_def_attrib.permission_id` → `add_extension_permissions`
- `security_policy.policy_id` → `security_policy`
- `security_policy_perm_attribute.attribute_id` → `security_group_perm_attribute`
- `security_policy_perm_attribute.permission_id` → `add_extension_permissions`
- `security_policy_perm_attribute.policy_id` → `security_policy`
- `security_policy_permissions.permission_id` → `add_extension_permissions`
- `security_policy_permissions.policy_id` → `security_policy`
- `security_user_effectivity.sub_fleet_id` → `sub_fleet_header`
- `security_user_groups.group_id` → `forecast_filter_groups`
- `security_user_notifications.notification_id` → `email_notification`
- `security_user_notifications.user_notification_id` → `security_user_notifications`
- `security_user_perm_attribute.attribute_id` → `security_group_perm_attribute`
- `security_user_perm_attribute.permission_id` → `add_extension_permissions`
- `security_user_permissions.permission_id` → `add_extension_permissions`
- `security_user_permissions_bkp.permission_id` → `add_extension_permissions`
- `security_user_policies.policy_id` → `security_policy`
- `serial_numbers_by_part.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `serial_numbers_by_part.serial_number` → `completion_part_serial`
- `sfdc_activity.activity_id` → `b737ng_activity_import_table`
- `sfdc_activity.booking_id` → `oeim_booking_base_data`
- `sfdc_activity.defect_stage_id` → `defect_stage_employees`
- `sfdc_activity.licence_id` → `email_licence`
- `sfdc_bookings.booking_id` → `oeim_booking_base_data`
- `sfdc_bookings.defect_code` → `defect_extensions`
- `sfdc_bookings.employee_number` → `defect_stage_employees`
- `sfdc_bookings.task_number` → `amp_datmig_comp_task_lookup`
- `sfdc_component_changes.component_change_id` → `sfdc_component_changes`
- `sfdc_component_changes.workcard_number` → `amp_access_panels_by_workcard`
- `sfdc_deleted_bookings.defect_code` → `defect_extensions`
- `sfdc_deleted_bookings.employee_number` → `defect_stage_employees`
- `sfdc_deleted_bookings.sequence_number` → `nrc_high_sequence_control`
- `sfdc_deleted_bookings.task_number` → `amp_datmig_comp_task_lookup`
- `sfdc_open_bookings.defect_code` → `defect_extensions`
- `sfdc_open_bookings.employee_number` → `defect_stage_employees`
- `sfdc_open_bookings.task_number` → `amp_datmig_comp_task_lookup`
- `shelf_li_dt_bkp_2020.batch_number` → `batch_file_header`
- `shelf_li_dt_bkp_2020.component_life_limit_id` → `component_life_limits`
- `shelf_li_dt_bkp_2020.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `shelf_li_dt_bkp_2020.serial_number` → `completion_part_serial`
- `shelf_li_dt_bkp_2020.shelf_life_date_id` → `shelf_life_dates`
- `shelf_life_dates_oases6834.batch_number` → `batch_file_header`
- `shelf_life_dates_oases6834.component_life_limit_id` → `component_life_limits`
- `shelf_life_dates_oases6834.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `shelf_life_dates_oases6834.serial_number` → `completion_part_serial`
- `shelf_life_dates_oases6834.shelf_life_date_id` → `shelf_life_dates`
- `shelf_life_expiry_req_codes.requirement_code` → `nrc_requirements_actions`
- `shipment.company_code` → `company_codes`
- `shipment.currency_code` → `currency_codes`
- `shipment.shipment_id` → `shipment`
- `shipment_documents.document_id` → `aircraft_documents`
- `shipment_documents.document_image_id` → `document_image_source`
- `shipment_documents.shipment_id` → `shipment`
- `shipment_item.batch_number` → `batch_file_header`
- `shipment_item.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `shipment_item.serial_number` → `completion_part_serial`
- `shipment_item.shipment_id` → `shipment`
- `shipment_item.shipment_item_id` → `shipment_item`
- `shipment_item_customs.customs_entry_number` → `batches_by_customs_entry`
- `shipment_item_customs.customs_status_code` → `customs_status_codes`
- `shipment_item_customs.shipment_item_id` → `shipment_item`
- `shipment_item_demands.demand_id` → `demand_reason_to_movement_code`
- `shipment_item_demands.item_id` → `delivery_note_item_header_1`
- `shipment_status.shipment_id` → `shipment`
- `shipment_status.shipment_status_id` → `shipment_status`
- `shipment_status.shipment_status_type_id` → `shipment_status_type`
- `shipment_status_type.status_id` → `amp_revision_status`
- `short_long_serials.long_serial_number` → `long_serial_number_xref`
- `short_long_serials.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `skill_codes.skill_code` → `skill_codes`
- `sold_hours_history.defect_number` → `defect_extensions`
- `stock_audit_batches.batch_number` → `batch_file_header`
- `stock_audit_batches.bin_number` → `bins`
- `stock_audit_batches.stock_audit_id` → `stock_audit_batches`
- `stock_audit_bins.bin_number` → `bins`
- `stock_audit_bins.stock_audit_id` → `stock_audit_batches`
- `stock_audits.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `stock_audits.stock_audit_id` → `stock_audit_batches`
- `stock_by_bin.bin_number` → `bins`
- `stock_by_bin.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `stock_documents.batch_number` → `batch_file_header`
- `stock_documents.document_image_id` → `document_image_source`
- `stock_documents.stock_document_id` → `stock_documents`
- `stock_groups_bkp_oases382.vat_code` → `amp_workcard_activations`
- `stock_works_order_markups.works_order_number` → `credit_works_order_cards`
- `strip_documents.document_image_id` → `document_image_source`
- `strip_documents.strip_document_id` → `strip_documents`
- `strip_documents.strip_report_number` → `strip_report_findings_text`
- `strip_report_findings_text.strip_report_number` → `strip_report_findings_text`
- `strip_report_header_1.currency_code` → `currency_codes`
- `strip_report_header_1.order_number` → `batch_orders`
- `strip_report_header_1.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `strip_report_header_1.serial_number` → `completion_part_serial`
- `strip_report_header_1.strip_report_number` → `strip_report_findings_text`
- `strip_report_header_1.works_order_number` → `credit_works_order_cards`
- `strip_report_header_2.strip_report_number` → `strip_report_findings_text`
- `strip_report_modification_text.strip_report_number` → `strip_report_findings_text`
- `sub_fleet_header.sub_fleet_id` → `sub_fleet_header`
- `sub_fleets.sub_fleet_id` → `sub_fleet_header`
- `sub_fleets_jn.aircraft_code` → `aircraft_assembles`
- `sub_fleets_jn.sub_fleet_id` → `sub_fleet_header`
- `system_header_icarus.key_id` → `osys_key_to_reportid`
- `talend_jobs.talend_job_id` → `talend_jobs`
- `task_activity_link.aircraft_code` → `aircraft_assembles`
- `task_activity_link.package_code` → `amp_package_notes`
- `task_activity_link.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `task_activity_link.serial_number` → `completion_part_serial`
- `task_activity_link.visit_code` → `amp_datmig_fleet_visit_pack`
- `task_activity_link.workcard_number` → `amp_access_panels_by_workcard`
- `taskcard_wo_order_line.order_number` → `batch_orders`
- `tech_log_3.revision_id` → `amp_revision_history`
- `tech_log_defect_text.aircraft_code` → `aircraft_assembles`
- `tech_log_documents.document_image_id` → `document_image_source`
- `tech_log_documents.report_id` → `amp_report_documents`
- `tech_log_rectification_text.aircraft_code` → `aircraft_assembles`
- `tech_log_rectification_text.sequence_number` → `nrc_high_sequence_control`
- `tech_log_workcard_link.aircraft_code` → `aircraft_assembles`
- `tech_log_workcard_link.workcard_number` → `amp_access_panels_by_workcard`
- `temp_rfc_paragraphs.paragraph_id` → `paragraph_cancels`
- `temp_rfc_paragraphs.rfc_id` → `fleet_forecast_plans_rfc`
- `test_table.key_id` → `osys_key_to_reportid`
- `third_party_account_id.account_code` → `access_dim_accounts_info`
- `third_party_account_id.account_id` → `access_dim_accounts_info`
- `tiered_markup_range.markup_code` → `freight_cost_markups`
- `tool_check_out_in_duplicates.batch_number` → `batch_file_header`
- `tool_check_out_in_duplicates.employee_number` → `defect_stage_employees`
- `tool_check_out_in_duplicates.task_number` → `amp_datmig_comp_task_lookup`
- `trades.trade_code` → `trades`
- `training_details.training_id` → `employee_training_details`
- `transaction_header_mavis.key_id` → `osys_key_to_reportid`
- `transaction_header_trex_lasers.key_id` → `osys_key_to_reportid`
- `transaction_log_icarus.account_code` → `access_dim_accounts_info`
- `transaction_log_icarus.batch_number` → `batch_file_header`
- `transaction_log_icarus.bin_number` → `bins`
- `transaction_log_icarus.company_code` → `company_codes`
- `transaction_log_icarus.currency_code` → `currency_codes`
- `transaction_log_icarus.delivery_note_number` → `delivery_note_extended_remarks`
- `transaction_log_icarus.movement_code` → `component_movement_hist_life`
- `transaction_log_icarus.order_number` → `batch_orders`
- `transaction_log_icarus.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `transaction_log_icarus.serial_number` → `completion_part_serial`
- `transaction_log_icarus.vat_code` → `amp_workcard_activations`
- `transaction_log_icarus.warehouse_code` → `account_available_warehouses`
- `transaction_log_icarus.works_order_number` → `credit_works_order_cards`
- `transaction_log_icarus_8134.account_code` → `access_dim_accounts_info`
- `transaction_log_icarus_8134.batch_number` → `batch_file_header`
- `transaction_log_icarus_8134.bin_number` → `bins`
- `transaction_log_icarus_8134.company_code` → `company_codes`
- `transaction_log_icarus_8134.currency_code` → `currency_codes`
- `transaction_log_icarus_8134.delivery_note_number` → `delivery_note_extended_remarks`
- `transaction_log_icarus_8134.movement_code` → `component_movement_hist_life`
- `transaction_log_icarus_8134.order_number` → `batch_orders`
- `transaction_log_icarus_8134.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `transaction_log_icarus_8134.serial_number` → `completion_part_serial`
- `transaction_log_icarus_8134.vat_code` → `amp_workcard_activations`
- `transaction_log_icarus_8134.warehouse_code` → `account_available_warehouses`
- `transaction_log_icarus_8134.works_order_number` → `credit_works_order_cards`
- `transaction_log_lasers.log_number` → `amp_data_migration_log`
- `transaction_log_lasers.user_id` → `dataset_locks_by_user`
- `transaction_log_mavis.log_number` → `amp_data_migration_log`
- `transaction_log_mavis.option_number` → `lmc_base_data_options`
- `transaction_log_trecs.log_number` → `amp_data_migration_log`
- `transaction_log_trecs.user_id` → `dataset_locks_by_user`
- `transaction_types.transaction_type_code` → `transaction_types`
- `uf_forecast_cache.ac_code` → `access_dim_accounts_info`
- `uf_forecast_cache.alert_number` → `alert_colors`
- `uf_forecast_cache.class_code` → `document_classes`
- `uf_forecast_cache.fleet_code` → `amp_datmig_fleet_visit_pack`
- `uf_forecast_cache.interval_id` → `amp_component_intervals`
- `uf_forecast_cache.na_id` → `alternate_parts`
- `uf_forecast_cache.package_code` → `amp_package_notes`
- `uf_forecast_cache.paragraph_id` → `paragraph_cancels`
- `uf_forecast_cache.rfc_id` → `fleet_forecast_plans_rfc`
- `uf_forecast_cache.visit_code` → `amp_datmig_fleet_visit_pack`
- `uf_forecast_cache.workcard_id` → `amp_access_panels_by_workcard`
- `unit_owners.account_code` → `access_dim_accounts_info`
- `unit_owners.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `unit_owners.serial_number` → `completion_part_serial`
- `unknown_part_numbers.sequence_number` → `nrc_high_sequence_control`
- `unknown_part_numbers.unknown_part_number` → `sales_requested_unknown_parts`
- `unmatched_issues_and_returns.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `unmatched_issues_and_returns.requirement_number` → `nrc_requirements_actions`
- `unsatified_service_exchanges.batch_number` → `batch_file_header`
- `unsatified_service_exchanges.order_number` → `batch_orders`
- `unsatified_service_exchanges.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `unsatified_service_exchanges.serial_number` → `completion_part_serial`
- `uom_conversion_at_part_level.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `user_warehouse_access.user_id` → `dataset_locks_by_user`
- `user_warehouse_access.warehouse_code` → `account_available_warehouses`
- `variations.aircraft_code` → `aircraft_assembles`
- `variations.planners_notes_cat_id` → `planners_notes_categories`
- `variations.variation_id` → `forecast_variation_details`
- `variations_xref.aircraft_code` → `aircraft_assembles`
- `variations_xref.package_code` → `amp_package_notes`
- `variations_xref.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `variations_xref.planners_notes_xref_id` → `planners_notes_xref`
- `variations_xref.revision_id` → `amp_revision_history`
- `variations_xref.serial_number` → `completion_part_serial`
- `variations_xref.variation_id` → `forecast_variation_details`
- `variations_xref.visit_code` → `amp_datmig_fleet_visit_pack`
- `variations_xref.workcard_interval_id` → `amp_workcard_intervals`
- `variations_xref_overrides.life_code_level_id` → `life_code_levels`
- `variations_xref_overrides.variation_number` → `forecast_variation_details`
- `vat_codes.export_id` → `export_codes`
- `vat_codes.vat_code` → `amp_workcard_activations`
- `warehouse_distribution.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `warehouse_distribution.warehouse_code` → `account_available_warehouses`
- `warehouse_header_1.warehouse_code` → `account_available_warehouses`
- `warehouse_header_2.airport_id` → `airport_codes`
- `warehouse_header_2.warehouse_code` → `account_available_warehouses`
- `warehouse_lmc_email_address.warehouse_code` → `account_available_warehouses`
- `warehouse_replenishment_data.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `warehouse_replenishment_data.warehouse_code` → `account_available_warehouses`
- `warranty_claims.batch_number` → `batch_file_header`
- `warranty_claims.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `warranty_claims.serial_number` → `completion_part_serial`
- `warranty_claims.user_id` → `dataset_locks_by_user`
- `warranty_claims.warranty_claim_id` → `warranty_claims`
- `warranty_claims.warranty_terms_id` → `warranty_terms`
- `warranty_exclusions.account_code` → `access_dim_accounts_info`
- `warranty_exclusions.exclusion_id` → `aircraft_exclusions`
- `warranty_exclusions.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `warranty_exclusions.serial_number` → `completion_part_serial`
- `warranty_terms.account_code` → `access_dim_accounts_info`
- `warranty_terms.condition_code` → `condition_codes`
- `warranty_terms.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `warranty_terms.serial_number` → `completion_part_serial`
- `warranty_terms.warranty_terms_id` → `warranty_terms`
- `warranty_terms_documents.document_image_id` → `document_image_source`
- `warranty_terms_documents.warranty_terms_id` → `warranty_terms`
- `wcr_boeing_tb_revision.aircraft_code` → `aircraft_assembles`
- `wcr_boeing_tb_revision.revision_id` → `amp_revision_history`
- `wcr_boeing_tb_revision.save_id` → `amp_workcard_saved_reports`
- `wcr_boeing_tb_revision.user_id` → `dataset_locks_by_user`
- `wcr_msg_log.aircraft_code` → `aircraft_assembles`
- `wcr_msg_log.revision_id` → `amp_revision_history`
- `wcr_temp_access_panels.revision_id` → `amp_revision_history`
- `wcr_temp_access_panels.task_number` → `amp_datmig_comp_task_lookup`
- `wcr_temp_access_panels.workcard_number` → `amp_access_panels_by_workcard`
- `wcr_temp_base1.aircraft_code` → `aircraft_assembles`
- `wcr_temp_base1.document_id` → `aircraft_documents`
- `wcr_temp_base1.phase_code` → `rfc_frequency_phase_header`
- `wcr_temp_base1.revision_id` → `amp_revision_history`
- `wcr_temp_base1.trade_code` → `trades`
- `wcr_temp_base1.workcard_id` → `amp_access_panels_by_workcard`
- `wcr_temp_base1.workcard_number` → `amp_access_panels_by_workcard`
- `wcr_temp_base1.zone_code` → `dmg_rpr_measurement_zones`
- `wcr_temp_narratives.revision_id` → `amp_revision_history`
- `wcr_temp_narratives.task_number` → `amp_datmig_comp_task_lookup`
- `wcr_temp_narratives.workcard_number` → `amp_access_panels_by_workcard`
- `weight_and_balance_documents.aircraft_code` → `aircraft_assembles`
- `weight_and_balance_documents.document_id` → `aircraft_documents`
- `weight_and_balance_documents.document_image_id` → `document_image_source`
- `wo_auto_amended_contacts.aircraft_code` → `aircraft_assembles`
- `wo_releases.employee_number` → `defect_stage_employees`
- `work_sch_def_2_lg318.defect_number` → `defect_extensions`
- `work_sch_def_2_lg318.workcard_number` → `amp_access_panels_by_workcard`
- `work_schedule_defect_1.defect_number` → `defect_extensions`
- `work_schedule_defect_1.nrc_number` → `cq_quote_nrc_access_panels`
- `work_schedule_defect_1.workcard_number` → `amp_access_panels_by_workcard`
- `work_schedule_defect_2.defect_number` → `defect_extensions`
- `work_schedule_defect_2.workcard_number` → `amp_access_panels_by_workcard`
- `work_schedule_defect_3.approval_number` → `account_supplier_approvals`
- `work_schedule_defect_3.defect_number` → `defect_extensions`
- `work_schedule_defect_3.employee_number` → `defect_stage_employees`
- `work_schedule_defect_3.flight_number` → `aircraft_flight_hours_1`
- `work_schedule_defect_3.workcard_number` → `amp_access_panels_by_workcard`
- `work_schedule_defect_4.currency_code` → `currency_codes`
- `work_schedule_defect_4.defect_number` → `defect_extensions`
- `work_schedule_defect_4.engineering_support_status_id` → `engineering_support_status`
- `work_schedule_defect_4.workcard_number` → `amp_access_panels_by_workcard`
- `work_schedule_header_2.job_number` → `job_references`
- `work_schedule_header_2.works_order_number` → `credit_works_order_cards`
- `work_schedule_header_3.works_order_sub_status_id` → `works_order_sub_status`
- `work_schedule_ms_codes.account_code` → `access_dim_accounts_info`
- `work_schedule_trades.trade_code` → `trades`
- `work_schedule_workcards.trade_code` → `trades`
- `work_schedule_workcards.workcard_number` → `amp_access_panels_by_workcard`
- `work_schedule_zones.trade_code` → `trades`
- `workcard_accomplishments.workcard_number` → `amp_access_panels_by_workcard`
- `workcard_activations.workcard_activation_id` → `amp_workcard_activations`
- `workcard_activations.workcard_number` → `amp_access_panels_by_workcard`
- `workcard_cancellations.workcard_cancellation_id` → `amp_workcard_cancellations`
- `workcard_cancellations.workcard_number` → `amp_access_panels_by_workcard`
- `workcard_default_status.key_id` → `osys_key_to_reportid`
- `workcard_documents_filter.aircraft_code` → `aircraft_assembles`
- `workcard_documents_filter.filter_id` → `forecast_filter_groups`
- `workcard_form_number.aircraft_code` → `aircraft_assembles`
- `workcard_form_number.form_number_id` → `form_number`
- `workcard_forms.trade_code` → `trades`
- `workcard_forms.workcard_number` → `amp_access_panels_by_workcard`
- `workcard_properties.document_image_id` → `document_image_source`
- `workcard_status_codes.status_code` → `amp_revision_status`
- `workpack_printing_control.oases_report_id` → `oases_reports`
- `works_order_contracts.contract_id` → `customer_contract_rates`
- `works_order_contracts.markup_code` → `freight_cost_markups`
- `works_order_documents.document_image_id` → `document_image_source`
- `works_order_issues_and_returns.bin_number` → `bins`
- `works_order_issues_and_returns.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `works_order_issues_and_returns.requirement_number` → `nrc_requirements_actions`
- `works_order_issues_and_returns.rotable_batch_number` → `rotable_batch_locations`
- `works_order_issues_and_rtn_bac.bin_number` → `bins`
- `works_order_issues_and_rtn_bac.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `works_order_issues_and_rtn_bac.requirement_number` → `nrc_requirements_actions`
- `works_order_issues_and_rtn_bac.rotable_batch_number` → `rotable_batch_locations`
- `works_order_markup_header.markup_code` → `freight_cost_markups`
- `works_order_markup_table.markup_code` → `freight_cost_markups`
- `works_order_sub_status.status_code` → `amp_revision_status`
- `works_order_sub_status.works_order_sub_status_id` → `works_order_sub_status`
- `works_orders.account_code` → `access_dim_accounts_info`
- `works_orders.company_code` → `company_codes`
- `works_orders.licence_id` → `email_licence`
- `works_orders.movement_code` → `component_movement_hist_life`
- `works_orders.order_number` → `batch_orders`
- `works_orders.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `works_orders.serial_number` → `completion_part_serial`
- `works_orders_by_account.account_code` → `access_dim_accounts_info`
- `works_orders_by_account.company_code` → `company_codes`
- `works_orders_by_part_number.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`

### Relationships Removed from Legacy Schema

- `access_dim_accounts_info.ACCOUNT_ID` → `access_dim_accounts_info`
- `access_dim_accounts_info.INFO_ID` → `access_dim_accounts_info`
- `access_dim_accounts_info.INVOICE_NUMBER` → `invoice_categories`
- `access_dim_accounts_info.VAT_CODE` → `amp_workcard_activations`
- `access_dim_sales_info.AUDIT_NUMBER` → `amp_audit_notes`
- `access_dim_sales_info.CUSTOMER_CODE` → `customer_contract_rates`
- `access_dim_sales_info.INFO_ID` → `access_dim_accounts_info`
- `access_dim_sales_info.SALES_ORDER_NUMBER` → `customer_sales_order_xref`
- `access_dim_sales_info.VAT_CODE` → `amp_workcard_activations`
- `accomp_bkup.ACCOMPLISHMENT_ID` → `accomplishment_history`
- `accomp_bkup.AIRCRAFT_CODE` → `aircraft_assembles`
- `accomp_bkup.PACKAGE_CODE` → `amp_package_notes`
- `accomp_bkup.PARAGRAPH_ID` → `paragraph_cancels`
- `accomp_bkup.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `accomp_bkup.REPORT_ID` → `amp_report_documents`
- `accomp_bkup.REVISION_ID` → `amp_revisions`
- `accomp_bkup.RFC_ID` → `fleet_forecast_plans_rfc`
- `accomp_bkup.SERIAL_NUMBER` → `completion_part_serial`
- `accomp_bkup.VISIT_CODE` → `amp_datmig_fleet_visit_pack`
- `accomp_hist_delta_1763.ACCOMPLISHMENT_ID` → `accomplishment_history`
- `accomp_hist_delta_1763.AIRCRAFT_CODE` → `aircraft_assembles`
- `accomp_hist_delta_1763.DAMAGE_ID` → `dmg_rpr_damage`
- `accomp_hist_delta_1763.DOCUMENT_IMAGE_ID` → `document_image_source`
- `accomp_hist_delta_1763.PACKAGE_CODE` → `amp_package_notes`
- `accomp_hist_delta_1763.PARAGRAPH_ID` → `paragraph_cancels`
- `accomp_hist_delta_1763.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `accomp_hist_delta_1763.REPORT_ID` → `amp_report_documents`
- `accomp_hist_delta_1763.REVISION_ID` → `amp_revisions`
- `accomp_hist_delta_1763.RFC_ID` → `fleet_forecast_plans_rfc`
- `accomp_hist_delta_1763.SERIAL_NUMBER` → `completion_part_serial`
- `accomp_hist_delta_1763.VISIT_CODE` → `amp_datmig_fleet_visit_pack`
- `accomp_hist_lost_sched.ACCOMPLISHMENT_ID` → `accomplishment_history`
- `accomp_hist_lost_sched.AIRCRAFT_CODE` → `aircraft_assembles`
- `accomp_hist_lost_sched.PACKAGE_CODE` → `amp_package_notes`
- `accomp_hist_lost_sched.PARAGRAPH_ID` → `paragraph_cancels`
- `accomp_hist_lost_sched.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `accomp_hist_lost_sched.REPORT_ID` → `amp_report_documents`
- `accomp_hist_lost_sched.REVISION_ID` → `amp_revisions`
- `accomp_hist_lost_sched.RFC_ID` → `fleet_forecast_plans_rfc`
- `accomp_hist_lost_sched.SERIAL_NUMBER` → `completion_part_serial`
- `accomp_hist_lost_sched.VISIT_CODE` → `amp_datmig_fleet_visit_pack`
- `accomp_hist_lost_sched_val.ACCOMPLISHMENT_ID` → `accomplishment_history`
- `accomp_hist_lost_sched_val.LIFE_CODE_LEVEL_ID` → `life_code_levels`
- `accomp_values_bkup.ACCOMPLISHMENT_ID` → `accomplishment_history`
- `accomp_values_bkup.LIFE_CODE_LEVEL_ID` → `life_code_levels`
- `accomplishment_history.ACCOMPLISHMENT_ID` → `accomplishment_history`
- `accomplishment_history.AIRCRAFT_CODE` → `aircraft_assembles`
- `accomplishment_history.DAMAGE_ID` → `dmg_rpr_damage`
- `accomplishment_history.DOCUMENT_IMAGE_ID` → `document_image_source`
- `accomplishment_history.PACKAGE_CODE` → `amp_package_notes`
- `accomplishment_history.PARAGRAPH_ID` → `paragraph_cancels`
- `accomplishment_history.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `accomplishment_history.REPORT_ID` → `amp_report_documents`
- `accomplishment_history.REVISION_ID` → `amp_revisions`
- `accomplishment_history.RFC_ID` → `fleet_forecast_plans_rfc`
- `accomplishment_history.SERIAL_NUMBER` → `completion_part_serial`
- `accomplishment_history.VISIT_CODE` → `amp_datmig_fleet_visit_pack`
- `accomplishment_history_values.ACCOMPLISHMENT_ID` → `accomplishment_history`
- `accomplishment_history_values.LIFE_CODE_LEVEL_ID` → `life_code_levels`
- `account_ata_spec_2000_xref.ACCOUNT_CODE` → `access_dim_accounts_info`
- `account_available_warehouses.ACCOUNT_CODE` → `access_dim_accounts_info`
- `account_available_warehouses.WAREHOUSE_CODE` → `account_available_warehouses`
- `account_location_notes.ACCOUNT_CODE` → `access_dim_accounts_info`
- `account_system_header.KEY_ID` → `osys_key_to_reportid`
- `accs_var_corrections_bkp.ACCOMPLISHMENT_ID` → `accomplishment_history`
- `accum_cycles_static_data.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `add_extension_permissions.USER_ID` → `dataset_locks_by_user`
- `aircraft_build_chapters.AIRCRAFT_CODE` → `aircraft_assembles`
- `aircraft_documents.AIRCRAFT_CODE` → `aircraft_assembles`
- `aircraft_documents.AIRCRAFT_DOCUMENT_ID` → `aircraft_documents`
- `aircraft_documents.DOCUMENT_IMAGE_ID` → `document_image_source`
- `aircraft_flight_hours_1.AIRCRAFT_CODE` → `aircraft_assembles`
- `aircraft_flight_hours_2.AIRCRAFT_CODE` → `aircraft_assembles`
- `aircraft_life.AIRCRAFT_CODE` → `aircraft_assembles`
- `aircraft_life.LIFE_CODE_LEVEL_ID` → `life_code_levels`
- `aircraft_life_dbf1065.AIRCRAFT_CODE` → `aircraft_assembles`
- `aircraft_life_dbf1065.LIFE_CODE_LEVEL_ID` → `life_code_levels`
- `aircraft_major_checks.AIRCRAFT_CODE` → `aircraft_assembles`
- `aircraft_major_checks.PACKAGE_CODE` → `amp_package_notes`
- `aircraft_major_checks.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `aircraft_major_checks.SERIAL_NUMBER` → `completion_part_serial`
- `aircraft_major_checks.VISIT_CODE` → `amp_datmig_fleet_visit_pack`
- `aircraft_statistics.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `aircraft_subchapter_statistics.AIRCRAFT_CODE` → `aircraft_assembles`
- `aircraft_weight_7487bkp.AIRCRAFT_CODE` → `aircraft_assembles`
- `aircraft_weight_conf.CONF_ID` → `aircraft_weight_conf`
- `aircraft_weight_conf_entries.CONF_ID` → `aircraft_weight_conf`
- `aircraft_weight_conf_xref.AIRCRAFT_CODE` → `aircraft_assembles`
- `aircraft_weight_conf_xref.CONF_ID` → `aircraft_weight_conf`
- `airway_bill_references.ACCOUNT_CODE` → `access_dim_accounts_info`
- `airway_bill_references.DELIVERY_NOTE_NUMBER` → `delivery_note_extended_remarks`
- `airway_bill_references.ORDER_NUMBER` → `batch_orders`
- `airway_bill_references.SHIPMENT_ID` → `shipment`
- `alternate_parts.ALTERNATE_PART_NUMBER` → `alternate_parts`
- `alternate_parts.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `amp_acc_panel_desc_osd_33348.ACCESS_PANEL_CODE` → `amp_access_panel_desc_hdr`
- `amp_acc_panel_desc_osd_33348.REVISION_ID` → `amp_revisions`
- `amp_access_panel_desc_hdr.revision_id` → `amp_revisions`
- `amp_access_panel_descriptions.revision_id` → `amp_revisions`
- `amp_access_panel_effectivity.ACCESS_PANEL_CODE` → `amp_access_panel_desc_hdr`
- `amp_access_panel_effectivity.AIRCRAFT_CODE` → `aircraft_assembles`
- `amp_access_panel_effectivity.FLEET_CODE` → `amp_datmig_fleet_visit_pack`
- `amp_access_panel_effectivity.REVISION_ID` → `amp_revisions`
- `amp_access_panel_effectivity.SUB_FLEET_ID` → `sub_fleets`
- `amp_access_panel_notes.revision_id` → `amp_revisions`
- `amp_access_panels_by_workcard.revision_id` → `amp_revisions`
- `amp_accesspanel_effectivity_jn.ACCESS_PANEL_CODE` → `amp_access_panel_desc_hdr`
- `amp_accesspanel_effectivity_jn.AIRCRAFT_CODE` → `aircraft_assembles`
- `amp_accesspanel_effectivity_jn.FLEET_CODE` → `amp_datmig_fleet_visit_pack`
- `amp_accesspanel_effectivity_jn.REVISION_ID` → `amp_revisions`
- `amp_accesspanel_effectivity_jn.SUB_FLEET_ID` → `sub_fleets`
- `amp_audit_notes.FLEET_CODE` → `amp_datmig_fleet_visit_pack`
- `amp_audit_notes.PACKAGE_CODE` → `amp_package_notes`
- `amp_audit_notes.REVISION_ID` → `amp_revisions`
- `amp_audit_notes.VISIT_CODE` → `amp_datmig_fleet_visit_pack`
- `amp_audit_notes.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `amp_comments.revision_id` → `amp_revisions`
- `amp_component_intervals.revision_id` → `amp_revisions`
- `amp_component_reset_on_compl.COMPONENT_INTERVAL_ID` → `amp_component_intervals`
- `amp_component_reset_on_compl.COMPONENT_LIFE_LIMIT_ID` → `component_life_limits`
- `amp_data_migration_log.LOG_NUMBER` → `amp_data_migration_log`
- `amp_datmig_accomplishments.AIRCRAFT_CODE` → `aircraft_assembles`
- `amp_datmig_accomplishments.PACKAGE_CODE` → `amp_package_notes`
- `amp_datmig_accomplishments.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `amp_datmig_accomplishments.SERIAL_NUMBER` → `completion_part_serial`
- `amp_datmig_accomplishments.VISIT_CODE` → `amp_datmig_fleet_visit_pack`
- `amp_datmig_comp_task_lookup.PACKAGE_CODE` → `amp_package_notes`
- `amp_datmig_llp.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `amp_datmig_llp.SERIAL_NUMBER` → `completion_part_serial`
- `amp_document_effectivity_bk.AIRCRAFT_CODE` → `aircraft_assembles`
- `amp_document_effectivity_bk.DOCUMENT_ID` → `aircraft_documents`
- `amp_document_effectivity_bk.WORKCARD_ID` → `amp_access_panels_by_workcard`
- `amp_documents_by_workcard.revision_id` → `amp_revisions`
- `amp_documents_by_workcard_bk.DOCUMENT_ID` → `aircraft_documents`
- `amp_documents_by_workcard_bk.REVISION_ID` → `amp_revisions`
- `amp_documents_by_workcard_bk.SEQUENCE_NUMBER` → `nrc_high_sequence_control`
- `amp_documents_by_workcard_bk.WORKCARD_ID` → `amp_access_panels_by_workcard`
- `amp_documents_by_workcard_bk.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `amp_manufacturers_documents.DOCUMENT_ID` → `aircraft_documents`
- `amp_manufacturers_documents.REVISION_ID` → `amp_revisions`
- `amp_material_effectivity.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `amp_material_effectivity.SUB_FLEET_ID` → `sub_fleets`
- `amp_material_effectivity.WORKCARD_ID` → `amp_access_panels_by_workcard`
- `amp_material_effectivity_jn.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `amp_material_effectivity_jn.SUB_FLEET_ID` → `sub_fleets`
- `amp_material_effectivity_jn.WORKCARD_ID` → `amp_access_panels_by_workcard`
- `amp_materials_required_by_wc.revision_id` → `amp_revisions`
- `amp_package_notes.revision_id` → `amp_revisions`
- `amp_packages.revision_id` → `amp_revisions`
- `amp_packages_by_visit.PACKAGE_CODE` → `amp_package_notes`
- `amp_packages_by_visit.REVISION_ID` → `amp_revisions`
- `amp_packages_by_visit.VISIT_CODE` → `amp_datmig_fleet_visit_pack`
- `amp_packages_by_workcard.revision_id` → `amp_revisions`
- `amp_planning_notes.FLEET_CODE` → `amp_datmig_fleet_visit_pack`
- `amp_planning_notes.PACKAGE_CODE` → `amp_package_notes`
- `amp_planning_notes.REVISION_ID` → `amp_revisions`
- `amp_planning_notes.VISIT_CODE` → `amp_datmig_fleet_visit_pack`
- `amp_planning_notes.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `amp_report_documents.DOCUMENT_IMAGE_ID` → `document_image_source`
- `amp_report_documents.REVISION_ID` → `amp_revisions`
- `amp_revision_history.HISTORY_ID` → `accomplishment_history`
- `amp_revision_history.REVISION_ID` → `amp_revisions`
- `amp_revision_history.USER_ID` → `dataset_locks_by_user`
- `amp_revision_status.REVISION_STATUS_ID` → `amp_revision_status`
- `amp_revisions.revision_id` → `amp_revisions`
- `amp_visit_notes.revision_id` → `amp_revisions`
- `amp_visits.revision_id` → `amp_revisions`
- `amp_wc_aircraft_exclusions.revision_id` → `amp_revisions`
- `amp_wc_in_limits_bak.LIFE_CODE_LEVEL_ID` → `life_code_levels`
- `amp_wc_in_limits_bak.WORKCARD_INTERVAL_ID` → `amp_workcard_intervals_limits`
- `amp_wc_in_stages_bak.WORKCARD_INTERVAL_ID` → `amp_workcard_intervals_limits`
- `amp_wcard_extended_desc_41.REVISION_ID` → `amp_revisions`
- `amp_wcard_extended_desc_41.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `amp_workcard_ac_effectivity.AIRCRAFT_CODE` → `aircraft_assembles`
- `amp_workcard_ac_effectivity.SUB_FLEET_ID` → `sub_fleets`
- `amp_workcard_ac_effectivity.WORKCARD_ID` → `amp_access_panels_by_workcard`
- `amp_workcard_ac_effectivity_jn.AIRCRAFT_CODE` → `aircraft_assembles`
- `amp_workcard_ac_effectivity_jn.SUB_FLEET_ID` → `sub_fleets`
- `amp_workcard_ac_effectivity_jn.WORKCARD_ID` → `amp_access_panels_by_workcard`
- `amp_workcard_accomplishments.REVISION_ID` → `amp_revisions`
- `amp_workcard_accomplishments.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `amp_workcard_activations.revision_id` → `amp_revisions`
- `amp_workcard_call_workcard.revision_id` → `amp_revisions`
- `amp_workcard_cancellations.REVISION_ID` → `amp_revisions`
- `amp_workcard_cancellations.WORKCARD_CANCELLATION_ID` → `amp_workcard_cancellations`
- `amp_workcard_cancellations.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `amp_workcard_extended_desc.revision_id` → `amp_revisions`
- `amp_workcard_h3_7487bkp.PHASE_CODE` → `rfc_frequency_phase_header`
- `amp_workcard_h3_7487bkp.REVISION_ID` → `amp_revisions`
- `amp_workcard_header_1.revision_id` → `amp_revisions`
- `amp_workcard_header_1_43216.REVISION_ID` → `amp_revisions`
- `amp_workcard_header_1_43216.WORKCARD_ID` → `amp_access_panels_by_workcard`
- `amp_workcard_header_1_43216.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `amp_workcard_header_2.revision_id` → `amp_revisions`
- `amp_workcard_header_3.revision_id` → `amp_revisions`
- `amp_workcard_header_4.revision_id` → `amp_revisions`
- `amp_workcard_header_5.revision_id` → `amp_revisions`
- `amp_workcard_header_5.revision_number` → `amp_revisions`
- `amp_workcard_header_properties.revision_id` → `amp_revisions`
- `amp_workcard_intervals_limits.workcard_interval_id` → `amp_workcard_intervals_limits`
- `amp_workcard_intervals_stages.workcard_interval_id` → `amp_workcard_intervals_limits`
- `amp_workcard_lcl_applicability.LIFE_CODE_LEVEL_ID` → `life_code_levels`
- `amp_workcard_lcl_applicability.REVISION_ID` → `amp_revisions`
- `amp_workcard_lcl_applicability.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `amp_workcard_narrative.revision_id` → `amp_revisions`
- `amp_workcard_not_with_workcard.revision_id` → `amp_revisions`
- `amp_workcard_previously_acc_by.revision_id` → `amp_revisions`
- `amp_workcard_publications.PUBLICATION_CODE` → `amp_workcard_publications`
- `amp_workcard_publications.PUBLICATION_ID` → `amp_workcard_publications`
- `amp_workcard_publications.WORKCARD_ID` → `amp_access_panels_by_workcard`
- `amp_workcard_saved_reports.SAVED_REPORT_ID` → `amp_workcard_saved_reports`
- `amp_workcard_saved_reports_hdr.SAVED_REPORT_ID` → `amp_workcard_saved_reports`
- `amp_workcards_by_package.revision_id` → `amp_revisions`
- `amp_workcards_by_section.revision_id` → `amp_revisions`
- `assemble_thrust_life_code.AIRCRAFT_CODE` → `aircraft_assembles`
- `assemble_thrust_life_code.FLEET_CODE` → `amp_datmig_fleet_visit_pack`
- `assemble_thrust_life_code.LIFE_CODE` → `aircraft_life`
- `assemble_thrust_life_code.LIFE_CODE_ID` → `assemble_thrust_life_code`
- `assembly_model_header.MODEL_ID` → `assembly_model_header`
- `assembly_model_nodes.MODEL_ID` → `assembly_model_header`
- `assembly_model_nodes.NODE_ID` → `assembly_model_nodes`
- `audit_trail.AUDIT_ID` → `amp_audit_notes`
- `audit_trail.USER_ID` → `dataset_locks_by_user`
- `audit_trail_ids.AUDIT_ID` → `amp_audit_notes`
- `audit_trail_meta_data.AUDIT_ID` → `amp_audit_notes`
- `audit_trail_meta_data.META_ID` → `audit_trail_meta_data`
- `bar_codes.BAR_CODE` → `bar_codes`
- `bar_codes.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `bar_codes.WORKS_ORDER_NUMBER` → `credit_works_order_cards`
- `batch_history.BATCH_NUMBER` → `batch_file_header`
- `batch_history.USER_ID` → `dataset_locks_by_user`
- `batch_notes.BATCH_NUMBER` → `batch_file_header`
- `batch_notes.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `batch_notes.SERIAL_NUMBER` → `completion_part_serial`
- `batch_notes_gu4240.BATCH_NUMBER` → `batch_file_header`
- `batch_notes_gu4240.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `batch_notes_gu4240.SERIAL_NUMBER` → `completion_part_serial`
- `batch_orders.BATCH_NUMBER` → `batch_file_header`
- `batch_orders.ORDER_NUMBER` → `batch_orders`
- `batch_record_1_gu4240.BATCH_NUMBER` → `batch_file_header`
- `batch_record_1_gu4240.CURRENCY_CODE` → `currency_codes`
- `batch_record_1_gu4240.GOODS_RECEIVED_NUMBER` → `goods_received_sheet_document`
- `batch_record_1_gu4240.ORDER_NUMBER` → `batch_orders`
- `batch_record_1_gu4240.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `batch_record_1_gu4240.SERIAL_NUMBER` → `completion_part_serial`
- `batch_record_2.BATCH_NUMBER` → `batch_file_header`
- `batch_record_2.CURRENCY_CODE` → `currency_codes`
- `batch_record_2.CUSTOMS_ENTRY_NUMBER` → `batches_by_customs_entry`
- `batch_record_camo.BATCH_NUMBER` → `batch_file_header`
- `batches_by_airway_bill.AIRWAY_BILL_NUMBER` → `airway_bill_references`
- `batches_by_airway_bill.BATCH_NUMBER` → `batch_file_header`
- `batches_by_customs_entry.BATCH_NUMBER` → `batch_file_header`
- `batches_by_customs_entry.CUSTOMS_ENTRY_NUMBER` → `batches_by_customs_entry`
- `bkp_mobile_permissions.PERMISSION_ID` → `add_extension_permissions`
- `bulk_batch_header.BULK_BATCH_NUMBER` → `bulk_batch_header`
- `cfd_xref_to_tech_log.AIRCRAFT_CODE` → `aircraft_assembles`
- `company_codes.COMPANY_CODE` → `company_codes`
- `company_form_attachments.ATTACHMENT_ID` → `company_form_attachments`
- `company_form_attachments.COMPANY_FORM_ID` → `company_form_attachments`
- `company_form_details.COMPANY_CODE` → `company_codes`
- `company_form_details.COMPANY_FORM_ID` → `company_form_attachments`
- `company_form_details.FORM_NUMBER` → `company_form_attachments`
- `completion_fleet_ata_pos.AIRCRAFT_CODE` → `aircraft_assembles`
- `completion_life_values.AIRCRAFT_CODE` → `aircraft_assembles`
- `completion_life_values.LIFE_CODE_LEVEL_ID` → `life_code_levels`
- `completion_life_values.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `completion_life_values.SERIAL_NUMBER` → `completion_part_serial`
- `completion_maint_mod.AIRCRAFT_CODE` → `aircraft_assembles`
- `completion_maint_mod.REPORT_ID` → `amp_report_documents`
- `completion_part_serial.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `completion_part_serial.SERIAL_NUMBER` → `completion_part_serial`
- `component_mods_history_by_part.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `component_movement_history.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `component_movement_history.SERIAL_NUMBER` → `completion_part_serial`
- `component_movt_hist_ext_8661.AIRCRAFT_CODE` → `aircraft_assembles`
- `component_movt_hist_ext_8661.BATCH_NUMBER` → `batch_file_header`
- `component_movt_hist_ext_8661.COMPONENT_LIFE_LIMIT_ID` → `component_life_limits`
- `component_movt_hist_ext_8661.HISTORY_ID` → `accomplishment_history`
- `component_movt_hist_ext_8661.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `component_movt_hist_ext_8661.REPORT_ID` → `amp_report_documents`
- `component_movt_hist_ext_8661.SERIAL_NUMBER` → `completion_part_serial`
- `components_bkp_dj95.AIRCRAFT_CODE` → `aircraft_assembles`
- `components_bkp_dj95.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `components_bkp_dj95.SERIAL_NUMBER` → `completion_part_serial`
- `components_bkp_dj97.AIRCRAFT_CODE` → `aircraft_assembles`
- `components_bkp_dj97.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `components_bkp_dj97.SERIAL_NUMBER` → `completion_part_serial`
- `components_oases971.AIRCRAFT_CODE` → `aircraft_assembles`
- `components_oases971.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `components_oases971.SERIAL_NUMBER` → `completion_part_serial`
- `condition_pick_table.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `condition_pick_table.PICK_NUMBER` → `condition_pick_table`
- `condition_pick_table.REQUIREMENT_NUMBER` → `nrc_requirements_actions`
- `condition_pick_table.WAREHOUSE_CODE` → `account_available_warehouses`
- `consumable_repair_xref_to_part.BATCH_NUMBER` → `batch_file_header`
- `consumable_repair_xref_to_part.ORDER_NUMBER` → `batch_orders`
- `consumable_repair_xref_to_part.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `contacts_xref.ACCOUNT_CODE` → `access_dim_accounts_info`
- `cq_documents.DOCUMENT_IMAGE_ID` → `document_image_source`
- `cq_documents.QUOTE_ID` → `cq_quote_cards`
- `cq_quote_nrc_access_panels.ACCESS_PANEL_CODE` → `amp_access_panel_desc_hdr`
- `cq_quote_nrc_access_panels.QUOTE_ID` → `cq_quote_cards`
- `cq_quote_nrc_access_panels.QUOTE_NRC_ID` → `cq_quote_nrc_access_panels`
- `cq_quote_status_contacts.STATUS_ID` → `amp_revision_status`
- `crs_signature_text.AIRCRAFT_CODE` → `aircraft_assembles`
- `crs_signature_text.CRS_TEXT_ID` → `crs_text`
- `crs_text.CRS_TEXT_ID` → `crs_text`
- `customer_sales_order_xref.CUSTOMER_SALES_ORDER_NUMBER` → `customer_sales_order_xref`
- `customer_sales_order_xref.SALES_ORDER_NUMBER` → `customer_sales_order_xref`
- `customs_tariff_codes_territory.CUSTOMS_TARIFF_CODE` → `customs_tariff_codes`
- `daily_loans_out.ACCOUNT_CODE` → `access_dim_accounts_info`
- `daily_loans_out.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `daily_loans_out.SERIAL_NUMBER` → `completion_part_serial`
- `dataset_locks_by_lock_type.USER_ID` → `dataset_locks_by_user`
- `dataset_locks_by_user.USER_ID` → `dataset_locks_by_user`
- `defect_extensions.DEFECT_ID` → `defect_extensions`
- `defect_extensions.EXTENSION_ID` → `add_extension_permissions`
- `deferred_defect_xref_to_cfd_no.AIRCRAFT_CODE` → `aircraft_assembles`
- `delivery_note_extended_remarks.DELIVERY_NOTE_NUMBER` → `delivery_note_extended_remarks`
- `delivery_note_header_1.ACCOUNT_CODE` → `access_dim_accounts_info`
- `delivery_note_header_1.COMPANY_CODE` → `company_codes`
- `delivery_note_header_1.DELIVERY_NOTE_NUMBER` → `delivery_note_extended_remarks`
- `delivery_note_header_1.ORDER_NUMBER` → `batch_orders`
- `delivery_note_header_2.DELIVERY_NOTE_NUMBER` → `delivery_note_extended_remarks`
- `delivery_note_header_3.DELIVERY_NOTE_NUMBER` → `delivery_note_extended_remarks`
- `delivery_note_header_4.ACCOUNT_CODE` → `access_dim_accounts_info`
- `delivery_note_header_4.DELIVERY_NOTE_NUMBER` → `delivery_note_extended_remarks`
- `delivery_note_master_list.DELIVERY_NOTE_NUMBER` → `delivery_note_extended_remarks`
- `demand_reason_to_movement_code.MOVEMENT_CODE` → `component_movement_hist_life`
- `demand_reason_to_movement_code.REASON_ID` → `demand_reason_to_movement_code`
- `departments.DEPARTMENT_ID` → `departments`
- `departments.EXPORT_CODE` → `export_codes`
- `dmg_rpr_action_taken_details.ACTION_TAKEN_ID` → `dmg_rpr_action_taken_details`
- `dmg_rpr_attachments.DAMAGE_ID` → `dmg_rpr_damage`
- `dmg_rpr_attachments.DOCUMENT_IMAGE_ID` → `document_image_source`
- `dmg_rpr_ca_approval_details.CA_APPROVAL_ID` → `dmg_rpr_ca_approval_details`
- `dmg_rpr_corrosion_levels.CORROSION_LEVEL_ID` → `dmg_rpr_corrosion_levels`
- `dmg_rpr_damage.DAMAGE_ID` → `dmg_rpr_damage`
- `dmg_rpr_damage.DAMAGE_TYPE_ID` → `dmg_rpr_damage_types`
- `dmg_rpr_damage.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `dmg_rpr_damage.SECTION_ID` → `amp_workcard_sections`
- `dmg_rpr_damage.SERIAL_NUMBER` → `completion_part_serial`
- `dmg_rpr_damage.ZONE_CODE` → `dmg_rpr_measurement_zones`
- `dmg_rpr_damage_numbering.AIRCRAFT_CODE` → `aircraft_assembles`
- `dmg_rpr_damage_numbering.DAMAGE_ID` → `dmg_rpr_damage`
- `dmg_rpr_damage_numbering.DAMAGE_NUMBER` → `dmg_rpr_damage`
- `dmg_rpr_damage_types.DAMAGE_TYPE_ID` → `dmg_rpr_damage_types`
- `dmg_rpr_dmg_2d_position_labels.DAMAGE_ID` → `dmg_rpr_damage`
- `dmg_rpr_dmg_2d_position_labels.LABEL_ID` → `dmg_rpr_dmg_2d_position_labels`
- `dmg_rpr_dmg_2d_positions.DAMAGE_ID` → `dmg_rpr_damage`
- `dmg_rpr_dmg_2d_positions.POSITION_ID` → `dmg_rpr_dmg_2d_position_labels`
- `dmg_rpr_doc_effectivity.AIRCRAFT_CODE` → `aircraft_assembles`
- `dmg_rpr_doc_effectivity.DMG_RPR_DOC_EFFECTIVITY_ID` → `dmg_rpr_doc_effectivity`
- `dmg_rpr_doc_effectivity.FLEET_CODE` → `amp_datmig_fleet_visit_pack`
- `dmg_rpr_doc_effectivity.SUB_FLEET_ID` → `sub_fleets`
- `dmg_rpr_doc_subject.SUBJECT_ID` → `dmg_rpr_doc_subject`
- `dmg_rpr_document_order.AIRCRAFT_CODE` → `aircraft_assembles`
- `dmg_rpr_document_order.FLEET_CODE` → `amp_datmig_fleet_visit_pack`
- `dmg_rpr_document_order.ORDER_NUMBER` → `batch_orders`
- `dmg_rpr_document_order.SUB_FLEET_ID` → `sub_fleets`
- `dmg_rpr_documents.DOCUMENT_IMAGE_ID` → `document_image_source`
- `dmg_rpr_documents.SUBJECT_ID` → `dmg_rpr_doc_subject`
- `dmg_rpr_fitted_locations.AIRCRAFT_CODE` → `aircraft_assembles`
- `dmg_rpr_fitted_locations.DAMAGE_ID` → `dmg_rpr_damage`
- `dmg_rpr_fitted_locations.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `dmg_rpr_fitted_locations.SERIAL_NUMBER` → `completion_part_serial`
- `dmg_rpr_idnt_inspect.INSPECTION_ID` → `dmg_rpr_inspection_type_dtls`
- `dmg_rpr_idnt_inspect_info.INSPECTION_ID` → `dmg_rpr_inspection_type_dtls`
- `dmg_rpr_inspection_type_dtls.INSPECTION_TYPE_ID` → `dmg_rpr_inspection_type_dtls`
- `dmg_rpr_inspections.DAMAGE_ID` → `dmg_rpr_damage`
- `dmg_rpr_inspections.FREQUENCY_ID` → `rfc_frequency_phase_header`
- `dmg_rpr_inspections.INSPECTION_ID` → `dmg_rpr_inspection_type_dtls`
- `dmg_rpr_inspections.INSPECTION_TYPE_ID` → `dmg_rpr_inspection_type_dtls`
- `dmg_rpr_inspections.INTERIM_REPAIR_ID` → `dmg_rpr_interim_repairs`
- `dmg_rpr_inspections.PARAGRAPH_ID` → `paragraph_cancels`
- `dmg_rpr_inspections.RFC_ID` → `fleet_forecast_plans_rfc`
- `dmg_rpr_inspections.TIME_LIMITED_REPAIR_ID` → `dmg_rpr_time_limited_repairs`
- `dmg_rpr_inspections.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `dmg_rpr_interim_repairs.DAMAGE_ID` → `dmg_rpr_damage`
- `dmg_rpr_interim_repairs.FREQUENCY_ID` → `rfc_frequency_phase_header`
- `dmg_rpr_interim_repairs.INTERIM_REPAIR_ID` → `dmg_rpr_interim_repairs`
- `dmg_rpr_interim_repairs.PARAGRAPH_ID` → `paragraph_cancels`
- `dmg_rpr_interim_repairs.RFC_ID` → `fleet_forecast_plans_rfc`
- `dmg_rpr_interim_repairs.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `dmg_rpr_location.AIRCRAFT_CODE` → `aircraft_assembles`
- `dmg_rpr_location.DAMAGE_ID` → `dmg_rpr_damage`
- `dmg_rpr_location.MATERIAL_TYPE_ID` → `dmg_rpr_material_types_dtls`
- `dmg_rpr_location.POSITION_ID` → `dmg_rpr_dmg_2d_position_labels`
- `dmg_rpr_location.SURFACE_FINISH_ID` → `dmg_rpr_surface_finish_details`
- `dmg_rpr_location_measurement.DAMAGE_ID` → `dmg_rpr_damage`
- `dmg_rpr_location_measurement.MEASUREMENT_ID` → `dmg_rpr_location_measurement`
- `dmg_rpr_mat_types_fld_dtls.MATERIAL_TYPE_ID` → `dmg_rpr_material_types_dtls`
- `dmg_rpr_material_types_dtls.MATERIAL_TYPE_ID` → `dmg_rpr_material_types_dtls`
- `dmg_rpr_measurement_sections.MEASUREMENT_ID` → `dmg_rpr_location_measurement`
- `dmg_rpr_measurement_sections.MEASUREMENT_SECTION_ID` → `dmg_rpr_measurement_sections`
- `dmg_rpr_measurement_sections.SECTION_ID` → `amp_workcard_sections`
- `dmg_rpr_measurement_zones.MEASUREMENT_ID` → `dmg_rpr_location_measurement`
- `dmg_rpr_measurement_zones.MEASUREMENT_ZONE_ID` → `dmg_rpr_measurement_zones`
- `dmg_rpr_measurements.MEASUREMENT_ID` → `dmg_rpr_location_measurement`
- `dmg_rpr_permanent_repairs.DAMAGE_ID` → `dmg_rpr_damage`
- `dmg_rpr_permanent_repairs.FREQUENCY_ID` → `rfc_frequency_phase_header`
- `dmg_rpr_permanent_repairs.PARAGRAPH_ID` → `paragraph_cancels`
- `dmg_rpr_permanent_repairs.REPAIR_ID` → `consumable_repair_xref_to_part`
- `dmg_rpr_permanent_repairs.RFC_ID` → `fleet_forecast_plans_rfc`
- `dmg_rpr_permanent_repairs.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `dmg_rpr_repair_req_details.DAMAGE_ID` → `dmg_rpr_damage`
- `dmg_rpr_repair_req_details.REQUIREMENT_NUMBER` → `nrc_requirements_actions`
- `dmg_rpr_section_details.SECTION_ID` → `amp_workcard_sections`
- `dmg_rpr_section_fleet_details.SECTION_ID` → `amp_workcard_sections`
- `dmg_rpr_stage_limits.LIFE_CODE_LEVEL_ID` → `life_code_levels`
- `dmg_rpr_stage_limits.LIMIT_ID` → `amp_component_intervals_limits`
- `dmg_rpr_stage_limits.STAGE_ID` → `amp_component_intervals_stages`
- `dmg_rpr_stages.INSPECTION_ID` → `dmg_rpr_inspection_type_dtls`
- `dmg_rpr_stages.INTERIM_REPAIR_ID` → `dmg_rpr_interim_repairs`
- `dmg_rpr_stages.PERMANENT_REPAIR_ID` → `dmg_rpr_permanent_repairs`
- `dmg_rpr_stages.STAGE_ID` → `amp_component_intervals_stages`
- `dmg_rpr_stages.TIME_LIMITED_REPAIR_ID` → `dmg_rpr_time_limited_repairs`
- `dmg_rpr_subject_sections.SECTION_ID` → `amp_workcard_sections`
- `dmg_rpr_subject_sections.SUBJECT_ID` → `dmg_rpr_doc_subject`
- `dmg_rpr_subject_sections.SUBJECT_SECTION_ID` → `dmg_rpr_subject_sections`
- `dmg_rpr_subject_zones.SUBJECT_ID` → `dmg_rpr_doc_subject`
- `dmg_rpr_subject_zones.SUBJECT_ZONE_ID` → `dmg_rpr_subject_zones`
- `dmg_rpr_surface_finish_details.SURFACE_FINISH_ID` → `dmg_rpr_surface_finish_details`
- `dmg_rpr_time_limited_repairs.DAMAGE_ID` → `dmg_rpr_damage`
- `dmg_rpr_time_limited_repairs.FREQUENCY_ID` → `rfc_frequency_phase_header`
- `dmg_rpr_time_limited_repairs.PARAGRAPH_ID` → `paragraph_cancels`
- `dmg_rpr_time_limited_repairs.RFC_ID` → `fleet_forecast_plans_rfc`
- `dmg_rpr_time_limited_repairs.TIME_LIMITED_REPAIR_ID` → `dmg_rpr_time_limited_repairs`
- `dmg_rpr_time_limited_repairs.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `document_classes.DOCUMENT_ID` → `aircraft_documents`
- `document_image_source.DOCUMENT_IMAGE_SOURCE_ID` → `document_image_source`
- `document_image_types.DOCUMENT_IMAGE_SOURCE_ID` → `document_image_source`
- `document_images_jn.DOCUMENT_IMAGE_ID` → `document_image_source`
- `drn_class_codes.CLASS_CODE` → `document_classes`
- `drn_component_mods_history.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `drn_component_mods_history.REPORT_ID` → `amp_report_documents`
- `drn_component_mods_history.SERIAL_NUMBER` → `completion_part_serial`
- `drn_components_nsbl_history.LIFE_CODE_LEVEL_ID` → `life_code_levels`
- `drn_components_nsbl_history.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `drn_components_nsbl_history.SERIAL_NUMBER` → `completion_part_serial`
- `drn_cycles.AIRCRAFT_CODE` → `aircraft_assembles`
- `drn_cycles.CYCLE_NUMBER` → `accum_cycles_static_data`
- `drn_fleet_ata.AIRCRAFT_CODE` → `aircraft_assembles`
- `drn_fleet_ata.CLASS_CODE` → `document_classes`
- `drn_life_limits.AIRCRAFT_CODE` → `aircraft_assembles`
- `drn_life_limits.LIFE_CODE_LEVEL_ID` → `life_code_levels`
- `drn_life_limits.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `drn_life_limits.SERIAL_NUMBER` → `completion_part_serial`
- `drn_maint_mod.AIRCRAFT_CODE` → `aircraft_assembles`
- `drn_maint_mod.CLASS_CODE` → `document_classes`
- `drn_maint_mod.DRN_CYCLE_NUMBER` → `drn_cycles`
- `drn_maint_mod_notes.AIRCRAFT_CODE` → `aircraft_assembles`
- `drn_maintenance_history.AIRCRAFT_CODE` → `aircraft_assembles`
- `drn_maintenance_history.CLASS_CODE` → `document_classes`
- `drn_maintenance_history.REPORT_ID` → `amp_report_documents`
- `drn_maintenance_history_notes.AIRCRAFT_CODE` → `aircraft_assembles`
- `drn_mod_desc_order_hist.AIRCRAFT_CODE` → `aircraft_assembles`
- `drn_mod_desc_order_hist.CLASS_CODE` → `document_classes`
- `drn_modification_history.AIRCRAFT_CODE` → `aircraft_assembles`
- `drn_modification_history.CLASS_CODE` → `document_classes`
- `drn_modification_history.REPORT_ID` → `amp_report_documents`
- `drn_modification_history_notes.AIRCRAFT_CODE` → `aircraft_assembles`
- `drn_part_serial.CLASS_CODE` → `document_classes`
- `drn_part_serial.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `drn_part_serial.SERIAL_NUMBER` → `completion_part_serial`
- `dummy_part_numbers.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `easa_trace.TRACE_ID` → `easa_trace`
- `email_notification.CATEGORY_ID` → `maint_cost_time_category_set`
- `email_template.TEMPLATE_ID` → `email_template`
- `employee_experience_details.EMPLOYEE_NUMBER` → `defect_stage_employees`
- `employee_experience_details.EXPERIENCE_ID` → `employee_experience_details`
- `employee_presence.EMPLOYEE_NUMBER` → `defect_stage_employees`
- `employee_presence_log.EMPLOYEE_NUMBER` → `defect_stage_employees`
- `employee_presence_log.TASK_NUMBER` → `amp_datmig_comp_task_lookup`
- `employee_training_details.EMPLOYEE_NUMBER` → `defect_stage_employees`
- `employee_training_details.TRAINING_ID` → `employee_training_details`
- `end_use_codes.END_USE_CODE` → `end_use_codes`
- `engineering_support_history.DEFECT_NUMBER` → `defect_extensions`
- `engineering_support_history.ENGINEERING_SUPPORT_HISTORY_ID` → `engineering_support_history`
- `engineering_support_history.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `esign_off_nrc.DOCUMENT_ID` → `aircraft_documents`
- `esign_off_nrc.NRC_NUMBER` → `cq_quote_nrc_access_panels`
- `export_codes.EXPORT_CODE` → `export_codes`
- `export_codes.EXPORT_ID` → `export_codes`
- `extended_part_descriptions.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `extensions.EXTENSION_ID` → `add_extension_permissions`
- `fleet_assembles.FLEET_CODE` → `amp_datmig_fleet_visit_pack`
- `fleet_chap_part_header_1.ALTERNATE_PART_NUMBER` → `alternate_parts`
- `fleet_chap_part_header_1.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `fleet_chap_part_header_2.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `fleet_chap_part_header_3.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `fleet_chapter_part_aircraft.AIRCRAFT_CODE` → `aircraft_assembles`
- `fleet_chapter_part_aircraft.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `fleet_forecast_plans.AIRCRAFT_CODE` → `aircraft_assembles`
- `fleet_forecast_plans.CLASS_CODE` → `document_classes`
- `fleet_forecast_plans.PLAN_ID` → `amp_planning_notes`
- `fleet_forecast_plans.REVISION_ID` → `amp_revisions`
- `fleet_forecast_plans_amp.PACKAGE_CODES` → `amp_packages`
- `fleet_forecast_plans_amp.PLAN_ID` → `amp_planning_notes`
- `fleet_forecast_plans_amp.VISIT_CODES` → `amp_visits`
- `fleet_forecast_plans_amp.WORKCARD_NUMBERS` → `amp_workcards_by_package`
- `fleet_forecast_plans_drn.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `fleet_forecast_plans_drn.PLAN_ID` → `amp_planning_notes`
- `fleet_forecast_plans_drn.SERIAL_NUMBER` → `completion_part_serial`
- `fleet_forecast_plans_rfc.PLAN_ID` → `amp_planning_notes`
- `fleet_forecast_plans_rfc.RFC_ID` → `fleet_forecast_plans_rfc`
- `fleet_statistics.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `float_history.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `float_history.USER_ID` → `dataset_locks_by_user`
- `flown_sectors_bkp.AIRCRAFT_CODE` → `aircraft_assembles`
- `flown_sectors_bkp.FLIGHT_NUMBER` → `aircraft_flight_hours_1`
- `flown_sectors_bkp.REPORT_ID` → `amp_report_documents`
- `flown_sectors_bkp.SECTOR_ID` → `flown_sectors`
- `flown_sectors_con_680.AIRCRAFT_CODE` → `aircraft_assembles`
- `flown_sectors_con_680.FLIGHT_NUMBER` → `aircraft_flight_hours_1`
- `flown_sectors_con_680.REPORT_ID` → `amp_report_documents`
- `flown_sectors_con_680.SECTOR_ID` → `flown_sectors`
- `flown_sectors_delta1817.AIRCRAFT_CODE` → `aircraft_assembles`
- `flown_sectors_delta1817.FLIGHT_NUMBER` → `aircraft_flight_hours_1`
- `flown_sectors_delta1817.REPORT_ID` → `amp_report_documents`
- `flown_sectors_delta1817.SECTOR_ID` → `flown_sectors`
- `forecast_cache.AIRCRAFT_CODE` → `aircraft_assembles`
- `forecast_cache.ALERT_NUMBER` → `alert_colors`
- `forecast_cache.CLASS_CODE` → `document_classes`
- `forecast_cache.COMPONENT_LIFE_LIMIT_ID` → `component_life_limits`
- `forecast_cache.PACKAGE_CODE` → `amp_package_notes`
- `forecast_cache.REVISION_ID` → `amp_revisions`
- `forecast_cache.RFC_ID` → `fleet_forecast_plans_rfc`
- `forecast_cache.VISIT_CODE` → `amp_datmig_fleet_visit_pack`
- `forecast_cache.WORKCARD_CODE` → `amp_access_panels_by_workcard`
- `forecast_cache.WORKCARD_INTERVAL_ID` → `amp_workcard_intervals_limits`
- `forecast_cache.WORKS_ORDER_NUMBER` → `credit_works_order_cards`
- `forecast_cache_ac_details.revision_id` → `amp_revisions`
- `forecast_cache_revisions.revision_id` → `amp_revisions`
- `forecast_filter_groups.GROUP_ID` → `forecast_filter_groups`
- `forecast_filters.FILTER_ID` → `forecast_filter_groups`
- `forecast_filters.GROUP_ID` → `forecast_filter_groups`
- `forecast_parameters.PARAM_ID` → `forecast_parameters`
- `forecast_variation_details.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `form_number.FORM_NUMBER` → `company_form_attachments`
- `form_number.FORM_NUMBER_ID` → `form_number`
- `forward_schedule_summary_vals.LIFE_CODE_LEVEL_ID` → `life_code_levels`
- `freight_cost_markups.FREIGHT_COST_MARKUP_ID` → `freight_cost_markups`
- `freight_costs.FREIGHT_COST_ID` → `freight_cost_markups`
- `freight_costs.ORDER_NUMBER` → `batch_orders`
- `freight_costs.SHIPMENT_ITEM_ID` → `shipment_item`
- `gl_global_codes.GL_ID` → `gl_global_codes`
- `goods_received_sheet_document.BATCH_NUMBER` → `batch_file_header`
- `goods_received_sheet_document.DOCUMENT_IMAGE_ID` → `document_image_source`
- `hazardous_materials.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `ie96_historic.ACCOUNT_CODE` → `access_dim_accounts_info`
- `ie96_historic.BATCH_NUMBER` → `batch_file_header`
- `ie96_historic.BIN_NUMBER` → `bins`
- `ie96_historic.INV_NUMBER` → `invoice_categories`
- `ie96_historic.ORDER_NUMBER` → `batch_orders`
- `ie96_historic.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `ie96_historic.PRICE_TYPE_CODE` → `price_types`
- `ie96_historic.SERIAL_NUMBER` → `completion_part_serial`
- `inherited_acquisition_costs.BATCH_NUMBER` → `batch_file_header`
- `inherited_acquisition_costs.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `inherited_acquisition_costs.SERIAL_NUMBER` → `completion_part_serial`
- `invoice_line_notes.INVOICE_NUMBER` → `invoice_categories`
- `invoice_lines.ACCOUNT_CODE` → `access_dim_accounts_info`
- `invoice_lines.BATCH_NUMBER` → `batch_file_header`
- `invoice_lines.CURRENCY_CODE` → `currency_codes`
- `invoice_lines.GOODS_RECEIVED_NUMBER` → `goods_received_sheet_document`
- `invoice_lines.INVOICE_NUMBER` → `invoice_categories`
- `invoice_lines.ORDER_NUMBER` → `batch_orders`
- `invoice_lines.VAT_CODE` → `amp_workcard_activations`
- `invoice_system_header.KEY_ID` → `osys_key_to_reportid`
- `invoice_trail_entries.BATCH_NUMBER` → `batch_file_header`
- `invoice_trail_entries.CURRENCY_CODE` → `currency_codes`
- `invoice_trail_entries.INVOICE_NUMBER` → `invoice_categories`
- `invoice_trail_entries.INVOICE_TRAIL_ID` → `invoice_trail_entries`
- `invoice_trail_entries.ORDER_NUMBER` → `batch_orders`
- `invoice_trail_entries.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `invoice_trail_entries.SERIAL_NUMBER` → `completion_part_serial`
- `invoices.ACCOUNT_CODE` → `access_dim_accounts_info`
- `invoices.CURRENCY_CODE` → `currency_codes`
- `invoices.INVOICE_NUMBER` → `invoice_categories`
- `jasper_workcard_templates.TEMPLATE_ID` → `email_template`
- `lasers_system_header.KEY_ID` → `osys_key_to_reportid`
- `latest_repair_values.CURRENCY_CODE` → `currency_codes`
- `latest_repair_values.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `latest_repair_values.SERIAL_NUMBER` → `completion_part_serial`
- `ldt.LIFE_CODE_LEVEL_ID` → `life_code_levels`
- `le80_defect_temp.AIRCRAFT_CODE` → `aircraft_assembles`
- `life_code_entry_backup.AIRCRAFT_CODE` → `aircraft_assembles`
- `life_code_entry_backup.LIFE_CODE_LEVEL_ID` → `life_code_levels`
- `life_code_entry_backup.REPORT_ID` → `amp_report_documents`
- `life_code_entry_dbf1065.AIRCRAFT_CODE` → `aircraft_assembles`
- `life_code_entry_dbf1065.LIFE_CODE_LEVEL_ID` → `life_code_levels`
- `life_code_entry_dbf1065.REPORT_ID` → `amp_report_documents`
- `life_code_levels.validation_code` → `awsdms_validation_failures_v1`
- `lmc_base_data_options.AIRCRAFT_CODE` → `aircraft_assembles`
- `lmc_base_data_options.OPT_ID` → `lmc_base_data_options`
- `lmc_base_data_reported_wc.LMC_BASE_DATA_ID` → `lmc_base_data_defs`
- `lmc_base_data_reported_wc.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `maint_accomplishment_costs.ACCOMPLISHMENT_ID` → `accomplishment_history`
- `maint_accomplishment_costs.MAINT_COST_ID` → `maint_cost_budget_adsb`
- `maint_associated_cost_aircraft.AIRCRAFT_CODE` → `aircraft_assembles`
- `maint_associated_cost_aircraft.ASSOCIATED_COST_ID` → `maint_associated_cost_aircraft`
- `maint_associated_cost_aircraft.CATEGORY_ID` → `maint_cost_time_category_set`
- `maint_associated_costs.ASSOCIATED_COST_ID` → `maint_associated_cost_aircraft`
- `maint_associated_costs.CURRENCY_CODE` → `currency_codes`
- `maint_card_pref_cost_cats.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `maint_cost_budget_adsb.AIRCRAFT_CODE` → `aircraft_assembles`
- `maint_cost_budget_adsb.BUDGET_ID` → `maint_cost_budget_adsb`
- `maint_cost_budget_adsb.FREQUENCY_ID` → `rfc_frequency_phase_header`
- `maint_cost_budget_adsb.ITEM_ID` → `delivery_note_item_header_1`
- `maint_cost_budget_adsb.PHASE_NUMBER` → `rfc_frequency_phase_header`
- `maint_cost_budget_adsb.REVISION_ID` → `amp_revisions`
- `maint_cost_budget_adsb.RFC_ID` → `fleet_forecast_plans_rfc`
- `maint_cost_budget_adsb.WORKCARD_ID` → `amp_access_panels_by_workcard`
- `maint_cost_budget_adsb.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `maint_cost_budget_aircraft.AIRCRAFT_CODE` → `aircraft_assembles`
- `maint_cost_budget_aircraft.BUDGET_ID` → `maint_cost_budget_adsb`
- `maint_cost_budget_cfds.AIRCRAFT_CODE` → `aircraft_assembles`
- `maint_cost_budget_cfds.BUDGET_ID` → `maint_cost_budget_adsb`
- `maint_cost_budget_cfds.ITEM_ID` → `delivery_note_item_header_1`
- `maint_cost_budget_costs.BUDGET_COST_ID` → `maint_cost_budget_costs`
- `maint_cost_budget_costs.BUDGET_ID` → `maint_cost_budget_adsb`
- `maint_cost_budget_costs.COST_TYPE_ID` → `maintenance_cost_types`
- `maint_cost_budget_costs.ITEM_ID` → `delivery_note_item_header_1`
- `maint_cost_budget_defects.AIRCRAFT_CODE` → `aircraft_assembles`
- `maint_cost_budget_defects.BUDGET_COST_ID` → `maint_cost_budget_costs`
- `maint_cost_budget_defects.BUDGET_ID` → `maint_cost_budget_adsb`
- `maint_cost_budget_labour_ests.BUDGET_ID` → `maint_cost_budget_adsb`
- `maint_cost_budget_labour_ests.ITEM_ID` → `delivery_note_item_header_1`
- `maint_cost_budget_labour_ests.LABOUR_EST_ID` → `maint_cost_budget_labour_ests`
- `maint_cost_budget_materials.BUDGET_ID` → `maint_cost_budget_adsb`
- `maint_cost_budget_materials.ITEM_ID` → `delivery_note_item_header_1`
- `maint_cost_budget_materials.MATERIAL_ID` → `amp_material_effectivity`
- `maint_cost_budget_materials.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `maint_cost_budget_packages.AIRCRAFT_CODE` → `aircraft_assembles`
- `maint_cost_budget_packages.BUDGET_ID` → `maint_cost_budget_adsb`
- `maint_cost_budget_packages.ITEM_ID` → `delivery_note_item_header_1`
- `maint_cost_budget_packages.PACKAGE_CODE` → `amp_package_notes`
- `maint_cost_budget_packages.REVISION_ID` → `amp_revisions`
- `maint_cost_budget_visits.AIRCRAFT_CODE` → `aircraft_assembles`
- `maint_cost_budget_visits.BUDGET_ID` → `maint_cost_budget_adsb`
- `maint_cost_budget_visits.ITEM_ID` → `delivery_note_item_header_1`
- `maint_cost_budget_visits.REVISION_ID` → `amp_revisions`
- `maint_cost_budget_visits.VISIT_CODE` → `amp_datmig_fleet_visit_pack`
- `maint_cost_budget_workcards.AIRCRAFT_CODE` → `aircraft_assembles`
- `maint_cost_budget_workcards.BUDGET_ID` → `maint_cost_budget_adsb`
- `maint_cost_budget_workcards.COST_CODE` → `cost_codes`
- `maint_cost_budget_workcards.ITEM_ID` → `delivery_note_item_header_1`
- `maint_cost_budget_workcards.PACKAGE_ITEM_ID` → `package_items`
- `maint_cost_budget_workcards.REVISION_ID` → `amp_revisions`
- `maint_cost_budget_workcards.WORKCARD_ID` → `amp_access_panels_by_workcard`
- `maint_cost_budget_workcards.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `maint_cost_hourly_rate_set.CATEGORY_SET_ID` → `maint_cost_time_category_set`
- `maint_cost_hourly_rate_set.HOURLY_RATE_SET_ID` → `maint_cost_hourly_rate_set`
- `maint_cost_hourly_rates.COST_CODE` → `cost_codes`
- `maint_cost_hourly_rates.HOURLY_RATE_SET_ID` → `maint_cost_hourly_rate_set`
- `maint_cost_hourly_rates.TIME_CATEGORY_ID` → `maint_cost_time_category_set`
- `maint_cost_mro_wo_invoices.INVOICE_ID` → `invoice_categories`
- `maint_cost_mro_wo_quotes.QUOTE_ID` → `cq_quote_cards`
- `maint_cost_time_categories.CATEGORY_SET_ID` → `maint_cost_time_category_set`
- `maint_cost_time_categories.CONTRACT_ID` → `customer_contract_rates`
- `maint_cost_time_categories.TIME_CATEGORY_ID` → `maint_cost_time_category_set`
- `maint_cost_time_category_set.CATEGORY_SET_ID` → `maint_cost_time_category_set`
- `maint_hist_associated_costs.COST_TYPE_ID` → `maintenance_cost_types`
- `maint_hist_associated_costs.MAINT_COST_ID` → `maint_cost_budget_adsb`
- `maint_historic_defects.DEFECT_ID` → `defect_extensions`
- `maint_labour_costs.MAINT_COST_ID` → `maint_cost_budget_adsb`
- `maint_material_costs.BATCH_NUMBER` → `batch_file_header`
- `maint_material_costs.MAINT_COST_ID` → `maint_cost_budget_adsb`
- `maint_material_costs.MATERIAL_COST_ID` → `maint_material_costs`
- `maint_material_costs.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `maint_material_costs.SERIAL_NUMBER` → `completion_part_serial`
- `maint_nrc_costs.MAINT_COST_ID` → `maint_cost_budget_adsb`
- `maint_nrc_costs.NRC_NUMBER` → `cq_quote_nrc_access_panels`
- `maint_pack_pref_cost_cats.PACKAGE_CODE` → `amp_package_notes`
- `maint_works_order_costs.MAINT_COST_ID` → `maint_cost_budget_adsb`
- `maintenance_cat_excl_subchap.CATEGORY_ID` → `maint_cost_time_category_set`
- `maintenance_cat_incl_chapter.CATEGORY_ID` → `maint_cost_time_category_set`
- `maintenance_cat_incl_parts.CATEGORY_ID` → `maint_cost_time_category_set`
- `maintenance_cat_incl_parts.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `maintenance_cost_budgets.BUDGET_ID` → `maint_cost_budget_adsb`
- `maintenance_cost_cat_fleet.CATEGORY_ID` → `maint_cost_time_category_set`
- `maintenance_cost_categories.CATEGORY_ID` → `maint_cost_time_category_set`
- `maintenance_cost_entry.COST_ID` → `cost_codes`
- `maintenance_cost_entry.ENTRY_ID` → `batches_by_customs_entry`
- `maintenance_cost_invoices.CURRENCY_CODE` → `currency_codes`
- `maintenance_cost_invoices.INVOICE_ID` → `invoice_categories`
- `maintenance_cost_quotes.ACCOUNT_CODE` → `access_dim_accounts_info`
- `maintenance_cost_quotes.CURRENCY_CODE` → `currency_codes`
- `maintenance_cost_quotes.QUOTE_ID` → `cq_quote_cards`
- `maintenance_cost_types.COST_ID` → `cost_codes`
- `mandatory_parts.COST_CODE` → `cost_codes`
- `manufacturers_work_documents.DOCUMENT_ID` → `aircraft_documents`
- `manufacturers_work_documents.REVISION_ID` → `amp_revisions`
- `marketing_codes.MARKETING_CODE` → `marketing_codes`
- `markups.MARKUP_CODE` → `freight_cost_markups`
- `material_pool_agreement.AGREEMENT_ID` → `material_pool_agreement`
- `material_pool_agreement.CURRENCY_CODE` → `currency_codes`
- `material_pool_agreement_ac.AGREEMENT_ID` → `material_pool_agreement`
- `material_pool_agreement_ac.AIRCRAFT_CODE` → `aircraft_assembles`
- `material_pool_agreement_pn.AGREEMENT_ID` → `material_pool_agreement`
- `material_pool_agreement_pn.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `mavis_system_header.KEY_ID` → `osys_key_to_reportid`
- `maximum_preload_pick_quantity.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `mel_items.revision_id` → `amp_revisions`
- `mel_references.revision_id` → `amp_revisions`
- `mel_revision_history.HISTORY_ID` → `accomplishment_history`
- `mel_revision_history.REVISION_ID` → `amp_revisions`
- `mel_revision_history.USER_ID` → `dataset_locks_by_user`
- `mel_revisions.revision_id` → `amp_revisions`
- `monthly_loans_in.ORDER_NUMBER` → `batch_orders`
- `monthly_loans_in.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `monthly_loans_in.SERIAL_NUMBER` → `completion_part_serial`
- `monthly_loans_out.DELIVERY_NOTE_NUMBER` → `delivery_note_extended_remarks`
- `monthly_loans_out.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `monthly_loans_out.SERIAL_NUMBER` → `completion_part_serial`
- `n_s_extended_part_descriptions.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `netline_import_index.REPORT_ID` → `amp_report_documents`
- `no_narrative_default.AIRCRAFT_CODE` → `aircraft_assembles`
- `non_stock_parts_bkp_oases382.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `non_stock_parts_bkp_oases382.STOCK_CHECK_CODE` → `random_stock_check_bins`
- `nrc_defect_notes.DEFECT_NUMBER` → `defect_extensions`
- `nrc_defect_notes.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `nrc_high_sequence_control.KEY_ID` → `osys_key_to_reportid`
- `nrc_print_history.DEFECT_NUMBER` → `defect_extensions`
- `nrc_print_history.PRINT_HISTORY_ID` → `nrc_print_history`
- `nrc_print_history.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `nrc_properties.NRC_NUMBER` → `cq_quote_nrc_access_panels`
- `nrc_rectification_notes.DEFECT_NUMBER` → `defect_extensions`
- `nrc_rectification_notes.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `nrc_status_history.DEFECT_NUMBER` → `defect_extensions`
- `nrc_status_history.STATUS_CODE` → `amp_revision_status`
- `nrc_status_history.STATUS_HISTORY_ID` → `nrc_status_history`
- `nrc_status_history.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `nrc_workcard_narrative.NRC_NUMBER` → `cq_quote_nrc_access_panels`
- `nrc_xref_to_scheduled_workcard.DEFECT_NUMBER` → `defect_extensions`
- `nrc_xref_to_scheduled_workcard.NRC_NUMBER` → `cq_quote_nrc_access_panels`
- `nrc_xref_to_scheduled_workcard.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `oases_message_log.LOG_NUMBER` → `amp_data_migration_log`
- `oases_reports.REPORT_ID` → `amp_report_documents`
- `oeim_invoice.INVOICE_NUMBER` → `invoice_categories`
- `oeim_invoice_snap_con_rates.COST_CODE` → `cost_codes`
- `oeim_invoice_snap_con_rates.INVOICE_NUMBER` → `invoice_categories`
- `oeim_invoice_snap_con_rates.TIME_CATEGORY_ID` → `maint_cost_time_category_set`
- `oeim_invoice_snap_cost_codes.COST_CODE` → `cost_codes`
- `oeim_invoice_snap_cost_codes.INVOICE_NUMBER` → `invoice_categories`
- `oeim_invoice_snap_currencies.CURRENCY_CODE` → `currency_codes`
- `oeim_invoice_snap_currencies.INVOICE_NUMBER` → `invoice_categories`
- `oeim_invoice_snap_departments.DEPARTMENT_ID` → `departments`
- `oeim_invoice_snap_departments.EXPORT_CODE` → `export_codes`
- `oeim_invoice_snap_departments.INVOICE_NUMBER` → `invoice_categories`
- `oeim_invoice_snap_employees.EMPLOYEE_NUMBER` → `defect_stage_employees`
- `oeim_invoice_snap_employees.INVOICE_NUMBER` → `invoice_categories`
- `oeim_invoice_snap_part_master.INVOICE_NUMBER` → `invoice_categories`
- `oeim_invoice_snap_part_master.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `oeim_invoice_snap_pay_types.INVOICE_NUMBER` → `invoice_categories`
- `oeim_invoice_snap_pay_types.PAYMENT_CODE` → `payment_types`
- `oeim_invoice_snap_pm_bkup.INVOICE_NUMBER` → `invoice_categories`
- `oeim_invoice_snap_pm_bkup.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `oeim_invoice_snap_public_hol.INVOICE_NUMBER` → `invoice_categories`
- `oeim_invoice_snap_serl_master.INVOICE_NUMBER` → `invoice_categories`
- `oeim_invoice_snap_serl_master.LONG_SERIAL_NUMBER` → `long_serial_number_xref`
- `oeim_invoice_snap_serl_master.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `oeim_invoice_snap_serl_master.SERIAL_NUMBER` → `completion_part_serial`
- `oeim_invoice_snap_sfdc_book.BOOKING_ID` → `oeim_booking_base_data`
- `oeim_invoice_snap_sfdc_book.DEFECT_CODE` → `defect_extensions`
- `oeim_invoice_snap_sfdc_book.EMPLOYEE_NUMBER` → `defect_stage_employees`
- `oeim_invoice_snap_sfdc_book.INVOICE_NUMBER` → `invoice_categories`
- `oeim_invoice_snap_sfdc_book.TASK_NUMBER` → `amp_datmig_comp_task_lookup`
- `oeim_invoice_snap_time_crits.INVOICE_NUMBER` → `invoice_categories`
- `oeim_invoice_snap_users.INVOICE_NUMBER` → `invoice_categories`
- `oeim_invoice_snap_users.OASES_ID` → `cfd_categorires_bkpoases405`
- `oeim_invoice_snap_vat_codes.EXPORT_ID` → `export_codes`
- `oeim_invoice_snap_vat_codes.INVOICE_NUMBER` → `invoice_categories`
- `oeim_invoice_snap_vat_codes.VAT_CODE` → `amp_workcard_activations`
- `oeim_invoice_works_orders.ACCOUNT_CODE` → `access_dim_accounts_info`
- `oeim_invoice_works_orders.INVOICE_NUMBER` → `invoice_categories`
- `oeim_quote_dismissed.INVOICE_NUMBER` → `invoice_categories`
- `oeim_quote_dismissed.PACKAGE_CODE` → `amp_package_notes`
- `oeim_quote_dismissed.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `oeim_quote_dismissed.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `oeim_transaction_log_details.DETAIL_NUMBER` → `aircraft_lease_details`
- `oeim_transaction_log_details.LOG_NUMBER` → `amp_data_migration_log`
- `oeim_transaction_log_header.LOG_NUMBER` → `amp_data_migration_log`
- `ord_po_unit_conv_delta1827.ORDER_NUMBER` → `batch_orders`
- `order_change_history.HISTORY_ID` → `accomplishment_history`
- `order_change_history.ORDER_NUMBER` → `batch_orders`
- `order_change_history.PREORDER_ID` → `preorder_line_requirement_xref`
- `order_customs_info.ORDER_NUMBER` → `batch_orders`
- `order_delivery_note_remarks.ORDER_NUMBER` → `batch_orders`
- `order_email_chasing.ORDER_NUMBER` → `batch_orders`
- `order_goods_received_invoices.CURRENCY_CODE` → `currency_codes`
- `order_goods_received_invoices.INVOICE_NUMBER` → `invoice_categories`
- `order_goods_received_invoices.ORDER_NUMBER` → `batch_orders`
- `order_goods_received_invoices.VAT_CODE` → `amp_workcard_activations`
- `order_header_2.ORDER_NUMBER` → `batch_orders`
- `order_header_2.WORKS_ORDER_NUMBER` → `credit_works_order_cards`
- `order_header_3.DELIVERY_NOTE_NUMBER` → `delivery_note_extended_remarks`
- `order_header_3.ORDER_NUMBER` → `batch_orders`
- `order_header_4.EMPLOYEE_NUMBER` → `defect_stage_employees`
- `order_header_4.ORDER_NUMBER` → `batch_orders`
- `order_history.BATCH_NUMBER` → `batch_file_header`
- `order_history.CONDITION_CODE` → `condition_codes`
- `order_history.CURRENCY_CODE` → `currency_codes`
- `order_history.INVOICE_NUMBER` → `invoice_categories`
- `order_history.ORDER_NUMBER` → `batch_orders`
- `order_history.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `order_history.SERIAL_NUMBER` → `completion_part_serial`
- `order_line_additional_info.AIRWAY_BILL_NUMBER` → `airway_bill_references`
- `order_line_additional_info.CONDITION_CODE` → `condition_codes`
- `order_line_additional_info.ORDER_NUMBER` → `batch_orders`
- `order_line_additional_info.RELEASE_CODE` → `release_codes`
- `order_line_additional_info_2.ORDER_NUMBER` → `batch_orders`
- `order_line_notes.ORDER_NUMBER` → `batch_orders`
- `order_line_quotes_data.CURRENCY_CODE` → `currency_codes`
- `order_line_quotes_data.ORDER_NUMBER` → `batch_orders`
- `order_line_quotes_data.VAT_CODE` → `amp_workcard_activations`
- `order_line_requirement_xref.ORDER_NUMBER` → `batch_orders`
- `order_line_requirement_xref.REQUIREMENT_NUMBER` → `nrc_requirements_actions`
- `order_line_weight_dimension.DIMENSION_ID` → `order_line_weight_dimension`
- `order_line_weight_dimension.ORDER_NUMBER` → `batch_orders`
- `order_numbers_by_supplier.ACCOUNT_CODE` → `access_dim_accounts_info`
- `order_numbers_by_supplier.ORDER_NUMBER` → `batch_orders`
- `order_print_date.ORDER_NUMBER` → `batch_orders`
- `order_purchase_unit_conversion.ORDER_NUMBER` → `batch_orders`
- `order_standard_text_blocks.BLOCK_NUMBER` → `block_countries`
- `order_supplier_approval.ORDER_NUMBER` → `batch_orders`
- `order_supplier_approval.SUPPLIER_APPROVAL_NUMBER` → `account_supplier_approvals`
- `order_text.ORDER_NUMBER` → `batch_orders`
- `order_workshop_works_orders.ORDER_NUMBER` → `batch_orders`
- `orders_by_due_date.ORDER_NUMBER` → `batch_orders`
- `orders_to_part_number_xref.ORDER_NUMBER` → `batch_orders`
- `orders_to_part_number_xref.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `ordr_goods_bkp.GOODS_RECEIVED_NUMBER` → `goods_received_sheet_document`
- `ordr_goods_bkp.ORDER_NUMBER` → `batch_orders`
- `ordr_goods_bkp.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `osys_defect_act_to_defect_id.DEFECT_ID` → `defect_extensions`
- `osys_defect_to_defect_id.DEFECT_ID` → `defect_extensions`
- `osys_defect_to_defect_id.DEFECT_NUMBER` → `defect_extensions`
- `osys_defect_to_tech_log_line.DEFECT_NUMBER` → `defect_extensions`
- `osys_key_to_reportid.REPORT_ID` → `amp_report_documents`
- `outstation_codes.OUTSTATION_CODE` → `outstation_codes`
- `package.PACKAGE_ID` → `amp_package_notes`
- `package.SHIPMENT_ID` → `shipment`
- `package_items.ITEM_ID` → `delivery_note_item_header_1`
- `package_items.PACKAGE_ID` → `amp_package_notes`
- `package_items.PACKAGE_ITEMS_ID` → `package_items`
- `paragraph_cancels.PARAGRAPH_ID` → `paragraph_cancels`
- `paragraph_cancels.RFC_ID` → `fleet_forecast_plans_rfc`
- `part_applicability_codes.APPLICABILITY_CODE` → `amp_workcard_lcl_applicability`
- `part_change_warning_chapters.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_change_warnings.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_customs_tariff_territory.CUSTOMS_TARIFF_CODE` → `customs_tariff_codes`
- `part_customs_tariff_territory.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_master_bkp_oases382.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_master_bkp_oases382.STOCK_CHECK_CODE` → `random_stock_check_bins`
- `part_number_amendment_history.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_number_amendment_history.USER_ID` → `dataset_locks_by_user`
- `part_number_chapters.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_number_chapters_dj-82.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_number_essentiality_codes.ESSENTIALITY_CODE` → `part_number_essentiality_codes`
- `part_number_essentiality_codes.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_number_marketing_codes.MARKETING_CODE` → `marketing_codes`
- `part_number_marketing_codes.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_number_order_retention.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_number_shelf_life_details.COMPONENT_LIFE_LIMIT_ID` → `component_life_limits`
- `part_number_shelf_life_details.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_number_technical_notes.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_number_vat_codes.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_number_vat_codes.VAT_CODE` → `amp_workcard_activations`
- `part_serial_documents.DOCUMENT_IMAGE_ID` → `document_image_source`
- `part_serial_documents.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_serial_documents.PART_SERIAL_DOCUMENT_ID` → `part_serial_documents`
- `part_serial_documents.SERIAL_NUMBER` → `completion_part_serial`
- `part_serial_master_list.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_xref_to_pick_history.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `part_xref_to_pick_history.PICK_NUMBER` → `condition_pick_table`
- `part_xref_to_pick_history.REQUIREMENT_NUMBER` → `nrc_requirements_actions`
- `parts_customs_tariff_codes.CUSTOMS_TARIFF_CODE` → `customs_tariff_codes`
- `parts_customs_tariff_codes.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `parts_freight_tiered_markups.FREIGHT_COST_MARKUP_ID` → `freight_cost_markups`
- `parts_received_without_cost.ORDER_NUMBER` → `batch_orders`
- `parts_received_without_cost.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `parts_requiring_export_licence.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `pick_hist_7890_bkp.ALTERNATE_PART_NUMBER` → `alternate_parts`
- `pick_hist_7890_bkp.BATCH_NUMBER` → `batch_file_header`
- `pick_hist_7890_bkp.ORDER_NUMBER` → `batch_orders`
- `pick_hist_7890_bkp.PICK_NUMBER` → `condition_pick_table`
- `pick_hist_7890_bkp.REQUIREMENT_NUMBER` → `nrc_requirements_actions`
- `pick_hist_7890_bkp.SERIAL_NUMBER` → `completion_part_serial`
- `pick_history.ALTERNATE_PART_NUMBER` → `alternate_parts`
- `pick_history.BATCH_NUMBER` → `batch_file_header`
- `pick_history.ORDER_NUMBER` → `batch_orders`
- `pick_history.PICK_NUMBER` → `condition_pick_table`
- `pick_history.REQUIREMENT_NUMBER` → `nrc_requirements_actions`
- `pick_history.SERIAL_NUMBER` → `completion_part_serial`
- `pirep_index_data.AIRCRAFT_CODE` → `aircraft_assembles`
- `planners_notes.CATEGORY_ID` → `maint_cost_time_category_set`
- `planners_notes.NOTES_XREF_ID` → `planners_notes_xref`
- `planners_notes.STATUS_ID` → `amp_revision_status`
- `planners_notes_statuses.STATUS_ID` → `amp_revision_status`
- `planners_notes_xref.AIRCRAFT_CODE` → `aircraft_assembles`
- `planners_notes_xref.ALERT_NUMBER` → `alert_colors`
- `planners_notes_xref.PACKAGE_CODE` → `amp_package_notes`
- `planners_notes_xref.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `planners_notes_xref.REVISION_ID` → `amp_revisions`
- `planners_notes_xref.RFC_ID` → `fleet_forecast_plans_rfc`
- `planners_notes_xref.SERIAL_NUMBER` → `completion_part_serial`
- `planners_notes_xref.VISIT_CODE` → `amp_datmig_fleet_visit_pack`
- `planners_notes_xref.WORKCARD_INTERVAL_ID` → `amp_workcard_intervals_limits`
- `preorder_line_requirement_xref.PREORDER_ID` → `preorder_line_requirement_xref`
- `preorder_line_requirement_xref.REQUIREMENT_NUMBER` → `nrc_requirements_actions`
- `preorder_line_stock_info.BATCH_NUMBER` → `batch_file_header`
- `preorder_line_stock_info.BIN_NUMBER` → `bins`
- `preorder_line_stock_info.MOVEMENT_CODE` → `component_movement_hist_life`
- `preorder_line_stock_info.PREORDER_ID` → `preorder_line_requirement_xref`
- `preorder_line_stock_info.SERIAL_NUMBER` → `completion_part_serial`
- `preorder_lines.CONDITION_CODE` → `condition_codes`
- `preorder_lines.NON_STOCK_PART_NUMBER` → `non_stock_parts`
- `preorder_lines.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `preorder_lines.PREORDER_ID` → `preorder_line_requirement_xref`
- `preorder_lines.RELEASE_CODE` → `release_codes`
- `preorder_lines.VAT_CODE` → `amp_workcard_activations`
- `preorders.ACCOUNT_CODE` → `access_dim_accounts_info`
- `preorders.COMPANY_CODE` → `company_codes`
- `preorders.CURRENCY_CODE` → `currency_codes`
- `preorders.EMPLOYEE_NUMBER` → `defect_stage_employees`
- `preorders.PREORDER_ID` → `preorder_line_requirement_xref`
- `price_codes.PRICE_CODE` → `price_codes`
- `purchase_demand_by_part.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `quote_email_chasing.ORDER_NUMBER` → `batch_orders`
- `quotes_by_part.ACCOUNT_CODE` → `access_dim_accounts_info`
- `quotes_by_part.CURRENCY_CODE` → `currency_codes`
- `quotes_by_part.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `quotes_for_part_by_account.ACCOUNT_CODE` → `access_dim_accounts_info`
- `quotes_for_part_by_account.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `random_stock_check_bins.BIN_NUMBER` → `bins`
- `random_stock_check_bins.WAREHOUSE_CODE` → `account_available_warehouses`
- `random_stock_check_date.WAREHOUSE_CODE` → `account_available_warehouses`
- `random_stock_check_log.WAREHOUSE_CODE` → `account_available_warehouses`
- `random_stock_check_parts.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `random_stock_check_parts.WAREHOUSE_CODE` → `account_available_warehouses`
- `rd_xref_to_tech_logs.AIRCRAFT_CODE` → `aircraft_assembles`
- `rd_xref_to_tech_logs.ALERT_NUMBER` → `alert_colors`
- `rd_xref_to_tech_logs.KEY_ID` → `osys_key_to_reportid`
- `rd_xref_to_tech_logs.STATUS_CODE` → `amp_revision_status`
- `rdi_history.ALERT_NUMBER` → `alert_colors`
- `rdi_history.USER_ID` → `dataset_locks_by_user`
- `rdi_to_nrc.NRC_NUMBER` → `cq_quote_nrc_access_panels`
- `rdi_to_nrc.RDI_NUMBER` → `rdi_history`
- `release_codes.RELEASE_CODE` → `release_codes`
- `reliability_report_logo_desc.DOCUMENT_IMAGE_ID` → `document_image_source`
- `reliability_report_logo_desc.LOGO_DESC_ID` → `reliability_report_logo_desc`
- `repair_approval_data.ACCOUNT_CODE` → `access_dim_accounts_info`
- `repair_approval_data.BATCH_NUMBER` → `batch_file_header`
- `repair_approval_data.MOVEMENT_CODE` → `component_movement_hist_life`
- `repetitive_defect_header_1.AIRCRAFT_CODE` → `aircraft_assembles`
- `repetitive_defect_header_1.ALERT_NUMBER` → `alert_colors`
- `repetitive_defect_header_2.ALERT_NUMBER` → `alert_colors`
- `repetitive_defect_narrative.ALERT_NUMBER` → `alert_colors`
- `repetitive_defect_narrative.USER_ID` → `dataset_locks_by_user`
- `repetitive_defect_tech_logs.ALERT_NUMBER` → `alert_colors`
- `repetitive_defect_tech_logs.SEQUENCE_NUMBER` → `nrc_high_sequence_control`
- `req_priority_desc_oases_1228.PRIORITY_ID` → `req_priority_desc_oases_1228`
- `requests_for_quotes.RFQ_NUMBER` → `requirement_to_rfq_xref`
- `requests_for_quotes_lines.MOVEMENT_CODE` → `component_movement_hist_life`
- `requests_for_quotes_lines.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `requests_for_quotes_lines.RELEASE_CODE` → `release_codes`
- `requests_for_quotes_lines.RFQ_NUMBER` → `requirement_to_rfq_xref`
- `requests_for_quotes_notes.RFQ_NUMBER` → `requirement_to_rfq_xref`
- `requirement_planners_notes.REQUIREMENT_NUMBER` → `nrc_requirements_actions`
- `requirement_priority_desc.PRIORITY_ID` → `req_priority_desc_oases_1228`
- `requirement_priority_leadtimes.PRIORITY_CODE` → `req_priority_desc_oases_1228`
- `requirement_priority_sla.ACCOUNT_CODE` → `access_dim_accounts_info`
- `requirement_priority_sla.PRIORITY_CODE` → `req_priority_desc_oases_1228`
- `requirement_recharge_details.BATCH_NUMBER` → `batch_file_header`
- `requirement_recharge_details.COST_CODE` → `cost_codes`
- `requirement_recharge_details.CURRENCY_CODE` → `currency_codes`
- `requirement_recharge_details.REQUIREMENT_NUMBER` → `nrc_requirements_actions`
- `requirement_recharge_details.STRIP_REPORT_NUMBER` → `strip_report_findings_text`
- `requirement_source_codes.SOURCE_CODE` → `document_image_source`
- `rfc_documents.DOCUMENT_IMAGE_ID` → `document_image_source`
- `rfc_documents.RFC_DOCUMENT_ID` → `rfc_documents`
- `rfc_documents.RFC_ID` → `fleet_forecast_plans_rfc`
- `rfc_download_effectivity.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `rfc_download_effectivity.TAXONOMY_ID` → `rfc_download_taxonomy`
- `rfc_download_origin_codes.ACCOMPLISHMENT_CODE` → `accomplishment_history`
- `rfc_download_origin_codes.AUTHORITY_CODE` → `rfc_regulating_authority`
- `rfc_download_origin_codes.CHANGE_ORIGIN_CODE` → `rfc_change_origin`
- `rfc_download_taxonomy.AUTHORITY_CODE` → `rfc_regulating_authority`
- `rfc_download_taxonomy.TAXONOMY_ID` → `rfc_download_taxonomy`
- `rfc_evaluation_history.EVALUATION_HISTORY_ID` → `rfc_evaluation_history`
- `rfc_evaluation_history.RFC_ID` → `fleet_forecast_plans_rfc`
- `rfc_header_publications.PUBLICATION_CODE` → `amp_workcard_publications`
- `rfc_header_publications.RFC_ID` → `fleet_forecast_plans_rfc`
- `rfc_print_history_log.LOG_ID` → `amp_data_migration_log`
- `rfc_print_history_log.RFC_ID` → `fleet_forecast_plans_rfc`
- `rfc_publications.PUBLICATION_CODE` → `amp_workcard_publications`
- `rfc_statement_sections.SECTION_CODE` → `amp_workcard_sections`
- `rfc_statement_sections.SECTION_ID` → `amp_workcard_sections`
- `rfc_transaction_log.LOG_ID` → `amp_data_migration_log`
- `rfc_transaction_log.RFC_ID` → `fleet_forecast_plans_rfc`
- `rfq_by_part_number.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `rfq_by_part_number.RFQ_NUMBER` → `requirement_to_rfq_xref`
- `rfq_quote_received.ACCOUNT_CODE` → `access_dim_accounts_info`
- `rfq_quote_received.CURRENCY_CODE` → `currency_codes`
- `rfq_quote_received.RFQ_NUMBER` → `requirement_to_rfq_xref`
- `rfq_requirement_xref.REQUIREMENT_NUMBER` → `nrc_requirements_actions`
- `rfq_requirement_xref.RFQ_NUMBER` → `requirement_to_rfq_xref`
- `rfq_supplier_notes.ACCOUNT_CODE` → `access_dim_accounts_info`
- `rfq_supplier_notes.RFQ_NUMBER` → `requirement_to_rfq_xref`
- `rotable_float_values.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `rotables_below_re_order.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `rp_base_plan_header.BASE_PLAN_ID` → `rp_base_plan_header`
- `rp_block_resource.BLOCK_ID` → `block_countries`
- `rp_block_resource.SCOPE_TYPE_ID` → `scope_type_rating`
- `rp_block_resource.SHIFT_ID` → `rp_basic_shift`
- `rp_block_resource.WAREHOUSE_CODE` → `account_available_warehouses`
- `rp_block_resource_days.BLOCK_ID` → `block_countries`
- `rp_block_resource_days.DAY_ID` → `public_holidays`
- `rp_block_resource_days.DAY_NUMBER` → `public_holidays`
- `rp_dependencies.MILESTONE_ID` → `rp_milestone_history`
- `rp_dependencies.REVISION_ID` → `amp_revisions`
- `rp_dependencies.TYPE_ID` → `aircraft_types`
- `rp_dependencies.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `rp_employee_allocation.ALLOCATION_HEADER_ID` → `rp_employee_allocation_header`
- `rp_employee_allocation.ALLOCATION_ID` → `order_requirement_allocation`
- `rp_employee_allocation.NRC_NUMBER` → `cq_quote_nrc_access_panels`
- `rp_employee_allocation.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `rp_employee_allocation_header.ALLOCATION_HEADER_ID` → `rp_employee_allocation_header`
- `rp_employee_allocation_header.BASIC_SHIFT_ID` → `rp_basic_shift`
- `rp_employee_allocation_header.EMPLOYEE_NUMBER` → `defect_stage_employees`
- `rp_milestone_history.HISTORY_ID` → `accomplishment_history`
- `rp_milestone_history.MILESTONE_ID` → `rp_milestone_history`
- `rp_milestones.MILESTONE_CODE` → `rp_milestone_history`
- `rp_milestones.MILESTONE_ID` → `rp_milestone_history`
- `rp_weekends.WEEKENDS_ID` → `rp_weekends`
- `rp_wo_base_estimated_defects.BASE_PLAN_ID` → `rp_base_plan_header`
- `rp_wo_base_estimated_defects.BASIC_SHIFT_ID` → `rp_basic_shift`
- `rp_wo_base_milestones.BASE_PLAN_ID` → `rp_base_plan_header`
- `rp_wo_base_milestones.MILESTONE_ID` → `rp_milestone_history`
- `rp_wo_base_nrc_plan.BASE_PLAN_ID` → `rp_base_plan_header`
- `rp_wo_base_nrc_plan.BASIC_SHIFT_ID` → `rp_basic_shift`
- `rp_wo_base_nrc_plan.NRC_NUMBER` → `cq_quote_nrc_access_panels`
- `rp_wo_base_workcard_plan.BASE_PLAN_ID` → `rp_base_plan_header`
- `rp_wo_base_workcard_plan.BASIC_SHIFT_ID` → `rp_basic_shift`
- `rp_wo_base_workcard_plan.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `rp_wo_milestones.MILESTONE_ID` → `rp_milestone_history`
- `sabre_flight_map.REPORT_ID` → `amp_report_documents`
- `sabre_trace.TRACE_ID` → `easa_trace`
- `sage_order_line_details.ORDER_NUMBER` → `batch_orders`
- `sales_invoice_genled_xref.END_USE_CODE` → `end_use_codes`
- `sales_invoices_xref.INVOICE_NUMBER` → `invoice_categories`
- `sales_invoices_xref.SALES_ORDER_NUMBER` → `customer_sales_order_xref`
- `sales_order_history.SALES_REQUEST_NUMBER` → `sales_request_quote_detail`
- `sales_order_notes.SALES_ORDER_NUMBER` → `customer_sales_order_xref`
- `sales_order_parameters.KEY_ID` → `osys_key_to_reportid`
- `sales_order_payments.SALES_ORDER_DISPATCH_NUMBER` → `sales_order_dispatches`
- `sales_order_payments.SALES_ORDER_NUMBER` → `customer_sales_order_xref`
- `sales_order_payments.USER_ID` → `dataset_locks_by_user`
- `sales_orders.ACCOUNT_CODE` → `access_dim_accounts_info`
- `sales_orders.COMPANY_CODE` → `company_codes`
- `sales_orders.CURRENCY_CODE` → `currency_codes`
- `sales_orders.SALES_ORDER_NUMBER` → `customer_sales_order_xref`
- `sales_orders_by_part.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `sales_orders_by_part.SALES_ORDER_NUMBER` → `customer_sales_order_xref`
- `sales_quotes_out_history.ACCOUNT_CODE` → `access_dim_accounts_info`
- `sales_quotes_out_history.CONDITION_CODE` → `condition_codes`
- `sales_quotes_out_history.CURRENCY_CODE` → `currency_codes`
- `sales_quotes_out_history.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `sales_quotes_out_history.SALES_REQUEST_NUMBER` → `sales_request_quote_detail`
- `sales_request_quote_header.ACCOUNT_CODE` → `access_dim_accounts_info`
- `sales_request_quote_header.COMPANY_CODE` → `company_codes`
- `sales_request_quote_header.CURRENCY_CODE` → `currency_codes`
- `sales_request_quote_header.SALES_REQUEST_NUMBER` → `sales_request_quote_detail`
- `sales_request_quote_header.USER_ID` → `dataset_locks_by_user`
- `sales_request_quote_notes.SALES_REQUEST_NUMBER` → `sales_request_quote_detail`
- `sales_requested_unknown_parts.SALES_REQUEST_NUMBER` → `sales_request_quote_detail`
- `sales_requests_by_part.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `sales_requests_by_part.SALES_REQUEST_NUMBER` → `sales_request_quote_detail`
- `sales_requests_by_unknown_part.SALES_REQUEST_NUMBER` → `sales_request_quote_detail`
- `sales_requests_by_unknown_part.UNKNOWN_PART_NUMBER` → `sales_requested_unknown_parts`
- `sample_fleets_jn.AIRCRAFT_CODE` → `aircraft_assembles`
- `sample_fleets_jn.FLEET_CODE` → `amp_datmig_fleet_visit_pack`
- `sap_order_header.ORDER_NUMBER` → `batch_orders`
- `sap_order_header.PREORDER_ID` → `preorder_line_requirement_xref`
- `sap_order_line.ORDER_NUMBER` → `batch_orders`
- `sap_order_line.PREORDER_ID` → `preorder_line_requirement_xref`
- `schedule_forecast_xref.AIRCRAFT_CODE` → `aircraft_assembles`
- `schedule_forecast_xref.PACKAGE_CODE` → `amp_package_notes`
- `schedule_forecast_xref.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `schedule_forecast_xref.RFC_ID` → `fleet_forecast_plans_rfc`
- `schedule_forecast_xref.SERIAL_NUMBER` → `completion_part_serial`
- `schedule_forecast_xref.VISIT_CODE` → `amp_datmig_fleet_visit_pack`
- `schedule_forecast_xref.WORKCARD_ID` → `amp_access_panels_by_workcard`
- `schedule_forecast_xref.WORKCARD_INTERVAL_ID` → `amp_workcard_intervals_limits`
- `schedule_forecast_xref.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `schedule_source.AIRCRAFT_CODE` → `aircraft_assembles`
- `schedule_source.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `schedule_source.RFC_ID` → `fleet_forecast_plans_rfc`
- `schedule_source.SERIAL_NUMBER` → `completion_part_serial`
- `security_audit_log_header.AUDIT_LOG_ID` → `security_audit_log_header`
- `security_audit_log_header.PERMISSION_ID` → `add_extension_permissions`
- `security_audit_log_meta_data.AUDIT_LOG_ID` → `security_audit_log_header`
- `security_audit_log_meta_data.SEQUENCE_NUMBER` → `nrc_high_sequence_control`
- `security_group_perm_attribute.ATTRIBUTE_ID` → `security_group_perm_attribute`
- `security_group_perm_attribute.GROUP_ID` → `forecast_filter_groups`
- `security_group_perm_attribute.PERMISSION_ID` → `add_extension_permissions`
- `security_group_permissions.GROUP_ID` → `forecast_filter_groups`
- `security_group_permissions.PERMISSION_ID` → `add_extension_permissions`
- `security_group_policies.GROUP_ID` → `forecast_filter_groups`
- `security_group_policies.POLICY_ID` → `security_policy`
- `security_groups.GROUP_ID` → `forecast_filter_groups`
- `security_permission_def_attrib.ATTRIBUTE_ID` → `security_group_perm_attribute`
- `security_permission_def_attrib.PERMISSION_ID` → `add_extension_permissions`
- `security_policy.POLICY_ID` → `security_policy`
- `security_policy_perm_attribute.ATTRIBUTE_ID` → `security_group_perm_attribute`
- `security_policy_perm_attribute.PERMISSION_ID` → `add_extension_permissions`
- `security_policy_perm_attribute.POLICY_ID` → `security_policy`
- `security_policy_permissions.PERMISSION_ID` → `add_extension_permissions`
- `security_policy_permissions.POLICY_ID` → `security_policy`
- `security_user_effectivity.sub_fleet_id` → `sub_fleets`
- `security_user_groups.GROUP_ID` → `forecast_filter_groups`
- `security_user_notifications.NOTIFICATION_ID` → `email_notification`
- `security_user_notifications.USER_NOTIFICATION_ID` → `security_user_notifications`
- `security_user_perm_attribute.ATTRIBUTE_ID` → `security_group_perm_attribute`
- `security_user_perm_attribute.PERMISSION_ID` → `add_extension_permissions`
- `security_user_permissions.PERMISSION_ID` → `add_extension_permissions`
- `security_user_permissions_bkp.PERMISSION_ID` → `add_extension_permissions`
- `security_user_policies.POLICY_ID` → `security_policy`
- `serial_numbers_by_part.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `serial_numbers_by_part.SERIAL_NUMBER` → `completion_part_serial`
- `sfdc_activity.ACTIVITY_ID` → `b737ng_activity_import_table`
- `sfdc_activity.BOOKING_ID` → `oeim_booking_base_data`
- `sfdc_activity.DEFECT_STAGE_ID` → `defect_stage_employees`
- `sfdc_activity.LICENCE_ID` → `email_licence`
- `sfdc_bookings.BOOKING_ID` → `oeim_booking_base_data`
- `sfdc_bookings.DEFECT_CODE` → `defect_extensions`
- `sfdc_bookings.EMPLOYEE_NUMBER` → `defect_stage_employees`
- `sfdc_bookings.TASK_NUMBER` → `amp_datmig_comp_task_lookup`
- `sfdc_component_changes.COMPONENT_CHANGE_ID` → `sfdc_component_changes`
- `sfdc_component_changes.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `sfdc_deleted_bookings.DEFECT_CODE` → `defect_extensions`
- `sfdc_deleted_bookings.EMPLOYEE_NUMBER` → `defect_stage_employees`
- `sfdc_deleted_bookings.SEQUENCE_NUMBER` → `nrc_high_sequence_control`
- `sfdc_deleted_bookings.TASK_NUMBER` → `amp_datmig_comp_task_lookup`
- `sfdc_open_bookings.DEFECT_CODE` → `defect_extensions`
- `sfdc_open_bookings.EMPLOYEE_NUMBER` → `defect_stage_employees`
- `sfdc_open_bookings.TASK_NUMBER` → `amp_datmig_comp_task_lookup`
- `shelf_li_dt_bkp_2020.BATCH_NUMBER` → `batch_file_header`
- `shelf_li_dt_bkp_2020.COMPONENT_LIFE_LIMIT_ID` → `component_life_limits`
- `shelf_li_dt_bkp_2020.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `shelf_li_dt_bkp_2020.SERIAL_NUMBER` → `completion_part_serial`
- `shelf_li_dt_bkp_2020.SHELF_LIFE_DATE_ID` → `shelf_life_dates`
- `shelf_life_dates_oases6834.BATCH_NUMBER` → `batch_file_header`
- `shelf_life_dates_oases6834.COMPONENT_LIFE_LIMIT_ID` → `component_life_limits`
- `shelf_life_dates_oases6834.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `shelf_life_dates_oases6834.SERIAL_NUMBER` → `completion_part_serial`
- `shelf_life_dates_oases6834.SHELF_LIFE_DATE_ID` → `shelf_life_dates`
- `shelf_life_expiry_req_codes.REQUIREMENT_CODE` → `nrc_requirements_actions`
- `shipment.COMPANY_CODE` → `company_codes`
- `shipment.CURRENCY_CODE` → `currency_codes`
- `shipment.SHIPMENT_ID` → `shipment`
- `shipment_documents.DOCUMENT_ID` → `aircraft_documents`
- `shipment_documents.DOCUMENT_IMAGE_ID` → `document_image_source`
- `shipment_documents.SHIPMENT_ID` → `shipment`
- `shipment_item.BATCH_NUMBER` → `batch_file_header`
- `shipment_item.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `shipment_item.SERIAL_NUMBER` → `completion_part_serial`
- `shipment_item.SHIPMENT_ID` → `shipment`
- `shipment_item.SHIPMENT_ITEM_ID` → `shipment_item`
- `shipment_item_customs.CUSTOMS_ENTRY_NUMBER` → `batches_by_customs_entry`
- `shipment_item_customs.CUSTOMS_STATUS_CODE` → `customs_status_codes`
- `shipment_item_customs.SHIPMENT_ITEM_ID` → `shipment_item`
- `shipment_item_demands.DEMAND_ID` → `demand_reason_to_movement_code`
- `shipment_item_demands.ITEM_ID` → `delivery_note_item_header_1`
- `shipment_status.SHIPMENT_ID` → `shipment`
- `shipment_status.SHIPMENT_STATUS_ID` → `shipment_status`
- `shipment_status.SHIPMENT_STATUS_TYPE_ID` → `shipment_status_type`
- `shipment_status_type.STATUS_ID` → `amp_revision_status`
- `short_long_serials.LONG_SERIAL_NUMBER` → `long_serial_number_xref`
- `short_long_serials.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `skill_codes.SKILL_CODE` → `skill_codes`
- `sold_hours_history.DEFECT_NUMBER` → `defect_extensions`
- `stock_audit_batches.BATCH_NUMBER` → `batch_file_header`
- `stock_audit_batches.BIN_NUMBER` → `bins`
- `stock_audit_batches.STOCK_AUDIT_ID` → `stock_audit_batches`
- `stock_audit_bins.BIN_NUMBER` → `bins`
- `stock_audit_bins.STOCK_AUDIT_ID` → `stock_audit_batches`
- `stock_audits.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `stock_audits.STOCK_AUDIT_ID` → `stock_audit_batches`
- `stock_by_bin.BIN_NUMBER` → `bins`
- `stock_by_bin.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `stock_documents.BATCH_NUMBER` → `batch_file_header`
- `stock_documents.DOCUMENT_IMAGE_ID` → `document_image_source`
- `stock_documents.STOCK_DOCUMENT_ID` → `stock_documents`
- `stock_groups_bkp_oases382.VAT_CODE` → `amp_workcard_activations`
- `stock_works_order_markups.WORKS_ORDER_NUMBER` → `credit_works_order_cards`
- `strip_documents.DOCUMENT_IMAGE_ID` → `document_image_source`
- `strip_documents.STRIP_DOCUMENT_ID` → `strip_documents`
- `strip_documents.STRIP_REPORT_NUMBER` → `strip_report_findings_text`
- `strip_report_findings_text.STRIP_REPORT_NUMBER` → `strip_report_findings_text`
- `strip_report_header_1.CURRENCY_CODE` → `currency_codes`
- `strip_report_header_1.ORDER_NUMBER` → `batch_orders`
- `strip_report_header_1.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `strip_report_header_1.SERIAL_NUMBER` → `completion_part_serial`
- `strip_report_header_1.STRIP_REPORT_NUMBER` → `strip_report_findings_text`
- `strip_report_header_1.WORKS_ORDER_NUMBER` → `credit_works_order_cards`
- `strip_report_header_2.STRIP_REPORT_NUMBER` → `strip_report_findings_text`
- `strip_report_modification_text.STRIP_REPORT_NUMBER` → `strip_report_findings_text`
- `sub_fleet_header.sub_fleet_id` → `sub_fleets`
- `sub_fleets.sub_fleet_id` → `sub_fleets`
- `sub_fleets_jn.AIRCRAFT_CODE` → `aircraft_assembles`
- `sub_fleets_jn.SUB_FLEET_ID` → `sub_fleets`
- `system_header_icarus.KEY_ID` → `osys_key_to_reportid`
- `talend_jobs.TALEND_JOB_ID` → `talend_jobs`
- `task_activity_link.AIRCRAFT_CODE` → `aircraft_assembles`
- `task_activity_link.PACKAGE_CODE` → `amp_package_notes`
- `task_activity_link.PART_NUMBER` → `PART_NUMBER_CHAPTERS_DJ-82`
- `task_activity_link.SERIAL_NUMBER` → `completion_part_serial`
- `task_activity_link.VISIT_CODE` → `amp_datmig_fleet_visit_pack`
- `task_activity_link.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `taskcard_wo_order_line.ORDER_NUMBER` → `batch_orders`
- `tech_log_3.revision_id` → `amp_revisions`
- `tech_log_defect_text.AIRCRAFT_CODE` → `aircraft_assembles`
- `tech_log_documents.DOCUMENT_IMAGE_ID` → `document_image_source`
- `tech_log_documents.REPORT_ID` → `amp_report_documents`
- `tech_log_rectification_text.AIRCRAFT_CODE` → `aircraft_assembles`
- `tech_log_rectification_text.SEQUENCE_NUMBER` → `nrc_high_sequence_control`
- `tech_log_workcard_link.AIRCRAFT_CODE` → `aircraft_assembles`
- `tech_log_workcard_link.WORKCARD_NUMBER` → `amp_access_panels_by_workcard`
- `temp_rfc_paragraphs.PARAGRAPH_ID` → `paragraph_cancels`
- `temp_rfc_paragraphs.RFC_ID` → `fleet_forecast_plans_rfc`
- `test_table.KEY_ID` → `osys_key_to_reportid`
- `third_party_account_id.ACCOUNT_CODE` → `access_dim_accounts_info`
- `third_party_account_id.ACCOUNT_ID` → `access_dim_accounts_info`
- `tiered_markup_range.MARKUP_CODE` → `freight_cost_markups`
- `units_of_measure.aircraft_code` → `aircraft_assembles`
- `units_of_measure.component_life_limit_id` → `component_life_limits`
- `units_of_measure.part_number` → `PART_NUMBER_CHAPTERS_DJ-82`
- `units_of_measure.serial_number` → `completion_part_serial`
- `units_of_measure.sub_fleet_id` → `sub_fleets`
- `units_of_measure.workcard_id` → `amp_access_panels_by_workcard`

---
