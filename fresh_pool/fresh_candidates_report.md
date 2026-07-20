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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-91MS` (url=203ms, nekobox=289ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-93MS` (url=202ms, nekobox=278ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-110MS` (url=217ms, nekobox=435ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-90MS` (url=224ms, nekobox=240ms, status=yes)
5. `AKUN-005-SAVVY-7-VLESS-WS-113MS` (url=270ms, nekobox=339ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-95MS` (url=222ms, nekobox=247ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-111MS` (url=307ms, nekobox=275ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-96MS` (url=270ms, nekobox=254ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-120MS` (url=254ms, nekobox=281ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-113MS` (url=219ms, nekobox=397ms, status=yes)
11. `AKUN-011-UK-GB-DCL-01-20191003-VLESS-WS-119MS` (url=263ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-124MS` (url=237ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-124MS` (url=245ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-93MS` (url=230ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-105MS` (url=238ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-122MS` (url=247ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-119MS` (url=240ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-128MS` (url=360ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-149MS` (url=299ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-113MS` (url=244ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-127MS` (url=288ms, status=HTTP 204)
22. `AKUN-022-UK-GB-DCL-01-20191003-VLESS-WS-104MS` (url=230ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-129MS` (url=268ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-140MS` (url=247ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-138MS` (url=262ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
