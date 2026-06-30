# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-466688-VLESS-WS-78MS` (url=228ms, nekobox=284ms, status=yes)
2. `AKUN-002-466688-VLESS-WS-75MS` (url=199ms, nekobox=230ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS` (url=212ms, nekobox=283ms, status=yes)
4. `AKUN-004-466688-VLESS-WS-77MS` (url=232ms, nekobox=298ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-80MS` (url=233ms, nekobox=248ms, status=yes)
6. `AKUN-006-COMPREND-NET-VLESS-WS-77MS` (url=228ms, nekobox=242ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-80MS` (url=213ms, nekobox=266ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-87MS` (url=212ms, nekobox=253ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-76MS` (url=224ms, nekobox=233ms, status=yes)
10. `AKUN-010-COMPREND-NET-VLESS-WS-88MS` (url=231ms, nekobox=362ms, status=yes)
11. `AKUN-011-NL-BRAINOZA-20250311-VLESS-WS-100MS` (url=210ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-87MS` (url=240ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-89MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-AEZA-NETWORK-VLESS-WS-91MS` (url=204ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-78MS` (url=238ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-128MS` (url=223ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-78MS` (url=258ms, status=HTTP 204)
18. `AKUN-018-ZOOM-VLESS-WS-111MS` (url=223ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-97MS` (url=240ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-178MS` (url=327ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-361MS` (url=731ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-363MS` (url=748ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-393MS` (url=892ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-403MS` (url=889ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-426MS` (url=862ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
