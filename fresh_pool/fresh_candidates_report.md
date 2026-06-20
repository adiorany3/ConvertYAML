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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-72MS` (url=239ms, nekobox=7172ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-73MS`
3. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-64MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-75MS` (url=250ms, nekobox=183ms, status=no)
5. `AKUN-003-UNKNOWN-VLESS-WS-84MS`
6. `AKUN-004-CLOUDFLARE-VLESS-WS-84MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-85MS`
8. `AKUN-006-UNKNOWN-VLESS-WS-76MS`
9. `AKUN-009-UNKNOWN-VLESS-WS-83MS` (url=265ms, nekobox=191ms, status=no)
10. `AKUN-007-U1HOST-FRA-VLESS-WS-73MS`
11. `AKUN-008-HOSTOFF-NET-VLESS-WS-76MS`
12. `AKUN-009-NET-NL-VLESS-WS-70MS`
13. `AKUN-010-CLOUDFLARE-VLESS-WS-90MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-91MS` (url=243ms, status=HTTP 204)
15. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-78MS` (url=244ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-75MS` (url=253ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-76MS` (url=245ms, status=HTTP 204)
18. `AKUN-018-CLOUDWEBMANAGE-EU-FR-VLESS-WS-96MS` (url=266ms, status=HTTP 204)
19. `AKUN-019-1PASSWORD-VLESS-WS-65MS` (url=239ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-82MS` (url=279ms, status=HTTP 204)
21. `AKUN-021-MEDIUM-VLESS-WS-89MS` (url=238ms, status=HTTP 204)
22. `AKUN-022-MYBB-VLESS-WS-73MS` (url=239ms, status=HTTP 204)
23. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-112MS` (url=232ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-293MS` (url=626ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-296MS` (url=609ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
