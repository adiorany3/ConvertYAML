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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-97MS` (url=218ms, nekobox=254ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-109MS` (url=228ms, nekobox=258ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-103MS` (url=298ms, nekobox=355ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-110MS` (url=229ms, nekobox=267ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-121MS` (url=259ms, nekobox=214ms, status=no)
6. `AKUN-005-AEZA-NETWORK-VLESS-WS-110MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-109MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-126MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-133MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-113MS` (url=230ms, nekobox=209ms, status=no)
11. `AKUN-009-CLOUDFLARE-VLESS-WS-120MS`
12. `AKUN-010-UNKNOWN-VLESS-WS-142MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-96MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-NODEJS-VLESS-WS-126MS` (url=252ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-122MS` (url=243ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-112MS` (url=250ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-286MS` (url=1369ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-388MS` (url=838ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-386MS` (url=896ms, status=HTTP 204)
20. `AKUN-023-UNKNOWN-VLESS-WS-420MS` (url=925ms, status=HTTP 204)
21. `AKUN-024-UNKNOWN-VLESS-WS-418MS` (url=913ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-331MS` (url=385ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-417MS` (url=793ms, status=HTTP 204)
24. `AKUN-030-UNKNOWN-VLESS-WS-374MS` (url=580ms, status=HTTP 204)
25. `AKUN-033-DEV-VLESS-WS-860MS` (url=1157ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
