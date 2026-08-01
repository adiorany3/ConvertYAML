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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-61MS` (url=203ms, nekobox=232ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-59MS` (url=200ms, nekobox=228ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-65MS` (url=205ms, nekobox=229ms, status=yes)
4. `AKUN-004-008500-VLESS-WS-64MS` (url=200ms, nekobox=237ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-73MS`
6. `AKUN-006-ALIBABA-VLESS-WS-77MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-57MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-85MS`
9. `AKUN-009-UNKNOWN-VLESS-WS-96MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-91MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-68MS` (url=211ms, status=HTTP 204)
12. `AKUN-013-DEV-VLESS-WS-94MS` (url=259ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-79MS` (url=211ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-76MS` (url=199ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-98MS` (url=208ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-93MS` (url=196ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-109MS` (url=204ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-77MS` (url=219ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-78MS` (url=199ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-388MS` (url=657ms, status=HTTP 204)
21. `AKUN-026-CLOUDFLARE-VLESS-WS-399MS` (url=718ms, status=HTTP 204)
22. `AKUN-029-CLOUDFLARE-VLESS-WS-457MS` (url=3366ms, status=HTTP 204)
23. `AKUN-030-CLOUDFLARE-VLESS-WS-496MS` (url=846ms, status=HTTP 204)
24. `AKUN-032-CLOUDFLARE-VLESS-WS-541MS` (url=937ms, status=HTTP 204)
25. `AKUN-034-CLOUDFLARE-VLESS-WS-549MS` (url=1297ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
