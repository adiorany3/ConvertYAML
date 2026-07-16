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
1. `AKUN-001-RU-BEGET-VLESS-WS-135MS` (url=287ms, nekobox=322ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-141MS` (url=290ms, nekobox=335ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-143MS` (url=287ms, nekobox=318ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-142MS` (url=301ms, nekobox=311ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-148MS` (url=330ms, nekobox=305ms, status=yes)
6. `AKUN-006-466688-VLESS-WS-137MS` (url=291ms, nekobox=396ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-143MS` (url=279ms, nekobox=326ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-152MS` (url=284ms, nekobox=328ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-156MS` (url=278ms, nekobox=309ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-146MS` (url=288ms, nekobox=304ms, status=yes)
11. `AKUN-011-DIXONS-VLESS-WS-151MS` (url=300ms, status=HTTP 204)
12. `AKUN-012-466688-VLESS-WS-139MS` (url=295ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-161MS` (url=297ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-152MS` (url=294ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-148MS` (url=304ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-168MS` (url=286ms, status=HTTP 204)
17. `AKUN-017-WPENG-VLESS-WS-156MS` (url=310ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-164MS` (url=300ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-165MS` (url=320ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-175MS` (url=336ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-184MS` (url=357ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-182MS` (url=314ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-162MS` (url=280ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-388MS` (url=2362ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-369MS` (url=731ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
