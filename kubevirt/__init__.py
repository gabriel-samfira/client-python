# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.intstr_int_or_string import IntstrIntOrString
from .models.resource_quantity import ResourceQuantity
from .models.runtime_raw_extension import RuntimeRawExtension
from .models.v1_api_group import V1APIGroup
from .models.v1_api_group_list import V1APIGroupList
from .models.v1_api_resource import V1APIResource
from .models.v1_api_resource_list import V1APIResourceList
from .models.v1_affinity import V1Affinity
from .models.v1_bios import V1BIOS
from .models.v1_bootloader import V1Bootloader
from .models.v1_cd_rom_target import V1CDRomTarget
from .models.v1_cpu import V1CPU
from .models.v1_cpu_feature import V1CPUFeature
from .models.v1_chassis import V1Chassis
from .models.v1_clock import V1Clock
from .models.v1_clock_offset_utc import V1ClockOffsetUTC
from .models.v1_cloud_init_config_drive_source import V1CloudInitConfigDriveSource
from .models.v1_cloud_init_no_cloud_source import V1CloudInitNoCloudSource
from .models.v1_config_map_volume_source import V1ConfigMapVolumeSource
from .models.v1_container_disk_source import V1ContainerDiskSource
from .models.v1_dhcp_options import V1DHCPOptions
from .models.v1_dhcp_private_options import V1DHCPPrivateOptions
from .models.v1_data_volume_source import V1DataVolumeSource
from .models.v1_delete_options import V1DeleteOptions
from .models.v1_devices import V1Devices
from .models.v1_disk import V1Disk
from .models.v1_disk_target import V1DiskTarget
from .models.v1_domain_spec import V1DomainSpec
from .models.v1_efi import V1EFI
from .models.v1_empty_disk_source import V1EmptyDiskSource
from .models.v1_ephemeral_volume_source import V1EphemeralVolumeSource
from .models.v1_feature_apic import V1FeatureAPIC
from .models.v1_feature_hyperv import V1FeatureHyperv
from .models.v1_feature_spinlocks import V1FeatureSpinlocks
from .models.v1_feature_state import V1FeatureState
from .models.v1_feature_vendor_id import V1FeatureVendorID
from .models.v1_features import V1Features
from .models.v1_fields_v1 import V1FieldsV1
from .models.v1_firmware import V1Firmware
from .models.v1_floppy_target import V1FloppyTarget
from .models.v1_gpu import V1GPU
from .models.v1_group_version_for_discovery import V1GroupVersionForDiscovery
from .models.v1_hpet_timer import V1HPETTimer
from .models.v1_http_get_action import V1HTTPGetAction
from .models.v1_http_header import V1HTTPHeader
from .models.v1_host_disk import V1HostDisk
from .models.v1_hugepages import V1Hugepages
from .models.v1_hyperv_timer import V1HypervTimer
from .models.v1_i6300_esb_watchdog import V1I6300ESBWatchdog
from .models.v1_input import V1Input
from .models.v1_interface import V1Interface
from .models.v1_interface_bridge import V1InterfaceBridge
from .models.v1_interface_masquerade import V1InterfaceMasquerade
from .models.v1_interface_sriov import V1InterfaceSRIOV
from .models.v1_interface_slirp import V1InterfaceSlirp
from .models.v1_kvm_timer import V1KVMTimer
from .models.v1_label_selector import V1LabelSelector
from .models.v1_label_selector_requirement import V1LabelSelectorRequirement
from .models.v1_list_meta import V1ListMeta
from .models.v1_local_object_reference import V1LocalObjectReference
from .models.v1_lun_target import V1LunTarget
from .models.v1_machine import V1Machine
from .models.v1_managed_fields_entry import V1ManagedFieldsEntry
from .models.v1_memory import V1Memory
from .models.v1_multus_network import V1MultusNetwork
from .models.v1_network import V1Network
from .models.v1_node_affinity import V1NodeAffinity
from .models.v1_node_selector import V1NodeSelector
from .models.v1_node_selector_requirement import V1NodeSelectorRequirement
from .models.v1_node_selector_term import V1NodeSelectorTerm
from .models.v1_object_meta import V1ObjectMeta
from .models.v1_owner_reference import V1OwnerReference
from .models.v1_pit_timer import V1PITTimer
from .models.v1_patch import V1Patch
from .models.v1_persistent_volume_claim_spec import V1PersistentVolumeClaimSpec
from .models.v1_persistent_volume_claim_volume_source import V1PersistentVolumeClaimVolumeSource
from .models.v1_pod_affinity import V1PodAffinity
from .models.v1_pod_affinity_term import V1PodAffinityTerm
from .models.v1_pod_anti_affinity import V1PodAntiAffinity
from .models.v1_pod_dns_config import V1PodDNSConfig
from .models.v1_pod_dns_config_option import V1PodDNSConfigOption
from .models.v1_pod_network import V1PodNetwork
from .models.v1_port import V1Port
from .models.v1_preconditions import V1Preconditions
from .models.v1_preferred_scheduling_term import V1PreferredSchedulingTerm
from .models.v1_probe import V1Probe
from .models.v1_rtc_timer import V1RTCTimer
from .models.v1_resource_requirements import V1ResourceRequirements
from .models.v1_restart_options import V1RestartOptions
from .models.v1_rng import V1Rng
from .models.v1_root_paths import V1RootPaths
from .models.v1_secret_volume_source import V1SecretVolumeSource
from .models.v1_server_address_by_client_cidr import V1ServerAddressByClientCIDR
from .models.v1_service_account_volume_source import V1ServiceAccountVolumeSource
from .models.v1_status import V1Status
from .models.v1_status_cause import V1StatusCause
from .models.v1_status_details import V1StatusDetails
from .models.v1_tcp_socket_action import V1TCPSocketAction
from .models.v1_time import V1Time
from .models.v1_timer import V1Timer
from .models.v1_toleration import V1Toleration
from .models.v1_typed_local_object_reference import V1TypedLocalObjectReference
from .models.v1_virtual_machine import V1VirtualMachine
from .models.v1_virtual_machine_condition import V1VirtualMachineCondition
from .models.v1_virtual_machine_instance import V1VirtualMachineInstance
from .models.v1_virtual_machine_instance_condition import V1VirtualMachineInstanceCondition
from .models.v1_virtual_machine_instance_file_system import V1VirtualMachineInstanceFileSystem
from .models.v1_virtual_machine_instance_file_system_info import V1VirtualMachineInstanceFileSystemInfo
from .models.v1_virtual_machine_instance_file_system_list import V1VirtualMachineInstanceFileSystemList
from .models.v1_virtual_machine_instance_guest_agent_info import V1VirtualMachineInstanceGuestAgentInfo
from .models.v1_virtual_machine_instance_guest_os_info import V1VirtualMachineInstanceGuestOSInfo
from .models.v1_virtual_machine_instance_guest_os_user import V1VirtualMachineInstanceGuestOSUser
from .models.v1_virtual_machine_instance_guest_os_user_list import V1VirtualMachineInstanceGuestOSUserList
from .models.v1_virtual_machine_instance_list import V1VirtualMachineInstanceList
from .models.v1_virtual_machine_instance_migration import V1VirtualMachineInstanceMigration
from .models.v1_virtual_machine_instance_migration_condition import V1VirtualMachineInstanceMigrationCondition
from .models.v1_virtual_machine_instance_migration_list import V1VirtualMachineInstanceMigrationList
from .models.v1_virtual_machine_instance_migration_spec import V1VirtualMachineInstanceMigrationSpec
from .models.v1_virtual_machine_instance_migration_state import V1VirtualMachineInstanceMigrationState
from .models.v1_virtual_machine_instance_migration_status import V1VirtualMachineInstanceMigrationStatus
from .models.v1_virtual_machine_instance_network_interface import V1VirtualMachineInstanceNetworkInterface
from .models.v1_virtual_machine_instance_preset import V1VirtualMachineInstancePreset
from .models.v1_virtual_machine_instance_preset_list import V1VirtualMachineInstancePresetList
from .models.v1_virtual_machine_instance_preset_spec import V1VirtualMachineInstancePresetSpec
from .models.v1_virtual_machine_instance_replica_set import V1VirtualMachineInstanceReplicaSet
from .models.v1_virtual_machine_instance_replica_set_condition import V1VirtualMachineInstanceReplicaSetCondition
from .models.v1_virtual_machine_instance_replica_set_list import V1VirtualMachineInstanceReplicaSetList
from .models.v1_virtual_machine_instance_replica_set_spec import V1VirtualMachineInstanceReplicaSetSpec
from .models.v1_virtual_machine_instance_replica_set_status import V1VirtualMachineInstanceReplicaSetStatus
from .models.v1_virtual_machine_instance_spec import V1VirtualMachineInstanceSpec
from .models.v1_virtual_machine_instance_status import V1VirtualMachineInstanceStatus
from .models.v1_virtual_machine_instance_template_spec import V1VirtualMachineInstanceTemplateSpec
from .models.v1_virtual_machine_list import V1VirtualMachineList
from .models.v1_virtual_machine_spec import V1VirtualMachineSpec
from .models.v1_virtual_machine_state_change_request import V1VirtualMachineStateChangeRequest
from .models.v1_virtual_machine_status import V1VirtualMachineStatus
from .models.v1_volume import V1Volume
from .models.v1_watch_event import V1WatchEvent
from .models.v1_watchdog import V1Watchdog
from .models.v1_weighted_pod_affinity_term import V1WeightedPodAffinityTerm
from .models.v1alpha1_data_volume import V1alpha1DataVolume
from .models.v1alpha1_data_volume_blank_image import V1alpha1DataVolumeBlankImage
from .models.v1alpha1_data_volume_source import V1alpha1DataVolumeSource
from .models.v1alpha1_data_volume_source_http import V1alpha1DataVolumeSourceHTTP
from .models.v1alpha1_data_volume_source_pvc import V1alpha1DataVolumeSourcePVC
from .models.v1alpha1_data_volume_source_registry import V1alpha1DataVolumeSourceRegistry
from .models.v1alpha1_data_volume_source_s3 import V1alpha1DataVolumeSourceS3
from .models.v1alpha1_data_volume_source_upload import V1alpha1DataVolumeSourceUpload
from .models.v1alpha1_data_volume_spec import V1alpha1DataVolumeSpec
from .models.v1alpha1_data_volume_status import V1alpha1DataVolumeStatus

# import apis into sdk package
from .apis.default_api import DefaultApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
from .models.v1_interface_bridge import V1InterfaceBridge
from .models.v1_interface_slirp import V1InterfaceSlirp
