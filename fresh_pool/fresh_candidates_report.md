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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-UNKNOWN-VLESS-WS-99MS` (url=240ms, nekobox=238ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-103MS` (url=217ms, nekobox=248ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-104MS` (url=214ms, nekobox=244ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-113MS` (url=239ms, nekobox=271ms, status=yes)
5. `AKUN-005-SPEEDTEST-VLESS-WS-116MS` (url=258ms, nekobox=215ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-119MS`
7. `AKUN-007-DEV-VLESS-WS-112MS` (url=226ms, nekobox=220ms, status=no)
8. `AKUN-008-UNKNOWN-VLESS-WS-119MS` (url=242ms, nekobox=257ms, status=no)
9. `AKUN-009-UNKNOWN-VLESS-WS-108MS` (url=228ms, nekobox=219ms, status=no)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-99MS` (url=205ms, nekobox=201ms, status=no)
11. `AKUN-006-DEV-VLESS-WS-113MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-111MS` (url=257ms, nekobox=197ms, status=no)
13. `AKUN-007-CLOUDFLARE-VLESS-WS-109MS`
14. `AKUN-008-CLOUDFLARE-VLESS-WS-117MS`
15. `AKUN-009-UNKNOWN-VLESS-WS-122MS`
16. `AKUN-010-CLOUDFLARE-VLESS-WS-157MS`
17. `AKUN-017-CLOUDFLARE-VLESS-WS-140MS` (url=263ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-106MS` (url=244ms, status=HTTP 204)
19. `AKUN-019-BIGCOMMERCE-VLESS-WS-120MS` (url=231ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-101MS` (url=222ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-164MS` (url=227ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-118MS` (url=209ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-126MS` (url=244ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-111MS` (url=210ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-103MS` (url=222ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
