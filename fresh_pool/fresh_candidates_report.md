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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-106MS` (url=268ms, nekobox=338ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-102MS` (url=288ms, nekobox=273ms, status=yes)
3. `AKUN-003-OVH-VLESS-WS-101MS` (url=285ms, nekobox=363ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-107MS` (url=248ms, nekobox=278ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-105MS` (url=286ms, nekobox=272ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-116MS` (url=275ms, nekobox=311ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-111MS` (url=287ms, nekobox=285ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-99MS` (url=312ms, nekobox=291ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-97MS` (url=274ms, nekobox=304ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-119MS` (url=278ms, nekobox=296ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-106MS` (url=296ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-133MS` (url=328ms, status=HTTP 204)
13. `AKUN-013-DIGITALOCEAN-VLESS-WS-124MS` (url=250ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-125MS` (url=244ms, status=HTTP 204)
15. `AKUN-015-NET-NL-VLESS-WS-131MS` (url=273ms, status=HTTP 204)
16. `AKUN-016-NETCUP-VLESS-WS-116MS` (url=252ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-129MS` (url=274ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-125MS` (url=247ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-147MS` (url=274ms, status=HTTP 204)
20. `AKUN-020-466688-VLESS-WS-125MS` (url=284ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-114MS` (url=278ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-152MS` (url=294ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-104MS` (url=275ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-283MS` (url=639ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-133MS` (url=234ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
