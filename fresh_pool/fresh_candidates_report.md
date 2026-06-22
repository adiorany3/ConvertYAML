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
1. `AKUN-001-GOV-VLESS-WS-112MS` (url=248ms, nekobox=271ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-103MS` (url=233ms, nekobox=219ms, status=no)
3. `AKUN-003-SPEEDTEST-VLESS-WS-119MS` (url=352ms, nekobox=208ms, status=no)
4. `AKUN-004-DEV-VLESS-WS-117MS` (url=230ms, nekobox=207ms, status=no)
5. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-113MS`
6. `AKUN-003-UNKNOWN-VLESS-WS-127MS`
7. `AKUN-004-UNKNOWN-VLESS-WS-124MS`
8. `AKUN-005-CLOUDFLARE-VLESS-WS-133MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-135MS` (url=231ms, nekobox=228ms, status=no)
10. `AKUN-006-GO-DADDY-COM-LLC-VLESS-WS-135MS`
11. `AKUN-007-CLOUDFLARE-VLESS-WS-133MS`
12. `AKUN-008-CLOUDFLARE-VLESS-WS-127MS`
13. `AKUN-009-UNKNOWN-VLESS-WS-147MS`
14. `AKUN-010-CLOUDFLARE-VLESS-WS-135MS`
15. `AKUN-015-CLOUDFLARE-VLESS-WS-115MS` (url=353ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-329MS` (url=577ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-334MS` (url=754ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-297MS` (url=701ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-333MS` (url=734ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-340MS` (url=619ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-386MS` (url=749ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-381MS` (url=736ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-601MS` (url=1036ms, status=HTTP 204)
24. `AKUN-030-UNKNOWN-VLESS-WS-634MS` (url=950ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-690MS` (url=1017ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
