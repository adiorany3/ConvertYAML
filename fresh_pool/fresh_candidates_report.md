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
1. `AKUN-001-UNKNOWN-VLESS-WS-97MS` (url=282ms, nekobox=311ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-112MS` (url=241ms, nekobox=322ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-107MS` (url=278ms, nekobox=219ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-116MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-131MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-125MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-112MS`
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-128MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-142MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-140MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-130MS`
12. `AKUN-012-US-VLESS-WS-155MS` (url=271ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-152MS` (url=283ms, status=HTTP 204)
14. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-151MS` (url=277ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-155MS` (url=272ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-286MS` (url=577ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-288MS` (url=600ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-320MS` (url=571ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-320MS` (url=620ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-339MS` (url=706ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-329MS` (url=683ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-316MS` (url=715ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-354MS` (url=759ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-336MS` (url=661ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-579MS` (url=1002ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
