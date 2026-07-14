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
1. `AKUN-001-UNKNOWN-VLESS-WS-94MS` (url=232ms, nekobox=259ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-89MS` (url=223ms, nekobox=236ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-98MS` (url=215ms, nekobox=7172ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-91MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-90MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-113MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-115MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-114MS`
9. `AKUN-008-ES-FORNEX-20160629-VLESS-WS-99MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-102MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-112MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-109MS` (url=214ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-103MS` (url=204ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-133MS` (url=235ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-100MS` (url=203ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-98MS` (url=229ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-144MS` (url=229ms, status=HTTP 204)
18. `AKUN-019-SPEEDTEST-VLESS-WS-124MS` (url=220ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-117MS` (url=213ms, status=HTTP 204)
20. `AKUN-021-DEV-VLESS-WS-121MS` (url=206ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-120MS` (url=210ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-155MS` (url=282ms, status=HTTP 204)
23. `AKUN-024-DEV-VLESS-WS-122MS` (url=213ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-144MS` (url=246ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-133MS` (url=217ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
