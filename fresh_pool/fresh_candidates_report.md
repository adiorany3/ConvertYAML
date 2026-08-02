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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-55MS` (url=219ms, nekobox=234ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-58MS` (url=209ms, nekobox=234ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-59MS` (url=225ms, nekobox=170ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-64MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-61MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-66MS`
7. `AKUN-006-008500-VLESS-WS-59MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-102MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-105MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-57MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-123MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-119MS` (url=212ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-65MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-117MS` (url=211ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-143MS` (url=275ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-73MS` (url=217ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-67MS` (url=323ms, status=HTTP 204)
18. `AKUN-018-090227-VLESS-WS-331MS` (url=586ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-519MS` (url=912ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-542MS` (url=1069ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-503MS` (url=999ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-548MS` (url=509ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-619MS` (url=1047ms, status=HTTP 204)
24. `AKUN-026-SUKARIO-VLESS-WS-596MS` (url=962ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-640MS` (url=1086ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
