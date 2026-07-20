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
1. `AKUN-001-UNKNOWN-VLESS-WS-135MS` (url=269ms, nekobox=316ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-140MS` (url=263ms, nekobox=315ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-135MS` (url=291ms, nekobox=309ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-145MS` (url=275ms, nekobox=303ms, status=yes)
5. `AKUN-005-SPEEDTEST-VLESS-WS-162MS` (url=247ms, nekobox=232ms, status=no)
6. `AKUN-005-UNKNOWN-VLESS-WS-140MS`
7. `AKUN-006-466688-VLESS-WS-143MS`
8. `AKUN-007-DE5-VLESS-WS-164MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-137MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-159MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-186MS`
12. `AKUN-012-466688-VLESS-WS-142MS` (url=275ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-171MS` (url=276ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-164MS` (url=303ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-150MS` (url=441ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-144MS` (url=283ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-135MS` (url=261ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-298MS` (url=407ms, status=HTTP 204)
19. `AKUN-019-SPEEDTEST-VLESS-WS-358MS` (url=727ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-352MS` (url=695ms, status=HTTP 204)
21. `AKUN-021-RS-RAPIDSEEDBOX-20190717-VLESS-WS-376MS` (url=748ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-437MS` (url=812ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-398MS` (url=746ms, status=HTTP 204)
24. `AKUN-024-RS-RAPIDSEEDBOX-20190717-VLESS-WS-440MS` (url=857ms, status=HTTP 204)
25. `AKUN-025-SPEEDTEST-VLESS-WS-408MS` (url=771ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
