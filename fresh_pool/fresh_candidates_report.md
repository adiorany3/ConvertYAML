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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-55MS` (url=235ms, nekobox=239ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-56MS` (url=215ms, nekobox=237ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-60MS` (url=215ms, nekobox=259ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-64MS` (url=218ms, nekobox=311ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-61MS` (url=214ms, nekobox=254ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-62MS` (url=225ms, nekobox=260ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-66MS` (url=213ms, nekobox=261ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-99MS` (url=199ms, nekobox=170ms, status=no)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-79MS` (url=226ms, nekobox=180ms, status=no)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-123MS` (url=216ms, nekobox=170ms, status=no)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-106MS` (url=225ms, nekobox=205ms, status=no)
12. `AKUN-008-UNKNOWN-VLESS-WS-97MS`
13. `AKUN-009-CLOUDFLARE-VLESS-WS-144MS`
14. `AKUN-010-CLOUDFLARE-VLESS-WS-124MS`
15. `AKUN-015-CLOUDFLARE-VLESS-WS-92MS` (url=218ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-116MS` (url=220ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-143MS` (url=235ms, status=HTTP 204)
18. `AKUN-019-ZVC-VLESS-WS-54MS` (url=230ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-97MS` (url=234ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-80MS` (url=258ms, status=HTTP 204)
21. `AKUN-022-TANG-NET-VLESS-WS-329MS` (url=713ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-354MS` (url=769ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-345MS` (url=787ms, status=HTTP 204)
24. `AKUN-027-SUKARIO-VLESS-WS-647MS` (url=1079ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-646MS` (url=1059ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
