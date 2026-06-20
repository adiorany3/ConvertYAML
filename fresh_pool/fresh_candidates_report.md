# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 7
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-112MS` (url=218ms, nekobox=211ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-117MS`
3. `AKUN-004-CLOUDFLARE-VLESS-WS-194MS` (url=226ms, nekobox=206ms, status=no)
4. `AKUN-002-CLOUDFLARE-VLESS-WS-416MS`
5. `AKUN-003-CLOUDFLARE-VLESS-WS-400MS`
6. `AKUN-004-UNKNOWN-VLESS-WS-387MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-549MS`
8. `AKUN-012-CLOUDFLARE-VLESS-WS-647MS` (url=881ms, nekobox=748ms, status=no)
9. `AKUN-013-CLOUDFLARE-VLESS-WS-637MS` (url=1042ms, nekobox=786ms, status=no)
10. `AKUN-016-CLOUDFLARE-VLESS-WS-649MS` (url=882ms, nekobox=744ms, status=no)
11. `AKUN-018-CLOUDFLARE-VLESS-WS-645MS` (url=911ms, nekobox=743ms, status=no)
12. `AKUN-019-CLOUDFLARE-VLESS-WS-648MS` (url=952ms, nekobox=757ms, status=no)
13. `AKUN-021-CLOUDFLARE-VLESS-WS-638MS` (url=884ms, nekobox=753ms, status=no)
14. `AKUN-022-CLOUDFLARE-VLESS-WS-646MS` (url=915ms, nekobox=820ms, status=no)
15. `AKUN-023-CLOUDFLARE-VLESS-WS-647MS` (url=1010ms, nekobox=766ms, status=no)
16. `AKUN-024-CLOUDFLARE-VLESS-WS-659MS` (url=1041ms, nekobox=767ms, status=no)
17. `AKUN-025-CLOUDFLARE-VLESS-WS-750MS` (url=1459ms, nekobox=1039ms, status=no)
18. `AKUN-027-CLOUDFLARE-VLESS-WS-765MS` (url=1700ms, nekobox=938ms, status=no)
19. `AKUN-028-UNKNOWN-VLESS-WS-750MS` (url=1195ms, nekobox=7179ms, status=no)
20. `AKUN-006-UNKNOWN-VLESS-WS-809MS`
21. `AKUN-007-CLOUDFLARE-VLESS-WS-381MS`

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
