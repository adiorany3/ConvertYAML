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
1. `AKUN-001-UNKNOWN-VLESS-WS-94MS` (url=227ms, nekobox=261ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-99MS` (url=242ms, nekobox=243ms, status=yes)
3. `AKUN-003-ZOOM-VLESS-WS-105MS` (url=240ms, nekobox=244ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-107MS` (url=246ms, nekobox=243ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-106MS` (url=223ms, nekobox=245ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-103MS` (url=268ms, nekobox=305ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-113MS` (url=254ms, nekobox=286ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-127MS` (url=237ms, nekobox=258ms, status=yes)
9. `AKUN-009-WPENG-VLESS-WS-134MS` (url=227ms, nekobox=253ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-112MS` (url=209ms, nekobox=237ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-147MS` (url=260ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-117MS` (url=214ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-144MS` (url=253ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-123MS` (url=215ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-135MS` (url=247ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-118MS` (url=266ms, status=HTTP 204)
17. `AKUN-017-MYBB-VLESS-WS-142MS` (url=245ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-147MS` (url=365ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-159MS` (url=241ms, status=HTTP 204)
20. `AKUN-020-CCWU-VLESS-WS-144MS` (url=247ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-137MS` (url=284ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-223MS` (url=307ms, status=HTTP 204)
23. `AKUN-023-ORG-VLESS-WS-142MS` (url=288ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-146MS` (url=255ms, status=HTTP 204)
25. `AKUN-025-DEV-VLESS-WS-121MS` (url=225ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
