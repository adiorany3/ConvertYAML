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
1. `AKUN-001-UNKNOWN-VLESS-WS-73MS` (url=212ms, nekobox=247ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=210ms, nekobox=234ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-83MS` (url=231ms, nekobox=280ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-82MS` (url=214ms, nekobox=247ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-76MS` (url=223ms, nekobox=237ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS` (url=225ms, nekobox=257ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-96MS` (url=248ms, nekobox=230ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-89MS` (url=238ms, nekobox=237ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-84MS` (url=244ms, nekobox=246ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-117MS` (url=275ms, nekobox=294ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-101MS` (url=219ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-127MS` (url=250ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-94MS` (url=213ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-119MS` (url=273ms, status=HTTP 204)
15. `AKUN-015-UK-GB-DCL-01-20191003-VLESS-WS-130MS` (url=246ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-110MS` (url=208ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-137MS` (url=227ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-125MS` (url=251ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-157MS` (url=312ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-125MS` (url=209ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-184MS` (url=422ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-168MS` (url=234ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-125MS` (url=414ms, status=HTTP 204)
24. `AKUN-025-WPENG-VLESS-WS-91MS` (url=236ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-387MS` (url=773ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
