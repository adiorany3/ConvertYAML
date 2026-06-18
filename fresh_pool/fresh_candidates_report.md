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
1. `AKUN-001-CLOUDWEBMANAGE-EU-FR-VLESS-WS-70MS` (url=243ms, nekobox=264ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-93MS`
3. `AKUN-003-CLOUDFLARE-VLESS-WS-104MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-89MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-89MS` (url=268ms, nekobox=263ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-101MS`
7. `AKUN-008-UNKNOWN-VLESS-WS-94MS` (url=248ms, nekobox=195ms, status=no)
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-86MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-92MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-82MS`
11. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-125MS`
12. `AKUN-013-US-VLESS-WS-108MS` (url=249ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-129MS` (url=252ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-104MS` (url=250ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-164MS` (url=240ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-101MS` (url=262ms, status=HTTP 204)
17. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-293MS` (url=609ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-269MS` (url=548ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-304MS` (url=3496ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-297MS` (url=593ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-303MS` (url=627ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-85MS` (url=250ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-86MS` (url=287ms, status=HTTP 204)
24. `AKUN-032-FDCSERVERS-FRANKFURT2-VLESS-WS-537MS` (url=900ms, status=HTTP 204)
25. `AKUN-034-CLOUDFLARE-VLESS-WS-781MS` (url=1320ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
