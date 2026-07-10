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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-75MS` (url=234ms, nekobox=253ms, status=yes)
2. `AKUN-002-PUBLICDOMAINREGISTRY-NET-VLESS-WS-79MS` (url=238ms, nekobox=248ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-84MS` (url=232ms, nekobox=246ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-82MS` (url=220ms, nekobox=233ms, status=yes)
5. `AKUN-005-DIGITALOCEAN-VLESS-WS-90MS` (url=213ms, nekobox=248ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-104MS` (url=225ms, nekobox=245ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-78MS` (url=226ms, nekobox=246ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-96MS` (url=227ms, nekobox=258ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS` (url=217ms, nekobox=250ms, status=yes)
10. `AKUN-010-HETZNER-VLESS-WS-102MS` (url=213ms, nekobox=318ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-111MS` (url=232ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-76MS` (url=220ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-118MS` (url=200ms, status=HTTP 204)
14. `AKUN-014-SPEEDTEST-VLESS-WS-92MS` (url=210ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-124MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-86MS` (url=206ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-121MS` (url=209ms, status=HTTP 204)
18. `AKUN-018-466688-VLESS-WS-91MS` (url=238ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-257MS` (url=575ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-266MS` (url=565ms, status=HTTP 204)
21. `AKUN-021-QZZ-VLESS-WS-231MS` (url=651ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-268MS` (url=949ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-275MS` (url=416ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-288MS` (url=699ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-279MS` (url=522ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
