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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-112MS` (url=276ms, nekobox=316ms, status=yes)
2. `AKUN-002-090227-VLESS-WS-111MS` (url=289ms, nekobox=284ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-126MS` (url=278ms, nekobox=333ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-132MS` (url=291ms, nekobox=315ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-114MS` (url=303ms, nekobox=274ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-124MS` (url=248ms, nekobox=289ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-109MS` (url=254ms, nekobox=276ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-130MS` (url=252ms, nekobox=311ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-117MS` (url=250ms, nekobox=325ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-132MS` (url=248ms, nekobox=331ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-145MS` (url=282ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-133MS` (url=294ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-145MS` (url=277ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-187MS` (url=291ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-104MS` (url=259ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-299MS` (url=1106ms, status=HTTP 204)
17. `AKUN-017-CONFLU-VLESS-WS-296MS` (url=764ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-340MS` (url=746ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-312MS` (url=1823ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-319MS` (url=786ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-322MS` (url=746ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-372MS` (url=789ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-356MS` (url=720ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-271MS` (url=480ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-606MS` (url=1051ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
