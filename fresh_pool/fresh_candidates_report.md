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
1. `AKUN-001-ZOOM-VLESS-WS-92MS` (url=211ms, nekobox=237ms, status=yes)
2. `AKUN-002-NETCRAFTERS-VLESS-WS-94MS` (url=237ms, nekobox=238ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-87MS` (url=218ms, nekobox=262ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-86MS` (url=204ms, nekobox=234ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-99MS` (url=239ms, nekobox=247ms, status=yes)
6. `AKUN-006-COMPREND-NET-VLESS-WS-87MS` (url=215ms, nekobox=234ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-87MS` (url=247ms, nekobox=273ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-103MS` (url=243ms, nekobox=240ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-95MS` (url=205ms, nekobox=233ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-113MS` (url=211ms, nekobox=248ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-109MS` (url=221ms, status=HTTP 204)
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-129MS` (url=205ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-147MS` (url=214ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-199MS` (url=224ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-133MS` (url=216ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-366MS` (url=2029ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-389MS` (url=596ms, status=HTTP 204)
18. `AKUN-019-WPENG-VLESS-WS-397MS` (url=853ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-427MS` (url=814ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-430MS` (url=855ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-439MS` (url=922ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-395MS` (url=826ms, status=HTTP 204)
23. `AKUN-025-RAVINOZ-VLESS-WS-699MS` (url=1118ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-704MS` (url=1177ms, status=HTTP 204)
25. `AKUN-034-CLOUDFLARE-VLESS-WS-860MS` (url=2136ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
