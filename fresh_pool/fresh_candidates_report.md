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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-120MS` (url=261ms, nekobox=307ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-131MS` (url=255ms, nekobox=294ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-137MS` (url=253ms, nekobox=289ms, status=yes)
4. `AKUN-004-OVH-VLESS-WS-134MS` (url=290ms, nekobox=290ms, status=yes)
5. `AKUN-005-466688-VLESS-WS-140MS` (url=250ms, nekobox=290ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-132MS` (url=267ms, nekobox=305ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-133MS` (url=290ms, nekobox=280ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-152MS` (url=276ms, nekobox=292ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-137MS` (url=277ms, nekobox=289ms, status=yes)
10. `AKUN-010-TANG-NET-VLESS-WS-142MS` (url=283ms, nekobox=337ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-130MS` (url=238ms, status=HTTP 204)
12. `AKUN-012-WPENG-VLESS-WS-151MS` (url=261ms, status=HTTP 204)
13. `AKUN-013-WPENG-VLESS-WS-148MS` (url=289ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-178MS` (url=267ms, status=HTTP 204)
15. `AKUN-015-WEYRO-NET-VLESS-WS-163MS` (url=276ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-148MS` (url=276ms, status=HTTP 204)
17. `AKUN-017-PAGES-VLESS-WS-153MS` (url=270ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-342MS` (url=673ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-365MS` (url=680ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-362MS` (url=757ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-367MS` (url=798ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-373MS` (url=909ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-385MS` (url=719ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-134MS` (url=662ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-614MS` (url=1016ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
