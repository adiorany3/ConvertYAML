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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-125MS` (url=248ms, nekobox=273ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-122MS` (url=262ms, nekobox=276ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-126MS` (url=231ms, nekobox=217ms, status=no)
4. `AKUN-003-3666888-VLESS-WS-134MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-130MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-132MS`
7. `AKUN-006-GOOGLE-VLESS-WS-134MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-123MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-139MS`
10. `AKUN-009-CCWU-VLESS-WS-146MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-128MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-158MS` (url=281ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-188MS` (url=332ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-129MS` (url=246ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-133MS` (url=251ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-178MS` (url=305ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-175MS` (url=318ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-339MS` (url=687ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-357MS` (url=716ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-179MS` (url=332ms, status=HTTP 204)
21. `AKUN-022-ZVC-VLESS-WS-132MS` (url=251ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-635MS` (url=933ms, status=HTTP 204)
23. `AKUN-027-IZM-TR-GLBBTLS-VLESS-WS-628MS` (url=1040ms, status=HTTP 204)
24. `AKUN-029-CLOUDFLARE-VLESS-WS-672MS` (url=1453ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-662MS` (url=989ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
