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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-131MS` (url=270ms, nekobox=310ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-132MS` (url=294ms, nekobox=316ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-135MS` (url=267ms, nekobox=296ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-139MS` (url=267ms, nekobox=294ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-140MS` (url=288ms, nekobox=300ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-143MS` (url=328ms, nekobox=297ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-151MS` (url=285ms, nekobox=310ms, status=yes)
8. `AKUN-008-SPEEDTEST-VLESS-WS-162MS` (url=252ms, nekobox=236ms, status=no)
9. `AKUN-008-ES-FORNEX-20160629-VLESS-WS-149MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-168MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-145MS`
12. `AKUN-012-NODEHOST-VLESS-WS-172MS` (url=313ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-154MS` (url=277ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-142MS` (url=263ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-149MS` (url=293ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-163MS` (url=307ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-184MS` (url=322ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-167MS` (url=272ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-178MS` (url=413ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-154MS` (url=253ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-172MS` (url=313ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-286MS` (url=604ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-304MS` (url=520ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-322MS` (url=437ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-349MS` (url=702ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
