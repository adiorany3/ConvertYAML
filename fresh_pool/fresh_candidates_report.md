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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-85MS` (url=233ms, nekobox=243ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-81MS`
3. `AKUN-004-CLOUDFLARE-VLESS-WS-96MS` (url=225ms, nekobox=202ms, status=no)
4. `AKUN-005-CLOUDFLARE-VLESS-WS-107MS` (url=232ms, nekobox=210ms, status=no)
5. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-104MS`
6. `AKUN-004-CLOUDFLARE-VLESS-WS-100MS`
7. `AKUN-008-CLOUDFLARE-VLESS-WS-114MS` (url=298ms, nekobox=201ms, status=no)
8. `AKUN-005-CLOUDFLARE-VLESS-WS-110MS`
9. `AKUN-010-CLOUDFLARE-VLESS-WS-108MS` (url=217ms, nekobox=214ms, status=no)
10. `AKUN-011-CLOUDFLARE-VLESS-WS-107MS` (url=205ms, nekobox=344ms, status=no)
11. `AKUN-006-UNKNOWN-VLESS-WS-130MS`
12. `AKUN-007-UNKNOWN-VLESS-WS-110MS`
13. `AKUN-014-DEV-VLESS-WS-115MS` (url=226ms, nekobox=205ms, status=no)
14. `AKUN-008-UNKNOWN-VLESS-WS-126MS`
15. `AKUN-016-DEV-VLESS-WS-128MS` (url=228ms, nekobox=219ms, status=no)
16. `AKUN-009-UNKNOWN-VLESS-WS-112MS`
17. `AKUN-010-UNKNOWN-VLESS-WS-132MS`
18. `AKUN-019-UNKNOWN-VLESS-WS-160MS` (url=274ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-165MS` (url=235ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-261MS` (url=509ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-260MS` (url=516ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-282MS` (url=595ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-270MS` (url=593ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-298MS` (url=577ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-302MS` (url=572ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
