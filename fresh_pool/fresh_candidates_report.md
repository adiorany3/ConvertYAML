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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-110MS` (url=249ms, nekobox=241ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-103MS` (url=245ms, nekobox=275ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-124MS` (url=244ms, nekobox=329ms, status=yes)
4. `AKUN-004-ICOOK-VLESS-WS-104MS` (url=246ms, nekobox=339ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-107MS` (url=307ms, nekobox=321ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-115MS` (url=243ms, nekobox=315ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-131MS` (url=325ms, nekobox=280ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-121MS` (url=235ms, nekobox=205ms, status=no)
9. `AKUN-008-UNKNOWN-VLESS-WS-115MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-131MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-159MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-151MS` (url=313ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-130MS` (url=276ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-150MS` (url=290ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-181MS` (url=331ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-174MS` (url=303ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-184MS` (url=437ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-101MS` (url=249ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-225MS` (url=462ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-159MS` (url=248ms, status=HTTP 204)
21. `AKUN-024-CONFLU-VLESS-WS-334MS` (url=632ms, status=HTTP 204)
22. `AKUN-026-CLOUDFLARE-VLESS-WS-415MS` (url=846ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-472MS` (url=921ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-489MS` (url=951ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-536MS` (url=1042ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
