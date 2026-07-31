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
1. `AKUN-001-ZVC-VLESS-WS-61MS` (url=225ms, nekobox=243ms, status=yes)
2. `AKUN-002-130519-VLESS-WS-60MS` (url=230ms, nekobox=247ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-64MS` (url=239ms, nekobox=251ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-67MS` (url=236ms, nekobox=274ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-79MS` (url=251ms, nekobox=262ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-73MS` (url=234ms, nekobox=280ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-60MS` (url=230ms, nekobox=255ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-85MS` (url=235ms, nekobox=258ms, status=yes)
9. `AKUN-009-EU-VLESS-WS-86MS` (url=423ms, nekobox=266ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-86MS` (url=232ms, nekobox=266ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-88MS` (url=273ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-167MS` (url=317ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-253MS` (url=565ms, status=HTTP 204)
14. `AKUN-015-NOTION-WEB-VLESS-WS-324MS` (url=758ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-437MS` (url=689ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-457MS` (url=739ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-452MS` (url=775ms, status=HTTP 204)
18. `AKUN-024-CLOUDFLARE-VLESS-WS-557MS` (url=935ms, status=HTTP 204)
19. `AKUN-027-CLOUDFLARE-VLESS-WS-509MS` (url=939ms, status=HTTP 204)
20. `AKUN-028-CLOUDFLARE-VLESS-WS-513MS` (url=1014ms, status=HTTP 204)
21. `AKUN-029-CLOUDFLARE-VLESS-WS-577MS` (url=832ms, status=HTTP 204)
22. `AKUN-031-CLOUDFLARE-VLESS-WS-609MS` (url=1267ms, status=HTTP 204)
23. `AKUN-032-CLOUDFLARE-VLESS-WS-612MS` (url=1512ms, status=HTTP 204)
24. `AKUN-033-CLOUDFLARE-VLESS-WS-641MS` (url=1230ms, status=HTTP 204)
25. `AKUN-034-CLOUDFLARE-VLESS-WS-611MS` (url=3211ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
