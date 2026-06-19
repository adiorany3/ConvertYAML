# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-090227-VLESS-WS-63MS` (url=221ms, nekobox=253ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-80MS` (url=237ms, nekobox=260ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-74MS` (url=261ms, nekobox=290ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-119MS` (url=207ms, nekobox=182ms, status=no)
5. `AKUN-005-SPEEDTEST-VLESS-WS-111MS` (url=243ms, nekobox=174ms, status=no)
6. `AKUN-004-CLOUDFLARE-VLESS-WS-126MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-117MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-124MS`
9. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-95MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-109MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-96MS` (url=214ms, nekobox=183ms, status=no)
12. `AKUN-013-SPEEDTEST-VLESS-WS-200MS` (url=326ms, nekobox=343ms, status=no)
13. `AKUN-014-ZENFO-1-VLESS-WS-403MS` (url=2753ms, nekobox=518ms, status=no)
14. `AKUN-009-UNKNOWN-VLESS-WS-364MS`
15. `AKUN-010-UNKNOWN-VLESS-WS-392MS`
16. `AKUN-017-CLOUDFLARE-VLESS-WS-355MS` (url=768ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-387MS` (url=833ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-409MS` (url=861ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-412MS` (url=839ms, status=HTTP 204)
20. `AKUN-027-BROADNNET-KR-VLESS-WS-740MS` (url=794ms, status=HTTP 204)
21. `AKUN-028-RS-RAPIDSEEDBOX-20190717-VLESS-WS-735MS` (url=1229ms, status=HTTP 204)
22. `AKUN-034-CLOUDFLARE-VLESS-WS-652MS` (url=899ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
