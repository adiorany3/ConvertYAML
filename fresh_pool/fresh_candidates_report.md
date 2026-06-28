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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-70MS` (url=225ms, nekobox=241ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS` (url=234ms, nekobox=247ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS` (url=206ms, nekobox=192ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-98MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-99MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-74MS`
7. `AKUN-006-DE-XTOM-20210903-VLESS-WS-117MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-94MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-94MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-141MS` (url=232ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-97MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-244MS` (url=499ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-233MS` (url=502ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-240MS` (url=502ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-257MS` (url=555ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-265MS` (url=556ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-265MS` (url=580ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-281MS` (url=602ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-104MS` (url=461ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-291MS` (url=577ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-99MS` (url=218ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-152MS` (url=205ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-319MS` (url=552ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
