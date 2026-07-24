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
1. `AKUN-001-UNKNOWN-VLESS-WS-85MS` (url=219ms, nekobox=256ms, status=yes)
2. `AKUN-002-CL-173-242-112-0-20-VLESS-WS-82MS` (url=213ms, nekobox=250ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-86MS` (url=231ms, nekobox=250ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-83MS` (url=211ms, nekobox=250ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-71MS` (url=225ms, nekobox=251ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-98MS` (url=219ms, nekobox=266ms, status=yes)
7. `AKUN-007-GOOGLE-VLESS-WS-114MS` (url=207ms, nekobox=240ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-113MS` (url=387ms, nekobox=380ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-87MS` (url=219ms, nekobox=236ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-151MS` (url=341ms, nekobox=362ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-153MS` (url=283ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-102MS` (url=237ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-100MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-175MS` (url=224ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-117MS` (url=335ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-159MS` (url=253ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-90MS` (url=254ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-366MS` (url=4521ms, status=HTTP 204)
19. `AKUN-019-ZVC-VLESS-WS-100MS` (url=228ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-345MS` (url=754ms, status=HTTP 204)
21. `AKUN-021-NET-141-11-202-0-23-VLESS-WS-391MS` (url=768ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-172MS` (url=395ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-443MS` (url=4433ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-723MS` (url=1370ms, status=HTTP 204)
25. `AKUN-034-SUKARIO-VLESS-WS-802MS` (url=1029ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
